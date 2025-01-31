import streamlit as st

def show():
    """Redirect to Calendly scheduling page and display email contact."""
    
    # Calendly Scheduling Button
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

    # Additional Email Contact
    st.markdown("""
    <div style="text-align: center; margin-top: 30px; font-size: 1.2em;">
        <p>Or email us directly at:</p>
        <p><a href="mailto:connect@habdulhaq.com" target="_blank" style="color: #129729; text-decoration: none;">
            connect@habdulhaq.com
        </a></p>
    </div>
    """, unsafe_allow_html=True)
