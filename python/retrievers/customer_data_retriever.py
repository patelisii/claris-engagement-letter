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
