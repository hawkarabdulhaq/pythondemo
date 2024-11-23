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
    return translations.get(key, {}).get(st.session_state.language, key).strip()  # Remove extra spaces

# Sidebar Navigation
with st.sidebar:
    # Sidebar header
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="input/logo.jpg" alt="Logo" style="width: 150px; border-radius: 50%;">
            <h2 style="margin-top: 10px; color: #2C3E50;">{translate("learning_platform_title")}</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Language selection
    st.radio(
        translate("select_language"),
        options=["EN", "KU"],
        index=0 if st.session_state.language == "EN" else 1,
        on_change=set_language,
        horizontal=True,
        key="lang_select"
    )
    
    st.markdown("---")  # Divider

    # Navigation buttons with icons
    st.markdown(f"""
        <div style="margin-top: 20px;">
            <button onclick="set_page('Home')">🏠 {translate("home_title")}</button><br>
            <button onclick="set_page('Fit Assessment')">📊 {translate("fit_assessment_title")}</button><br>
            <button onclick="set_page('Learning')">📘 {translate("learning_title")}</button><br>
            <button onclick="set_page('Certificate')">📜 {translate("certificate_title")}</button><br>
            <button onclick="set_page('Prices')">💵 {translate("prices_title")}</button><br>
            <button onclick="set_page('About')">ℹ️ {translate("about_title")}</button>
        </div>
    """, unsafe_allow_html=True)

    # Contact Section
    st.markdown("---")  # Divider
    st.markdown(f"""
        <div style="margin-top: 30px; font-size: 1em; color: #2C3E50;">
            <p><strong>{translate("contact")}:</strong></p>
            <p>📧 {translate("email")}: <a href="mailto:connect@habdulhaq.com" target="_blank" style="color: #1ABC9C;">connect@habdulhaq.com</a></p>
            <p>🌐 {translate("website")}: <a href="https://www.habdulhaq.com" target="_blank" style="color: #1ABC9C;">www.habdulhaq.com</a></p>
            <p>💬 {translate("discord")}: <a href="https://discord.gg/wcypuxhF" target="_blank" style="color: #1ABC9C;">{translate("discord")}</a></p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")  # Divider
    st.markdown(f"""
        <div style="margin-top: 10px; text-align: center; font-size: 1em;">
            <a href="https://calendly.com/hawkar_abdulhaq/introduction-to-coding-training-with-hawkar" target="_blank" style="color: #1ABC9C; font-weight: bold;">📅 {translate("schedule_demo")}</a>
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
    <hr style="margin-top: 50px; border: 1px solid #ccc;">
    <div style="text-align: center; margin-top: 10px; font-size: 0.9em; color: #7F8C8D;">
        {translate("footer")} <a href="https://www.habdulhaq.com" target="_blank" style="color: #1ABC9C;">habdulhaq.com</a> © 2024
    </div>
""", unsafe_allow_html=True)
