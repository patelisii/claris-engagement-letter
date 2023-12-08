import os
import json
import openai
from dotenv import load_dotenv
from datetime import datetime
import sqlite3


from retrievers.customer_data_retriever import query_engagement_data
from retrievers.template_retriever import get_sow_temlpate

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.environ.get("OPENAI_KEY")

def generate_letter(letterInfo):

    current_date = datetime.now().date()

    letterInfo['engagement_date'] = current_date
    letterInfo['service_year'] = current_date.year
    
    storedInfo = query_engagement_data(letterInfo["customer_name"], letterInfo["engagement_type"])
    template = get_sow_temlpate(letterInfo["engagement_type"])
    
    prompt = f"""
    Please create an engagement letter provided the following information:
    
    {letterInfo}
    
    {storedInfo}
    
    Fill in this SOW engagement letter template for {letterInfo["engagement_type"]} using the information above. Here is the template:
    
    {template}
    """
    
    response = openai.chat.completions.create(
        model = 'gpt-4-1106-preview',
        messages = [{'role': 'user', 'content': prompt}],
    )


    
    return response.choices[0].message.content

def add_meta_letter_to_db(letterInfo):

    conn = sqlite3.connect('data/engagement_letters_table.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO engagementLettersMeta 
    (EngagementType, Date, SignerName, SignerTitle, PartnerName, PartnerContactNumber, CustomerName, MSADate) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (letterInfo['engagement_type'], letterInfo['date'], 
          letterInfo['signerInfo']['name'], letterInfo['signerInfo']['title'], 
          letterInfo['partnerInfo']['partnerName'], letterInfo['partnerInfo']['partnerContactNumber'],
          letterInfo['customer_name'], letterInfo['msaDate']))


    conn.commit()
    conn.close()


f = open('data/sample_inputs/sample_letter_info.json')
data = json.load(f)
print(data)
print(generate_letter(data))