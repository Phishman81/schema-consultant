import requests
from bs4 import BeautifulSoup
import json
import openai

def fetch_html(url):
    response = requests.get(url)
    return response.text

def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text

def extract_json_ld(html):
    soup = BeautifulSoup(html, 'html.parser')
    json_ld = [json.loads(script.string) for script in soup.find_all('script', {'type':'application/ld+json'})]
    return json_ld

def analyze_text_with_gpt(api_key, text):
    # Set the OpenAI API key
    openai.api_key = api_key

    # Set the system message
    system_msg = 'You are an assistant that understands language and data.'

    # Set the user message
    user_msg = text

    # Create a request to the GPT API
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ]
    )

    # Extract the content from the response
    content = response["choices"][0]["message"]["content"]
    return content

def enhance_schema(json_ld, gpt_response):
    # For now, we're simply adding the GPT response as a potential enhancement.
    # In a real-world scenario, this would involve parsing the GPT response and adding relevant information to the schema.
    for schema in json_ld:
        schema['gpt_enhancement'] = gpt_response
    return json_ld
