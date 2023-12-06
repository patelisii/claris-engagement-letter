
import sqlite3



# Re-establish connection to the SQLite database
conn = sqlite3.connect('data/engagement_letters_table.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS engagementLettersMeta (
        EngagementLetterID INTEGER PRIMARY KEY,
        EngagementType TEXT,
        DATE DATE,
        SignerName TEXT,
        SignerTitle TEXT,
        PartnerName TEXT,
        PartnerContactNumber INT,
        CustomerName TEXT,
        MSADate DATE,
        FeeAmount INT
    )
''')

# Close the connection
conn.close()