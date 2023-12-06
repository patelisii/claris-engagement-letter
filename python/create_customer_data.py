import pandas as pd
import sqlite3

# Load the customer data from the CSV file
customer_csv_path = 'sample_data/updated_fake_customers.csv'
customer_df = pd.read_csv(customer_csv_path)

# Re-establish connection to the SQLite database
conn = sqlite3.connect('data/SOW_engagement_letters.db')
cursor = conn.cursor()

# Check if a table for customers exists, if not, create it
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        CustomerID INTEGER PRIMARY KEY,
        Name TEXT,
        Address TEXT,
        Phone TEXT,
        Email TEXT,
        BusinessType TEXT,
        ProjectAuthority TEXT,
        Budget REAL,
        ComplianceRequirements TEXT,
        RiskManagementStrategy TEXT,
        StakeholderCount INTEGER,
        CommunicationMethod TEXT,
        QualityStandards TEXT,
        StatesOperatedIn TEXT
    )
''')
               
# Insert customer data into the table
customer_df.to_sql('customers', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
