import streamlit as st
import requests
import streamlit.components.v1 as components

def show():
    # Use the raw URL for the SVG
    svg_url = "https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/aee80693b90c9c75f231d8c331a51f474fa47580/impact_wave.svg"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(svg_url, headers=headers)
    
    # Debug: Show status code to help troubleshoot issues
    st.write("Status Code:", response.status_code)
    
    if response.status_code == 200:
        svg_content = response.text
        # Render the SVG using components.html so that it is interpreted as HTML
        components.html(svg_content, height=500)
    else:
        st.error("Failed to load the impact wave graphic.")

    # Additional content below...
    st.markdown("""
    <div style="text-align: center; font-size: 1.5em; font-weight: bold; color: #eeeeee; margin-bottom: 20px;">
        Optimizing businesses for resilience and sustainable growth with AI!
    </div>
    """, unsafe_allow_html=True)
