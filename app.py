import streamlit as st
import home
import fit
import learning_platform
import enrollment
import certificate
import about
import style
from dictionary import translations  # Import translations dictionary

# Apply custom styles from style.py
style.apply_custom_styles()

# Initialize session state for page tracking and language
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'language' not in st.session_state:
    st.session_state.language = "EN"  # Default language is English

# Function to update page state
def set_page(page):
    st.session_state.page = page

# Function to update language state
def set_language(lang):
    st.session_state.language = lang

# Function to get translated text
def translate(key):
    return translations.get(key, {}).get(st.session_state.language, key)

# Sidebar Navigation with Logo, Course Title, and Language Options
with st.sidebar:
    # Language options at the top
    lang_col1, lang_col2 = st.columns(2)
    with lang_col1:
        st.button("EN", on_click=set_language, args=("EN",))
    with lang_col2:
        st.button("KU", on_click=set_language, args=("KU",))
    
    # Display the course code image at the top
    st.image("input/code.png", width=200)
    
    # Display the main logo image
    st.image("input/logo.jpg", width=200)
    
    # Navigation buttons
    st.button(translate("home_title"), on_click=set_page, args=("Home",))
    st.button(translate("fit_assessment_title"), on_click=set_page, args=("Fit Assessment",))
    st.button(translate("learning_title"), on_click=set_page, args=("Learning",))
    st.button(translate("certificate_title"), on_click=set_page, args=("Certificate",))
    st.button(translate("prices_title"), on_click=set_page, args=("Prices",))
    st.button(translate("about_title"), on_click=set_page, args=("About",))

    # Contact Information with Discord Link
    st.markdown(f"""
        <div style="margin-top: 30px; font-size: 1.1em; color: #2C3E50;">
            <p><strong>{translate("contact")}:</strong></p>
            <p>{translate("email")}: <a href="mailto:connect@habdulhaq.com" target="_blank" style="color: #1ABC9C;">connect@habdulhaq.com</a></p>
            <p>{translate("website")}: <a href="https://www.habdulhaq.com" target="_blank" style="color: #1ABC9C;">www.habdulhaq.com</a></p>
            <p>{translate("discord")}: <a href="https://discord.gg/wcypuxhF" target="_blank" style="color: #1ABC9C;">{translate("discord")}</a></p>
        </div>
        <div style="margin-top: 20px; font-size: 1.1em;">
            <p><strong>{translate("book_demo")}:</strong></p>
            <p><a href="https://calendly.com/hawkar_abdulhaq/introduction-to-coding-training-with-hawkar" target="_blank" style="color: #1ABC9C;">{translate("schedule_demo")}</a></p>
        </div>
    """, unsafe_allow_html=True)

# Display the selected page content based on the sidebar navigation
if st.session_state.page == "Home":
    home.show()
elif st.session_state.page == "Fit Assessment":
    fit.show()
elif st.session_state.page == "Learning":
    learning_platform.show()
elif st.session_state.page == "Certificate":
    certificate.show()
elif st.session_state.page == "Prices":
    enrollment.show()
elif st.session_state.page == "About":
    about.show()

# Footer
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        {translate("footer")} <a href="https://www.habdulhaq.com" target="_blank" style="color: #1ABC9C;">habdulhaq.com</a> © 2024
    </div>
""", unsafe_allow_html=True)
