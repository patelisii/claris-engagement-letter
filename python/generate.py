import os
import json
import openai
from dotenv import load_dotenv

from retrievers.customer_data_retriever import get_client_info
from retrievers.template_retriever import get_sow_temlpate

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.environ.get("OPENAI_KEY")

def generate_letter(letterInfo):
    customerInfo = get_client_info(letterInfo["customer_name"])
    template = get_sow_temlpate(letterInfo["engagement_type"])
    
    prompt = f"""
    Please create an engagement letter provided the following information:
    
    {letterInfo}
    
    Here is the client's information:
    
    {customerInfo}
    
    Fill in this SOW engagement letter template for {letterInfo["engagement_type"]} using the information above. Here is the template:
    
    {template}
    """
    
    response = openai.chat.completions.create(
        model = 'gpt-4-1106-preview',
        messages = [{'role': 'user', 'content': prompt}],
    )
    
    return response.choices[0].message.content


f = open('data/sample_input.json')
data = json.load(f)
print(generate_letter(data))