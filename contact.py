import streamlit as st
from streamlit.components.v1 import html

def show():
    """Display the embedded Calendly widget using an iframe."""
    calendly_embed = """
    <iframe 
        src="https://calendly.com/hawkar_abdulhaq/ai-for-impact?embed=true&background_color=373737&text_color=fcf8f8&primary_color=129729"
        width="100%" 
        height="700" 
        frameborder="0"
    ></iframe>
    """
    html(calendly_embed, height=700)
