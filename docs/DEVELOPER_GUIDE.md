# 👨‍💻 Developer Guide

## 🏗️ Project Structure

```
data_extraction_and_organization/
├── data/
│   ├── input/        # Place Excel files here
│   └── output/       # Processed files appear here
├── src/
│   ├── data_processor.py
│   ├── excel_handler.py
│   └── utils.py
├── logs/             # Processing logs
└── venv/             # Virtual environment
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- pip (Python package manager)

### 🔧 Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ketankshukla/data_extraction_and_organization.git
   cd data_extraction_and_organization
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🏗️ Code Architecture

### 📁 `data_processor.py`
- Main processing pipeline
- Class: `DataProcessor`
  - `process_files()`: Main entry point for processing
  - `clean_data()`: Data cleaning and validation

### 📁 `excel_handler.py`
- Excel file operations
- Class: `ExcelHandler`
  - `read_excel()`: Read Excel files
  - `save_excel()`: Save processed data

### 📁 `utils.py`
- Utility functions
- Functions:
  - `create_directories()`: Set up project directories
  - `setup_logging()`: Configure logging

## 🧪 Testing

### Running Tests
```bash
python -m pytest tests/
```

### Adding New Tests
1. Create test files in the `tests/` directory
2. Follow the naming convention: `test_*.py`
3. Use pytest fixtures for common setup

## 📝 Coding Standards

### Style Guide
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to all functions and classes

### Best Practices
1. **Error Handling**
   - Use try-except blocks for file operations
   - Log errors with appropriate levels

2. **Logging**
   - Use the logging module
   - Include relevant context in log messages

3. **Code Organization**
   - Keep functions focused and single-purpose
   - Use classes for related functionality

## 🔄 Git Workflow

1. **Creating a new feature**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Making changes**
   ```bash
   git add .
   git commit -m "feat: your descriptive message"
   ```

3. **Pushing changes**
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request on GitHub

## 🚀 Deployment

### Building for Production
1. Ensure all tests pass
2. Update version numbers
3. Create a release tag

### Release Process
1. Merge to main branch
2. Tag release version
3. Update changelog

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📚 Additional Resources

- [Python Documentation](https://docs.python.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [OpenPyXL Documentation](https://openpyxl.readthedocs.io/)

## Data Processing Pipeline

The data processing pipeline is implemented in `src/data_processor.py` and consists of the following components:

### Core Components

1. **DataProcessor Class**
   - Main class that orchestrates the data processing workflow
   - Handles file reading, cleaning, and saving processed data
   - Implements specialized cleaning functions for different data types
   - Generates detailed processing summaries and logs

2. **ExcelHandler Class**
   - Handles Excel file operations (reading and writing)
   - Supports different sheet names and data formats
   - Implements error handling for Excel operations

### Logging and Error Handling

The pipeline uses Python's built-in logging module with the following features:
- Detailed logging of processing steps and errors
- Both console and file output (logs stored in `data/output/processing.log`)
- Log rotation to prevent excessive file sizes
- Comprehensive error tracking and reporting

### Data Cleaning Functions

Specialized cleaning functions for different data types:
- `clean_customer_data`: Handles customer information and deduplication
- `clean_transaction_data`: Processes transaction records and payment methods
- `clean_inventory_data`: Manages product inventory and stock levels
- `clean_shipping_data`: Validates shipping dates and addresses
- `clean_review_data`: Processes product reviews and ratings
- `clean_error_logs`: Handles system error logs and timestamps

### Output Files

The pipeline generates several output files in the `data/output` directory:
1. Processed data files with `processed_` prefix
2. Processing summary with statistics for each file
3. Detailed log file with processing steps and errors

### Sample Data

Sample data files are provided in `data/input` for testing:
- `customer_data.xlsx`: Customer information
- `transaction_data.xlsx`: Transaction records
- `inventory_data.xlsx`: Product inventory
- `shipping_data.xlsx`: Shipping records
- `product_reviews.xlsx`: Product reviews
- `error_logs.xlsx`: System error logs
- `combined_data.xlsx`: Combined dataset
