import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_shipping_data():
    # Generate shipping records corresponding to transactions
    num_records = 1500
    
    shipping_ids = [f'SHP{str(i).zfill(8)}' for i in range(num_records)]
    transaction_ids = [f'TRX{str(random.randint(0, 1999)).zfill(8)}' for _ in range(num_records)]
    
    # Addresses with some formatting inconsistencies
    streets = ['Main St.', 'Oak Street', 'Maple Ave', 'Broadway', 'Park Road', '5th Avenue']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia']
    states = ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA']
    
    addresses = []
    for _ in range(num_records):
        street_num = random.randint(1, 9999)
        street = random.choice(streets)
        city = random.choice(cities)
        state = random.choice(states)
        zip_code = f'{random.randint(10000, 99999)}'
        
        # Introduce some inconsistencies in format
        if random.random() < 0.2:
            address = f'{street_num} {street}, {city} {state}, {zip_code}'
        else:
            address = f'{street_num} {street}\n{city}, {state} {zip_code}'
            
        addresses.append(address)
    
    # Shipping dates with some logical errors (shipped before order)
    base_dates = [datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365)) for _ in range(num_records)]
    shipping_dates = []
    delivery_dates = []
    
    for base_date in base_dates:
        if random.random() < 0.05:  # 5% chance of incorrect dates
            shipping_date = base_date - timedelta(days=random.randint(1, 5))
        else:
            shipping_date = base_date + timedelta(days=random.randint(1, 3))
            
        delivery_date = shipping_date + timedelta(days=random.randint(2, 7))
        shipping_dates.append(shipping_date)
        delivery_dates.append(delivery_date)
    
    df = pd.DataFrame({
        'ShippingID': shipping_ids,
        'TransactionID': transaction_ids,
        'ShippingAddress': addresses,
        'ShippingDate': shipping_dates,
        'DeliveryDate': delivery_dates,
        'ShippingMethod': np.random.choice(['Standard', 'Express', 'Next Day'], num_records, p=[0.6, 0.3, 0.1]),
        'TrackingNumber': [f'TRK{random.randint(100000, 999999)}' if random.random() > 0.1 else None for _ in range(num_records)]
    })
    
    return df

def generate_product_reviews():
    # Generate product reviews with text data
    num_records = 800
    
    product_ids = [f'PRD{str(random.randint(0, 7)).zfill(4)}' for _ in range(num_records)]
    customer_ids = [f'CUS{str(random.randint(0, 999)).zfill(6)}' for _ in range(num_records)]
    
    # Review templates with placeholders
    positive_templates = [
        "Great {product}! {feature} works perfectly.",
        "Excellent quality {product}. Worth every penny.",
        "The {feature} of this {product} is outstanding.",
        "Very satisfied with my {product} purchase."
    ]
    
    negative_templates = [
        "Disappointed with the {product}. {feature} needs improvement.",
        "The {product} didn't meet expectations. {feature} is lacking.",
        "Had issues with the {feature} of this {product}.",
        "Not happy with my {product} purchase."
    ]
    
    neutral_templates = [
        "Average {product}. {feature} is okay.",
        "The {product} is decent but could be better.",
        "Not bad, but the {feature} could use some work.",
        "Mediocre {product} for the price."
    ]
    
    features = {
        'Laptop': ['battery life', 'performance', 'display', 'keyboard'],
        'Smartphone': ['camera', 'battery', 'screen', 'speed'],
        'Tablet': ['touch response', 'display', 'battery life', 'performance'],
        'Monitor': ['picture quality', 'refresh rate', 'color accuracy', 'brightness'],
        'Keyboard': ['key feel', 'build quality', 'RGB lighting', 'ergonomics'],
        'Mouse': ['sensor accuracy', 'ergonomics', 'button feel', 'wireless connection'],
        'Headphones': ['sound quality', 'comfort', 'noise cancellation', 'battery life'],
        'Printer': ['print quality', 'speed', 'paper handling', 'ink efficiency']
    }
    
    reviews = []
    ratings = []
    products = []
    dates = []
    
    for _ in range(num_records):
        product = random.choice(list(features.keys()))
        feature = random.choice(features[product])
        rating = random.randint(1, 5)
        
        if rating >= 4:
            template = random.choice(positive_templates)
        elif rating <= 2:
            template = random.choice(negative_templates)
        else:
            template = random.choice(neutral_templates)
            
        review = template.format(product=product.lower(), feature=feature)
        
        # Add some typos and formatting issues
        if random.random() < 0.1:
            review = review.replace('the', 'teh').replace('with', 'wiht')
        
        reviews.append(review)
        ratings.append(rating)
        products.append(product)
        dates.append(datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365)))
    
    df = pd.DataFrame({
        'ProductID': product_ids,
        'CustomerID': customer_ids,
        'Product': products,
        'Rating': ratings,
        'ReviewText': reviews,
        'ReviewDate': dates,
        'Verified': np.random.choice([True, False], num_records, p=[0.8, 0.2])
    })
    
    return df

