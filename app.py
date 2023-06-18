import streamlit as st
from utils import (fetch_html, extract_text, extract_json_ld, analyze_text_with_gpt,
                   create_schema_with_gpt, combine_schemas_with_gpt, explain_changes_with_gpt)

st.title("Schema Markup Consultant")

api_key = st.text_input("Enter your GPT-API key:")

url = st.text_input("Enter a URL:")
if url:
    html_content = fetch_html(url)
    text_content = extract_text(html_content)
    st.write("Here is the continuation of the `app.py` file:

```python
    st.write("Here is the extracted text content:")
    st.write(text_content)
    
    schema_properties = analyze_text_with_gpt(api_key, text_content)
    st.write("Here are the identified schema properties:")
    st.write(schema_properties)
    
    new_schema = create_schema_with_gpt(api_key, schema_properties)
    st.write("Here is the new schema markup created:")
    st.write(new_schema)
    
    existing_schema = extract_json_ld(html_content)
    st.write("Here is the existing schema markup found on the page:")
    st.write(existing_schema)
    
    enhanced_schema = combine_schemas_with_gpt(api_key, existing_schema, new_schema)
    st.write("Here is the enhanced schema markup after combining the existing and new schema markups:")
    st.write(enhanced_schema)
    
    explanation = explain_changes_with_gpt(api_key, existing_schema, enhanced_schema)
    st.write("Here is an explanation of the changes and optimizations made:")
    st.write(explanation)
