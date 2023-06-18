import streamlit as st
from utils import fetch_html, extract_text, extract_json_ld, analyze_text_with_gpt, enhance_schema
import logging

logging.basicConfig(level=logging.INFO)

def app():
    st.title("Schema Markup Consultant")

    api_key = st.text_input("Enter your GPT API key")

    url = st.text_input("Enter a URL")
    if url:
        try:
            html = fetch_html(url)
            text = extract_text(html)
            st.text(text)

            st.text("Now looking for JSON-LD schema markup.")
            try:
                json_ld = extract_json_ld(html)
                st.markdown("**Found schema markup:**")
                st.json(json_ld)
            except Exception as e:
                logging.error(f"Exception occurred while finding schema markup: {e}")
                st.error(f"An error occurred: {e}")

            st.text("Now analyzing text content to identify possible schema properties.")
            try:
                gpt_response = analyze_text_with_gpt(api_key, text)
                st.text(gpt_response)
            except Exception as e:
                logging.error(f"Exception occurred while analyzing text: {e}")
                st.error(f"An error occurred: {e}")

            st.text("Now trying to combine the current schema markup with the new findings.")
            try:
                enhanced_json_ld = enhance_schema(json_ld, gpt_response)
                st.json(enhanced_json_ld)
            except Exception as e:
                logging.error(f"Exception occurred while enhancing schema: {e}")
                st.error(f"An error occurred: {e}")

        except Exception as e:
            logging.error(f"Exception occurred while processing URL: {e}")
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    app()
