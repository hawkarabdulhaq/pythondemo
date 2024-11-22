import streamlit as st
from dictionary import translate  # Import the centralized translate function

def show():
    # Ensure session_state.language is available
    if "language" not in st.session_state:
        st.session_state.language = "EN"  # Default to English if not set

    language = st.session_state.language  # Retrieve the selected language

    # Title
    st.markdown(f"### {translate('discount_title', language)}")
    
    # Description and Discount Details
    st.markdown(f"""
        {translate('discount_description', language)}
        
        - **{translate('friend_referral_title', language)}**: {translate('friend_referral_description', language)}
        - **{translate('refer_three_title', language)}**: {translate('refer_three_description', language)}
        - **{translate('student_discount_title', language)}**: {translate('student_discount_description', language)}
    """)

    # Contact Information
    st.markdown(f"""
        {translate('discount_contact', language)}
    """)

# Remove the direct call to show()
# The show() function should only be called explicitly from app.py
