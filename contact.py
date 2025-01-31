import streamlit as st

def show():
    """Redirect to Calendly scheduling page."""
    st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://calendly.com/hawkar_abdulhaq/ai-for-impact" target="_blank" style="
            background-color: #129729; 
            color: white; 
            padding: 15px 25px; 
            text-decoration: none; 
            border-radius: 5px; 
            font-size: 1.2em;">
            Schedule a Meeting
        </a>
    </div>
    """, unsafe_allow_html=True)
