import os
import logging
from datetime import datetime

def create_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        os.path.join('data', 'input'),
        os.path.join('data', 'output'),
        'logs',
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

def setup_logging():
    """Configure logging settings"""
    log_filename = os.path.join('logs', f'processing_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
