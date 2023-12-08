import pandas as pd
import sqlite3

# Load the customer data from the CSV file
customer_csv_path = 'sample_data/updated_fake_customers.csv'
customer_df = pd.read_csv(customer_csv_path)

# Re-establish connection to the SQLite database
conn = sqlite3.connect('data/SOW_engagement_letters.db')
cursor = conn.cursor()

# create_tables()

def load_csv_to_table(csv_file, table_name):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    # Upload DataFrame to SQLite table
    df.to_sql(table_name, conn, if_exists='append', index=False)
               
load_csv_to_table('sample_data/customers.csv', 'customers')
load_csv_to_table('sample_data/msa.csv', 'msa_engagements')
load_csv_to_table('sample_data/sow_engagements.csv', 'sow_engagements')
load_csv_to_table('sample_data/consulting_details.csv', 'consulting_details')
load_csv_to_table('sample_data/compliance_details.csv', 'compliance_details')


# Close the connection
conn.close()

def create_tables():
    conn = sqlite3.connect('data/SOW_engagement_letters.db')
    cursor = conn.cursor()

    # Check if a table for customers exists, if not, create it
    cursor.execute('''
        CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT
    );
    '''
    )
    cursor.execute('''
    CREATE TABLE msa_engagements (
        engagement_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    );
    ''')
    cursor.execute('''
    CREATE TABLE sow_engagements (
        engagement_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        engagement_type TEXT,
        date TEXT,
        signer_name TEXT,
        signer_title TEXT,
        partner_name TEXT,
        partner_contact_number TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    );
    ''')
    cursor.execute('''
    CREATE TABLE consulting_details (
        consulting_id INTEGER PRIMARY KEY AUTOINCREMENT,
        engagement_id INTEGER,
        service_year TEXT,
        consulting_fee_amount TEXT,
        payment_terms TEXT,
        information_deadline TEXT,
        completion_date TEXT,
        consulting_services TEXT,
        FOREIGN KEY (engagement_id) REFERENCES engagements (engagement_id)
    );
    ''')
    cursor.execute('''
    CREATE TABLE compliance_details (
        compliance_id INTEGER PRIMARY KEY AUTOINCREMENT,
        engagement_id INTEGER,
        service_year TEXT,
        fee_amount TEXT,
        additional_state_fee INTEGER,
        payment_terms TEXT,
        information_deadline TEXT,
        filing_deadline TEXT,
        extension_deadline TEXT,
        include_tax_planning BOOLEAN,
        include_audit_paragraph BOOLEAN,
        included_with_audit BOOLEAN,
        compliance_services TEXT,
        taxpayer_authorization_period TEXT,
        authorized_entities TEXT,
        substantiation_rules TEXT,
        FOREIGN KEY (engagement_id) REFERENCES engagements (engagement_id)
    );
    ''')
    conn.close()

