import os
import logging
from datetime import datetime
import pandas as pd
from excel_handler import ExcelHandler
from utils import setup_logging, create_directories

class DataProcessor:
    def __init__(self):
        self.excel_handler = ExcelHandler()
        self.setup_environment()
        
    def setup_environment(self):
        """Set up necessary directories and logging"""
        create_directories()
        setup_logging()
        self.logger = logging.getLogger(__name__)
        
    def process_files(self, input_dir):
        """Process all Excel files in the input directory"""
        self.logger.info("Starting data processing pipeline")
        
        # Get all Excel files
        excel_files = [f for f in os.listdir(input_dir) if f.endswith(('.xlsx', '.xls'))]
        if not excel_files:
            self.logger.warning("No Excel files found in input directory")
            return
        
        # Process each file
        combined_data = pd.DataFrame()
        for file in excel_files:
            self.logger.info(f"Processing file: {file}")
            file_path = os.path.join(input_dir, file)
            
            # Read and process the file
            df = self.excel_handler.read_excel(file_path)
            df = self.clean_data(df)
            
            # Combine with existing data
            combined_data = pd.concat([combined_data, df], ignore_index=True)
        
        # Remove duplicates
        original_rows = len(combined_data)
        combined_data = combined_data.drop_duplicates()
        duplicates_removed = original_rows - len(combined_data)
        self.logger.info(f"Removed {duplicates_removed} duplicate rows")
        
        # Save processed data
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join('data', 'output', f'processed_data_{timestamp}.xlsx')
        self.excel_handler.save_excel(combined_data, output_file)
        self.logger.info(f"Saved processed data to {output_file}")
        
        return combined_data
    
    def clean_data(self, df):
        """Clean and validate the data"""
        # Remove empty rows and columns
        df = df.dropna(how='all')
        df = df.dropna(axis=1, how='all')
        
        # Strip whitespace from string columns
        for col in df.select_dtypes(['object']):
            df[col] = df[col].str.strip()
        
        # Handle missing values
        df = df.fillna('')
        
        return df

def main():
    processor = DataProcessor()
    input_dir = os.path.join('data', 'input')
    processor.process_files(input_dir)

if __name__ == "__main__":
    main()
