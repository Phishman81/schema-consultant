import streamlit as st
from utils import fetch_html, extract_text, extract_json_ld, analyze_text_with_gpt, enhance_schema

def app():
    st.title("Schema Markup Consultant")

    st.write("Please enter your OpenAI GPT API key:")
    openai_api_key = st.text_input('', type='password')

    st.write("Please enter the URL you'd like to analyze:")
    url = st.text_input('')

    if st.button("Analyze URL"):
        html_content = fetch_html(url)
        text_content = extract_text(html_content)
        st.write("Text content from the URL:")
        st.write(text_content)
        
        st.write("Now looking for JSON-LD schema markup...")
        if st.button("Find Schema Markup"):
            json_ld_data = extract_json_ld(html_content)
            st.write("Current schema markup found on the URL:")
            st.write(json_ld_data)
            
            new_properties = analyze_text_with_gpt(text_content, openai_api_key)
            st.write("Potential new properties from the text content:")
            st.write(new_properties)

            enhanced_schema = enhance_schema(json_ld_data, new_properties)
            st.write("Enhanced schema markup:")
            st.write(enhanced_schema)

if __name__ == "__main__":
    app()