def generate_error_logs():
    # Generate system error logs with timestamps and severity levels
    num_records = 500
    
    error_types = [
        'DatabaseConnectionError',
        'FileNotFoundError',
        'ValidationError',
        'NetworkTimeoutError',
        'AuthenticationError'
    ]
    
    components = [
        'DataProcessor',
        'ExcelHandler',
        'DatabaseConnector',
        'APIService',
        'UserAuthentication'
    ]
    
    messages = []
    timestamps = []
    error_codes = []
    
    for _ in range(num_records):
        error_type = random.choice(error_types)
        component = random.choice(components)
        
        # Generate semi-structured error messages
        if error_type == 'DatabaseConnectionError':
            message = f"Failed to connect to database: timeout after {random.randint(30, 120)} seconds"
        elif error_type == 'FileNotFoundError':
            message = f"File 'data_{random.randint(1, 100)}.xlsx' not found in path /data/input/"
        elif error_type == 'ValidationError':
            message = f"Invalid data format in column {random.choice(['Name', 'Email', 'Phone', 'Date'])}"
        elif error_type == 'NetworkTimeoutError':
            message = f"Network request timed out after {random.randint(10, 60)} seconds"
        else:
            message = f"Authentication failed for user ID: USR{random.randint(1000, 9999)}"
            
        messages.append(f"[{component}] {error_type}: {message}")
        timestamps.append(datetime(2023, 1, 1) + timedelta(
            days=random.randint(0, 365),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59)
        ))
        error_codes.append(random.randint(4000, 5999))
    
    df = pd.DataFrame({
        'Timestamp': timestamps,
        'Severity': np.random.choice(['ERROR', 'WARNING', 'CRITICAL'], num_records, p=[0.5, 0.3, 0.2]),
        'ErrorCode': error_codes,
        'Message': messages,
        'Resolution': np.random.choice(['Resolved', 'Pending', 'In Progress', None], num_records, p=[0.6, 0.2, 0.1, 0.1])
    })
    
    return df

def main():
    # Generate additional datasets
    shipping_df = generate_shipping_data()
    reviews_df = generate_product_reviews()
    error_logs_df = generate_error_logs()
    
    # Save to Excel files with different formats and sheets
    with pd.ExcelWriter('data/input/shipping_data.xlsx', engine='openpyxl') as writer:
        shipping_df.to_excel(writer, sheet_name='Shipping Records', index=False)
        
        # Add a summary sheet
        summary_data = shipping_df['ShippingMethod'].value_counts().reset_index()
        summary_data.columns = ['Method', 'Count']
        summary_data.to_excel(writer, sheet_name='Summary', index=False)
    
    # Save reviews with some formatting
    reviews_df.to_excel('data/input/product_reviews.xlsx', index=False)
    
    # Save error logs with timestamp as index
    error_logs_df.set_index('Timestamp').to_excel('data/input/error_logs.xlsx')
    
    print("Additional sample data files have been generated in the data/input directory:")
    print("1. shipping_data.xlsx - Shipping records with address inconsistencies")
    print("2. product_reviews.xlsx - Product reviews with text data and ratings")
    print("3. error_logs.xlsx - System error logs with timestamps")

if __name__ == "__main__":
    main()
