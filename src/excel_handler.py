import pandas as pd
import logging

class ExcelHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def read_excel(self, file_path):
        """Read an Excel file and return a pandas DataFrame"""
        try:
            df = pd.read_excel(file_path)
            self.logger.info(f"Successfully read {file_path}")
            return df
        except Exception as e:
            self.logger.error(f"Error reading {file_path}: {str(e)}")
            raise
    
    def save_excel(self, df, file_path):
        """Save DataFrame to Excel file"""
        try:
            df.to_excel(file_path, index=False)
            self.logger.info(f"Successfully saved data to {file_path}")
        except Exception as e:
            self.logger.error(f"Error saving to {file_path}: {str(e)}")
            raise
