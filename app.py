import streamlit as st
import home
import fit
import learning_platform
import enrollment
import certificate
import about
import style

# Apply custom styles from style.py
style.apply_custom_styles()

# Initialize session state for page tracking and language
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'language' not in st.session_state:
    st.session_state.language = "EN"  # Default to English

# Function to update page state
def set_page(page):
    st.session_state.page = page

# Function to toggle language
def toggle_language(lang):
    st.session_state.language = lang

# Sidebar Navigation with Language Toggle
with st.sidebar:
    # Language selection at the top
    st.markdown("<h4 style='text-align: center;'>🌍 Language</h4>", unsafe_allow_html=True)
    lang_col1, lang_col2 = st.columns(2)
    with lang_col1:
        st.button("EN", on_click=toggle_language, args=("EN",))  # English button
    with lang_col2:
        st.button("KU", on_click=toggle_language, args=("KU",))  # Kurdish button

    # Display the course code image at the top
    st.image("input/code.png", width=200)
    
    # Display the main logo image
    st.image("input/logo.jpg", width=200)

    # Navigation buttons
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Fit Assessment", on_click=set_page, args=("Fit Assessment",))
    st.button("Learning", on_click=set_page, args=("Learning",))
    st.button("Certificate", on_click=set_page, args=("Certificate",))
    st.button("Prices", on_click=set_page, args=("Prices",))
    st.button("About", on_click=set_page, args=("About",))

    # Contact Information
    st.markdown("""
        <div style="margin-top: 30px; font-size: 1.1em; color: #2C3E50;">
            <p><strong>Contact:</strong></p>
            <p>Email: <a href="mailto:connect@habdulhaq.com" target="_blank" style="color: #1ABC9C;">connect@habdulhaq.com</a></p>
            <p>Website: <a href="https://www.habdulhaq.com" target="_blank" style="color: #1ABC9C;">www.habdulhaq.com</a></p>
            <p>Discord Server: <a href="https://discord.gg/wcypuxhF" target="_blank" style="color: #1ABC9C;">Join us on Discord</a></p>
        </div>
        <div style="margin-top: 20px; font-size: 1.1em;">
            <p><strong>Book a Free Demo Session:</strong></p>
            <p><a href="https://calendly.com/hawkar_abdulhaq/introduction-to-coding-training-with-hawkar" target="_blank" style="color: #1ABC9C;">Schedule a Demo on Calendly</a></p>
        </div>
    """, unsafe_allow_html=True)

# Load the appropriate content based on the language
language = st.session_state.language

# Display the selected page content
if st.session_state.page == "Home":
    home.show(language)
elif st.session_state.page == "Fit Assessment":
    fit.show(language)
elif st.session_state.page == "Learning":
    learning_platform.show(language)
elif st.session_state.page == "Certificate":
    certificate.show(language)
elif st.session_state.page == "Prices":
    enrollment.show(language)
elif st.session_state.page == "About":
    about.show(language)

# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        All rights reserved to <a href="https://www.habdulhaq.com" target="_blank" style="color: #1ABC9C;">habdulhaq.com</a> © 2024
    </div>
""", unsafe_allow_html=True)
