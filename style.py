import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    /* Set the default font to Courier */
    * {
        font-family: "Courier", monospace;
    }
    
    /* Styling the title */
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #2C3E50;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    /* Styling for section titles */
    .section-title {
        font-size: 1.7em;
        font-weight: bold;
        color: #34495E;
        margin-top: 30px;
        margin-bottom: 10px;
        border-bottom: 2px solid #34495E;
        padding-bottom: 5px;
    }
    
    /* General content styling */
    .content {
        font-size: 1.1em;
        color: #2C3E50;
        line-height: 1.6;
        text-align: justify;
        margin-bottom: 20px;
    }

    /* Highlighting important sections */
    .highlight {
        font-weight: bold;
        color: #1ABC9C;
    }
    
    /* Style for video container */
    .video-container {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
