import streamlit as st
import home
import trainings
import business  # Import Business Analysis module
import solutions  # Import Solutions module
import about
import style

# Function to toggle the theme
def toggle_theme():
    current_theme = st.session_state.get("theme", "light")
    new_theme = "dark" if current_theme == "light" else "light"
    st.session_state.theme = new_theme
    st.query_params["theme"] = new_theme  # Updated function

# Initialize session state for theme
if "theme" not in st.session_state:
    # Get the theme from query parameters (if available)
    query_params = st.query_params
    theme = query_params.get("theme", ["light"])[0]
    st.session_state.theme = theme

# Set the page config (without theme argument)
st.set_page_config(page_title="My App", page_icon="🌙", layout="wide", initial_sidebar_state="expanded")

# Apply custom styles from style.py
style.apply_custom_styles()

# Initialize session state for page tracking
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Function to update page state
def set_page(page):
    st.session_state.page = page

# Sidebar Navigation with Logo, Course Title, and Options
with st.sidebar:
    st.image("input/code.png", width=200)
    st.image("input/logo.jpg", width=200)
    
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Trainings", on_click=set_page, args=("Trainings",))  
    st.button("Business Analysis", on_click=set_page, args=("Business",))  
    st.button("Solutions", on_click=set_page, args=("Solutions",))  
    st.button("About", on_click=set_page, args=("About",))  

    # Theme toggle button
    st.button("Toggle Theme", on_click=toggle_theme)

    # Contact Information
    st.markdown("""
        <div style="margin-top: 30px; font-size: 1.1em; color: #2C3E50;">
            <p><strong>Contact:</strong></p>
            <p>Email: <a href="mailto:connect@habdulhaq.com" target="_blank" style="color: #1ABC9C;">connect@habdulhaq.com</a></p>
            <p>Website: <a href="https://www.habdulhaq.com" target="_blank" style="color: #1ABC9C;">www.habdulhaq.com</a></p>
            <p>Discord: <a href="https://discord.gg/wcypuxhF" target="_blank" style="color: #1ABC9C;">Join Discord</a></p>
        </div>
        <div style="margin-top: 20px; font-size: 1.1em;">
            <p><strong>Book a Demo:</strong></p>
            <p><a href="https://calendly.com/hawkar_abdulhaq/introduction-to-coding-training-with-hawkar" target="_blank" style="color: #1ABC9C;">Schedule a Demo</a></p>
        </div>
    """, unsafe_allow_html=True)

# Display the selected page content
if st.session_state.page == "Home":
    home.show()
elif st.session_state.page == "Trainings":
    trainings.show()
elif st.session_state.page == "Business":
    business.show()
elif st.session_state.page == "Solutions":
    solutions.show()
elif st.session_state.page == "About":
    about.show()

# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        habdulhaq.com © 2024
    </div>
""", unsafe_allow_html=True)
