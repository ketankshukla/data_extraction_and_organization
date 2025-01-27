# 📘 User Guide

## 🌟 Overview

The Data Extraction and Organization tool is designed to help you process and organize data from multiple Excel files efficiently. This guide will walk you through how to use the tool effectively.

## 🚀 Getting Started

### System Requirements
- Windows, macOS, or Linux operating system
- Python 3.8 or higher installed
- Minimum 4GB RAM recommended

### 📥 Installation

1. **Download the Project**
   ```bash
   git clone https://github.com/ketankshukla/data_extraction_and_organization.git
   cd data_extraction_and_organization
   ```

2. **Set Up Environment**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Using the Tool

### 1. Preparing Your Data

#### Supported File Formats
- Excel files (.xlsx, .xls)
- Files should have consistent column headers
- Data should be organized in rows and columns

#### File Organization
1. Place your Excel files in the `data/input` directory
2. Ensure files have proper read permissions

### 2. Running the Process

1. **Start the Processing**
   ```bash
   python src/data_processor.py
   ```

2. **Monitor Progress**
   - Check the console for real-time progress
   - Review logs in the `logs` directory

### 3. Output Files

- Processed files are saved in `data/output`
- Files are named with timestamp: `processed_data_YYYYMMDD_HHMMSS.xlsx`
- Original files remain unchanged in the input directory

## 📋 Features

### 1. Data Cleaning
- Removes empty rows and columns
- Strips whitespace from text
- Handles missing values

### 2. Deduplication
- Identifies and removes duplicate records
- Maintains data integrity

### 3. Data Validation
- Ensures data consistency
- Validates data formats

## 📊 Example Usage

### Basic Processing
1. Copy Excel files to `data/input`
2. Run the processor
3. Collect results from `data/output`

### Advanced Usage
- Multiple files are processed in sequence
- Results are combined into a single output file
- Detailed logs are generated for tracking

## 📊 Running the Data Processing Pipeline

The data processing pipeline can handle various types of Excel files. Here's how to use it:

1. **Prepare Your Data**
   - Place your Excel files in the `data/input` directory
   - Supported file types:
     - Customer data (filename contains "customer")
     - Transaction data (filename contains "transaction")
     - Inventory data (filename contains "inventory")
     - Shipping data (filename contains "shipping")
     - Product reviews (filename contains "review")
     - Error logs (filename contains "error")
     - Combined data (any other Excel file)

2. **Run the Pipeline**
   ```bash
   python src/data_processor.py
   ```

3. **Check the Results**
   - Processed files will be in `data/output` with a `processed_` prefix
   - A processing summary file shows statistics for each processed file
   - Check `data/output/processing.log` for detailed processing steps and any errors

### Understanding the Output

1. **Processed Files**
   - Each processed file maintains the same structure as the input
   - Data is cleaned and standardized
   - Invalid or duplicate records are removed

2. **Processing Summary**
   The summary file contains:
   - Number of records processed per file
   - Column names
   - File-specific statistics:
     - Customer data: Missing phone numbers
     - Transaction data: Total transaction amount
     - Shipping data: Invalid shipping dates
     - Product reviews: Average rating
     - Inventory data: Products below reorder point

3. **Log File**
   The log file (`processing.log`) shows:
   - Start and end of processing for each file
   - Number of records before and after cleaning
   - Any errors or warnings encountered
   - Processing completion status

### Troubleshooting

Common issues and solutions:

1. **File Not Processed**
   - Check if the file is in the correct directory
   - Ensure the file has a `.xlsx` extension
   - Verify the file is not corrupted

2. **Missing Statistics**
   - Ensure your file follows the expected format
   - Check if required columns are present
   - Review the log file for specific errors

3. **Invalid Dates**
   - For shipping data, ensure dates are in a valid format
   - Check if delivery dates are after shipping dates

### Best Practices

1. **File Naming**
   - Use descriptive names that indicate the data type
   - Include the data type in the filename (e.g., "customer", "transaction")
   - Avoid special characters in filenames

2. **Data Preparation**
   - Back up your data before processing
   - Ensure dates are in a consistent format
   - Remove any password protection from Excel files

3. **Monitoring**
   - Check the log file regularly
   - Review processing summaries for unexpected results
   - Keep track of the number of records processed

## 🔍 Troubleshooting

### Common Issues

1. **File Not Found**
   - Ensure files are in the correct directory
   - Check file permissions

2. **Processing Errors**
   - Verify Excel file format
   - Check for corrupted files
   - Review log files for details

3. **Memory Issues**
   - Process fewer files at once
   - Close other applications

### Error Messages

| Error | Solution |
|-------|----------|
| "Permission denied" | Check file permissions |
| "Invalid file format" | Ensure file is proper Excel format |
| "Out of memory" | Process smaller batches |

## 📈 Best Practices

1. **File Preparation**
   - Use consistent column headers
   - Remove unnecessary formatting
   - Save files in .xlsx format

2. **Processing**
   - Process similar files together
   - Regular backups of input files
   - Monitor system resources

3. **Data Management**
   - Organize files by date/category
   - Regular cleanup of output directory
   - Maintain backup copies

## 🆘 Getting Help

### Support Resources
- Check the logs in `logs` directory
- Review error messages
- Consult documentation

### Contact
For additional support:
- Create an issue on GitHub
- Contact the development team

## 📝 Tips and Tricks

1. **Optimize Performance**
   - Process similar files together
   - Regular cleanup of temp files
   - Monitor system resources

2. **Data Organization**
   - Use consistent naming conventions
   - Organize files by date/category
   - Regular backups

3. **Best Results**
   - Clean data before processing
   - Validate output regularly
   - Keep software updated
