import requests
import json

f = open('data/sample_inputs/complete_example.json')
data = json.load(f)

response = requests.post('https://diligencedemo.azurewebsites.net/createEngageLetter', json=data)

print(response.status_code)

print(response.json())