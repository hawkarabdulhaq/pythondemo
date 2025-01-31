import streamlit as st
from streamlit.components.v1 import html

def show():
    """Display the full Calendly widget with proper sizing"""
    calendly_html = """
    <style>
        #calendly-container {
            height: 100vh !important;
            min-height: 2500px;
            width: 100%;
        }
    </style>
    
    <div id="calendly-container">
        <iframe
            src="https://calendly.com/hawkar_abdulhaq/ai-for-impact?embed=true&background_color=373737&text_color=fcf8f8&primary_color=129729"
            width="100%"
            height="250%"
            frameborder="0"
        ></iframe>
    </div>
    """
    
    html(calendly_html, height=700)
