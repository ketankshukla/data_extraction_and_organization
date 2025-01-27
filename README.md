# Data Extraction and Organization Project

A Python-based pipeline for processing and organizing client data from multiple Excel files.

## Features
- Automated data processing from multiple Excel sources
- Data cleaning, filtering, and deduplication using Pandas
- Automated data merging and validation
- Improved data consistency and processing efficiency

## Setup
1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```
     .\venv\Scripts\activate
     ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Project Structure
- `src/`: Source code directory
  - `data_processor.py`: Main data processing logic
  - `excel_handler.py`: Excel file operations
  - `utils.py`: Utility functions
- `config/`: Configuration files
- `data/`: Directory for input/output data files
- `logs/`: Log files directory

## Usage
1. Place your Excel files in the `data/input` directory
2. Run the main script:
   ```
   python src/data_processor.py
   ```
3. Processed data will be saved in the `data/output` directory
