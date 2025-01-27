import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)

def generate_customer_data():
    # Generate sample customer data
    num_records = 1000
    
    # Customer IDs
    customer_ids = [f'CUS{str(i).zfill(6)}' for i in range(num_records)]
    
    # Names
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'James', 'Emma', 'William', 'Olivia']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    
    names = [f'{random.choice(first_names)} {random.choice(last_names)}' for _ in range(num_records)]
    
    # Email addresses
    emails = [f'{name.lower().replace(" ", ".")}@example.com' for name in names]
    
    # Phone numbers
    phone_numbers = [f'+1-{random.randint(200, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}' for _ in range(num_records)]
    
    # Dates
    start_date = datetime(2023, 1, 1)
    registration_dates = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(num_records)]
    
    # Create DataFrame
    df = pd.DataFrame({
        'CustomerID': customer_ids,
        'Name': names,
        'Email': emails,
        'Phone': phone_numbers,
        'RegistrationDate': registration_dates,
        'Status': np.random.choice(['Active', 'Inactive', 'Pending'], num_records, p=[0.7, 0.2, 0.1])
    })
    
    return df

def generate_transaction_data():
    # Generate sample transaction data
    num_records = 2000
    
    # Transaction IDs
    transaction_ids = [f'TRX{str(i).zfill(8)}' for i in range(num_records)]
    
    # Customer IDs (some customers will have multiple transactions)
    customer_ids = [f'CUS{str(random.randint(0, 999)).zfill(6)}' for _ in range(num_records)]
    
    # Products
    products = ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Headphones', 'Printer']
    product_prices = {
        'Laptop': (800, 2000),
        'Smartphone': (400, 1200),
        'Tablet': (200, 800),
        'Monitor': (150, 500),
        'Keyboard': (20, 150),
        'Mouse': (10, 80),
        'Headphones': (30, 300),
        'Printer': (100, 400)
    }
    
    selected_products = np.random.choice(products, num_records)
    amounts = [random.uniform(product_prices[p][0], product_prices[p][1]) for p in selected_products]
    
    # Dates
    start_date = datetime(2023, 1, 1)
    transaction_dates = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(num_records)]
    
    # Create DataFrame
    df = pd.DataFrame({
        'TransactionID': transaction_ids,
        'CustomerID': customer_ids,
        'Product': selected_products,
        'Amount': amounts,
        'TransactionDate': transaction_dates,
        'PaymentMethod': np.random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer'], num_records),
        'Status': np.random.choice(['Completed', 'Pending', 'Failed'], num_records, p=[0.85, 0.1, 0.05])
    })
    
    return df

def generate_product_inventory():
    # Generate sample product inventory data
    products = [
        ('Laptop', 'Electronics', 'High-end computing device'),
        ('Smartphone', 'Electronics', 'Mobile communication device'),
        ('Tablet', 'Electronics', 'Portable computing device'),
        ('Monitor', 'Electronics', 'Display device'),
        ('Keyboard', 'Accessories', 'Input device'),
        ('Mouse', 'Accessories', 'Pointing device'),
        ('Headphones', 'Accessories', 'Audio device'),
        ('Printer', 'Electronics', 'Printing device')
    ]
    
    df = pd.DataFrame({
        'ProductID': [f'PRD{str(i).zfill(4)}' for i in range(len(products))],
        'ProductName': [p[0] for p in products],
        'Category': [p[1] for p in products],
        'Description': [p[2] for p in products],
        'InStock': np.random.randint(10, 200, len(products)),
        'ReorderPoint': np.random.randint(5, 50, len(products)),
        'LastRestockDate': [datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365)) for _ in range(len(products))]
    })
    
    return df

def main():
    # Generate all datasets
    customer_df = generate_customer_data()
    transaction_df = generate_transaction_data()
    inventory_df = generate_product_inventory()
    
    # Add some duplicates and inconsistencies for testing
    # Duplicate some customer records with slight modifications
    duplicates = customer_df.head(50).copy()
    duplicates['Email'] = duplicates['Email'].str.replace('@example.com', '@email.com')
    customer_df = pd.concat([customer_df, duplicates])
    
    # Add some missing values
    transaction_df.loc[np.random.choice(transaction_df.index, 50), 'PaymentMethod'] = None
    customer_df.loc[np.random.choice(customer_df.index, 30), 'Phone'] = None
    
    # Save to Excel files
    customer_df.to_excel('data/input/customer_data.xlsx', index=False)
    transaction_df.to_excel('data/input/transaction_data.xlsx', index=False)
    inventory_df.to_excel('data/input/inventory_data.xlsx', index=False)
    
    # Create a combined dataset with some overlapping information
    combined_df = transaction_df.merge(customer_df[['CustomerID', 'Name', 'Email']], 
                                     on='CustomerID', how='left')
    combined_df.to_excel('data/input/combined_data.xlsx', index=False)
    
    print("Sample data files have been generated in the data/input directory:")
    print("1. customer_data.xlsx - Customer information with some duplicates")
    print("2. transaction_data.xlsx - Transaction records with some missing payment methods")
    print("3. inventory_data.xlsx - Product inventory status")
    print("4. combined_data.xlsx - Combined transaction and customer data")

if __name__ == "__main__":
    main()
