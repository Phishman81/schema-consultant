import requests
import openai
from bs4 import BeautifulSoup
from extruct.jsonld import JsonLdExtractor

def fetch_html(url):
    response = requests.get(url)
    return response.text

def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    return text

def extract_json_ld(html_content):
    extractor = JsonLdExtractor()
    data = extractor.extract(html_content)
    return data

def analyze_text_with_gpt(api_key, text):
    openai.api_key = api_key
    system_msg = 'You are a helpful assistant who understands schema markup and SEO.'
    user_msg = f'Please analyze the following text and suggest possible schema properties: {text}'

    response = openai.ChatCompletion.create(model="gpt-4-0613",
                                            messages=[{"role": "system", "content": system_msg},
                                                      {"role": "user", "content": user_msg}])
    return response["choices"][0]["message"]["content"]

def create_schema_with_gpt(api_key, properties):
    openai.api_key = api_key
    system_msg = 'You are a knowledgeable assistant capable of creating schema markup.'
    user_msg = f'Please create a schema markup with the following properties: {properties}'

    response = openai.ChatCompletion.create(model="gpt-4-0613",
                                            messages=[{"role": "system", "content": system_msg},
                                                      {"role": "user", "content": user_msg}])
    return response["choices"][0]["message"]["content"]

def combine_schemas_with_gpt(api_key, existing_schema, new_schema):
    openai.api_key = api_key
    system_msg = 'You are an assistant skilled in combining and optimizing schema markups.'
    user_msg = f'Please combine the following schema markups and optimize them: {existing_schema}, {new_schema}'

    response = openai.ChatCompletion.create(model="gpt-4-0613",
                                            messages=[{"role": "system", "content": system_msg},
                                                      {"role": "user", "content": user_msg}])
    return response["choices"][0]["message"]["content"]

def explain_changes_with_gpt(api_key, original_schema, enhanced_schema):
    openai.api_key = api_key
    system_msg = 'You are an assistant capable of explaining changes in schema markups.'
    user_msg = f'Please explain the changes between the original schema {original_schema} and the enhanced schema {enhanced_schema}'

    response = openai.ChatCompletion.create(model="gpt-4-0613",
                                            messages=[{"role": "system", "content": system_msg},
                                                      {"role": "user", "content": user_msg}])
    return response["choices"][0]["message"]["content"]
