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
    
    Fill in this SOW engagement letter template for tax consulting using the information in the JSON above. Here is the template:
    
    {template}
    """
    
    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo-16k',
        messages = [{'role': 'user', 'content': prompt}],
    )
    
    return response


f = open('data/sample_input.json')
data = json.load(f)