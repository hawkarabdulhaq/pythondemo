# theme.py
import streamlit as st

def apply_dark_theme():
    st.markdown(
        """
        <style>
            /* Set overall background and text colors */
            body {
                background-color: #121212;
                color: #e0e0e0;
            }

            /* Style the main block container */
            .block-container {
                background-color: #121212;
                color: #e0e0e0;
            }

            /* Customize buttons */
            .stButton>button {
                background-color: #333333;
                color: #e0e0e0;
                border: none;
            }
            .stButton>button:hover {
                background-color: #444444;
            }

            /* Optional: Hide Streamlit header for a cleaner look */
            header {
                visibility: hidden;
                height: 0;
            }

            /* Optional: Adjust sidebar styles */
            .css-1d391kg {  /* You may need to adjust this class based on your Streamlit version */
                background-color: #1e1e1e;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
