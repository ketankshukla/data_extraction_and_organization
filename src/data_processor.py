import os
import pandas as pd
import numpy as np
from datetime import datetime
import logging
from excel_handler import ExcelHandler
from utils import create_directories

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('data/output/processing.log', encoding='utf-8')
    ]
)

class DataProcessor:
    def __init__(self):
        self.excel_handler = ExcelHandler()
        self.setup_environment()
        
    def setup_environment(self):
        """Set up necessary directories and logging"""
        create_directories()
        
    def process_files(self, input_dir):
        """Process all Excel files in the input directory"""
        logger = logging.getLogger(__name__)
        logger.info("Starting data processing pipeline")
        
        # Get all Excel files
        excel_files = [f for f in os.listdir(input_dir) if f.endswith(('.xlsx', '.xls'))]
        if not excel_files:
            logger.warning("No Excel files found in input directory")
            return
            
        logger.info(f"Found {len(excel_files)} Excel files to process: {', '.join(excel_files)}")
        
        # Process each file
        processed_data = {}
        error_count = 0
        success_count = 0
        
        for file in excel_files:
            try:
                logger.info(f"\n{'='*50}")
                logger.info(f"Processing file: {file}")
                file_path = os.path.join(input_dir, file)
                
                # Read the file
                try:
                    if file == 'shipping_data.xlsx':
                        logger.info("Reading shipping data from 'Shipping Records' sheet")
                        df = self.excel_handler.read_excel(file_path, sheet_name='Shipping Records')
                    else:
                        df = self.excel_handler.read_excel(file_path)
                    
                    logger.info(f"Successfully read file with {len(df)} records and {len(df.columns)} columns")
                    logger.info(f"Columns: {', '.join(df.columns)}")
                except Exception as e:
                    logger.error(f"Error reading file {file}: {str(e)}")
                    error_count += 1
                    continue
                
                # Apply appropriate cleaning based on file type
                try:
                    initial_count = len(df)
                    if 'customer' in file.lower():
                        logger.info("Applying customer data cleaning")
                        df = self.clean_customer_data(df)
                    elif 'transaction' in file.lower():
                        logger.info("Applying transaction data cleaning")
                        df = self.clean_transaction_data(df)
                    elif 'inventory' in file.lower():
                        logger.info("Applying inventory data cleaning")
                        df = self.clean_inventory_data(df)
                    elif 'shipping' in file.lower():
                        logger.info("Applying shipping data cleaning")
                        df = self.clean_shipping_data(df)
                    elif 'review' in file.lower():
                        logger.info("Applying review data cleaning")
                        df = self.clean_review_data(df)
                    elif 'error' in file.lower():
                        logger.info("Applying error log cleaning")
                        df = self.clean_error_logs(df)
                    else:
                        logger.info("Applying general data cleaning")
                        df = self.clean_data(df)
                    
                    final_count = len(df)
                    records_removed = initial_count - final_count
                    logger.info(f"Cleaning complete: {records_removed} records removed")
                    logger.info(f"Final record count: {final_count}")
                    
                except Exception as e:
                    logger.error(f"Error cleaning file {file}: {str(e)}")
                    error_count += 1
                    continue
                
                processed_data[file] = df
                success_count += 1
                logger.info(f"Successfully processed {file}")
                
            except Exception as e:
                logger.error(f"Unexpected error processing {file}: {str(e)}")
                error_count += 1
                continue
        
        logger.info(f"\n{'='*50}")
        logger.info(f"Processing complete:")
        logger.info(f"Successfully processed: {success_count} files")
        logger.info(f"Errors encountered: {error_count} files")
        
        # Save processed data
        if processed_data:
            self.save_processed_data(processed_data)
        else:
            logger.error("No files were successfully processed")
        
        return processed_data
    
    def clean_customer_data(self, df):
        """Clean customer-specific data"""
        df = self.clean_data(df)
        
        # Standardize email addresses
        if 'Email' in df.columns:
            df['Email'] = df['Email'].str.lower()
        
        # Format phone numbers
        if 'Phone' in df.columns:
            df['Phone'] = df['Phone'].apply(lambda x: self.standardize_phone(x) if pd.notna(x) else x)
        
        # Remove duplicate customers based on Email
        if 'Email' in df.columns:
            df = df.drop_duplicates(subset=['Email'], keep='first')
        
        return df
    
    def clean_transaction_data(self, df):
        """Clean transaction-specific data"""
        df = self.clean_data(df)
        
        # Round amounts to 2 decimal places
        if 'Amount' in df.columns:
            df['Amount'] = df['Amount'].round(2)
        
        # Ensure dates are datetime
        if 'TransactionDate' in df.columns:
            df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
        
        return df
    
    def clean_shipping_data(self, df):
        """Clean shipping-specific data"""
        df = self.clean_data(df)
        
        # Standardize addresses
        if 'ShippingAddress' in df.columns:
            df['ShippingAddress'] = df['ShippingAddress'].str.replace('\n', ', ')
        
        # Validate shipping dates
        date_columns = ['ShippingDate', 'DeliveryDate']
        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col])
        
        # Flag invalid dates (delivery before shipping)
        if all(col in df.columns for col in date_columns):
            df['InvalidDates'] = df['DeliveryDate'] < df['ShippingDate']
            logger = logging.getLogger(__name__)
            logger.warning(f"Found {df['InvalidDates'].sum()} records with invalid shipping dates")
        
        return df
    
    def clean_review_data(self, df):
        """Clean review-specific data"""
        df = self.clean_data(df)
        
        # Clean review text
        if 'ReviewText' in df.columns:
            df['ReviewText'] = df['ReviewText'].apply(self.clean_text)
        
        # Validate ratings
        if 'Rating' in df.columns:
            df.loc[~df['Rating'].between(1, 5), 'Rating'] = None
        
        return df
    
    def clean_error_logs(self, df):
        """Clean error log data"""
        df = self.clean_data(df)
        
        # Ensure timestamp is datetime
        if 'Timestamp' in df.columns:
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        
        # Extract error type and component from message
        if 'Message' in df.columns:
            df[['Component', 'ErrorType', 'Details']] = df['Message'].str.extract(r'\[(.*?)\] (.*?): (.*)')
        
        return df
    
    def clean_inventory_data(self, df):
        """Clean inventory-specific data"""
        df = self.clean_data(df)
        
        # Ensure numeric columns are integers
        numeric_columns = ['InStock', 'ReorderPoint']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
        
        return df
    
    def clean_data(self, df):
        """General data cleaning"""
        # Remove empty rows and columns
        df = df.dropna(how='all')
        df = df.dropna(axis=1, how='all')
        
        # Strip whitespace from string columns
        for col in df.select_dtypes(['object']):
            df[col] = df[col].str.strip() if df[col].dtype == 'object' else df[col]
        
        return df
    
    def standardize_phone(self, phone):
        """Standardize phone number format"""
        if pd.isna(phone):
            return None
        # Remove all non-numeric characters
        nums = ''.join(filter(str.isdigit, str(phone)))
        if len(nums) == 10:
            return f'+1-{nums[:3]}-{nums[3:6]}-{nums[6:]}'
        elif len(nums) == 11 and nums.startswith('1'):
            return f'+{nums[0]}-{nums[1:4]}-{nums[4:7]}-{nums[7:]}'
        return phone
    
    def clean_text(self, text):
        """Clean text data"""
        if pd.isna(text):
            return None
        # Fix common typos
        text = text.replace('teh', 'the').replace('wiht', 'with')
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    def save_processed_data(self, processed_data):
        """Save all processed data"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save individual files
        for filename, df in processed_data.items():
            output_file = os.path.join('data', 'output', f'processed_{filename}')
            self.excel_handler.save_excel(df, output_file)
            logger = logging.getLogger(__name__)
            logger.info(f"Saved processed data to {output_file}")
        
        # Create a summary report
        summary_file = os.path.join('data', 'output', f'processing_summary_{timestamp}.txt')
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("Data Processing Summary\n")
            f.write("=====================\n\n")
            
            for filename, df in processed_data.items():
                f.write(f"\nFile: {filename}\n")
                f.write(f"Records processed: {len(df)}\n")
                f.write(f"Columns: {', '.join(df.columns)}\n")
                
                # Add specific statistics based on file type
                if 'customer' in filename.lower():
                    null_phones = df['Phone'].isna().sum()
                    f.write(f"Missing phone numbers: {null_phones}\n")
                    
                elif 'transaction' in filename.lower():
                    total_amount = df['Amount'].sum() if 'Amount' in df.columns else 0
                    f.write(f"Total transaction amount: ${total_amount:,.2f}\n")
                    
                elif 'shipping' in filename.lower() and 'InvalidDates' in df.columns:
                    invalid_dates = df['InvalidDates'].sum()
                    f.write(f"Invalid shipping dates found: {invalid_dates}\n")
                    
                elif 'review' in filename.lower() and 'Rating' in df.columns:
                    avg_rating = df['Rating'].mean()
                    f.write(f"Average rating: {avg_rating:.2f}\n")
                    
                elif 'inventory' in filename.lower():
                    low_stock = df[df['InStock'] <= df['ReorderPoint']].shape[0]
                    f.write(f"Products below reorder point: {low_stock}\n")
                
                f.write("-" * 50 + "\n")
        
        logger.info(f"Created processing summary: {summary_file}")

def main():
    processor = DataProcessor()
    input_dir = os.path.join('data', 'input')
    processor.process_files(input_dir)

if __name__ == "__main__":
    main()
