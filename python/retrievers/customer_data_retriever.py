import sqlite3

def get_client_info(customer_name):
    """
    Queries the database for a customer by name and returns their information in a dictionary format.

    :param customer_name: Name of the customer to query.
    :return: Dictionary containing the client's information.
    """
    # Re-establish connection to the SQLite database
    conn = sqlite3.connect('data/SOW_engagement_letters.db')
    cursor = conn.cursor()

    # Query the database for the customer
    cursor.execute("SELECT * FROM customers WHERE Name = ?", (customer_name,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Check if the customer is found
    if result:
        # Extracting address components
        address_components = result[2].split('\n')
        address_line = address_components[0]
        city_state_zip = address_components[1].split(',')
        city = city_state_zip[0].strip()
        state_zip = city_state_zip[1].strip().split(' ')
        state = state_zip[0]
        zip_code = state_zip[1] if len(state_zip) > 1 else ""

        # Creating the dictionary with client information
        client_info = {
            "clientInfo": {
                "clientName": result[1],
                "address": address_line,
                "city": city,
                "state": state,
                "zip": zip_code
            }
        }
        return client_info
    else:
        return {"error": "Customer not found."}


import sqlite3


# Function to query data based on customer name and engagement type
def query_engagement_data(customer_name, engagement_type):
    
    # Connect to SQLite database
    conn = sqlite3.connect('data/SOW_engagement_letters.db')  # Replace with your database file

    cursor = conn.cursor()

    # SQL query to fetch the required data
    if engagement_type == "Tax Consulting SOW":
        query = '''
        SELECT 
            c.customer_name, 
            se.engagement_type, 
            se.date AS engagement_date,
            mse.date AS msa_date,
            se.partner_name, 
            se.partner_contact_number,
            cd.service_year AS consulting_service_year,
            cd.consulting_fee_amount,
            cd.payment_terms AS consulting_payment_terms,
            cd.information_deadline AS consulting_information_deadline,
            cd.completion_date AS consulting_completion_date,
            cd.consulting_services
        FROM 
            customers c
        JOIN 
            sow_engagements se ON c.customer_id = se.customer_id
        JOIN
            msa_engagements mse ON c.customer_id = mse.customer_id
        LEFT JOIN 
            consulting_details cd ON se.engagement_id = cd.engagement_id
        WHERE 
            c.customer_name = ? AND se.engagement_type = ?
        ORDER BY 
            se.date DESC
        LIMIT 1
        '''
    else:  # Assuming engagement_type is "Tax Compliance SOW"
        query = '''
        SELECT 
            c.customer_name, 
            se.engagement_type, 
            se.date AS engagement_date,
            mse.date AS msa_date,
            se.partner_name, 
            se.partner_contact_number,
            cpd.service_year AS compliance_service_year,
            cpd.fee_amount AS compliance_fee_amount,
            cpd.additional_state_fee,
            cpd.payment_terms AS compliance_payment_terms,
            cpd.extension_deadline,
            cpd.include_tax_planning,
            cpd.include_audit_paragraph,
            cpd.included_with_audit,
            cpd.compliance_services,
            cpd.taxpayer_authorization_period,
            cpd.substantiation_rules
        FROM 
            customers c
        JOIN 
            sow_engagements se ON c.customer_id = se.customer_id
        JOIN
            msa_engagements mse ON c.customer_id = mse.customer_id
        LEFT JOIN 
            compliance_details cpd ON se.engagement_id = cpd.engagement_id
        WHERE 
            c.customer_name = ? AND se.engagement_type = ?
        ORDER BY 
            se.date DESC
        LIMIT 1
        '''
    
    # Execute the query
    cursor.execute(query, (customer_name, engagement_type))

    # Fetch all the rows
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    # Convert rows to dictionaries
    result = [dict(zip(columns, row)) for row in rows]

    # Close the cursor
    cursor.close()
    conn.close()

    return result

# Example usage
# customer_name = "Beta Ltd."  # Replace with the desired customer name
# engagement_type = "Tax Compliance SOW"  # Replace with the desired engagement type
# data = query_engagement_data(customer_name, engagement_type)

# print(data)

