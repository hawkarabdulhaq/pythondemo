import streamlit as st
import home
import fit  # Place Fit Assessment second for initial self-assessment
import learning_platform  # Combined Learning tab and Testimonials tab
import enrollment  # Updated to reflect "Prices" tab
import certificate  # Import the certificate module
import about  # Import the about module for the About page
import style  # Import the style module to apply global styles

# Apply custom styles from style.py
style.apply_custom_styles()

# Initialize session state for page tracking
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Function to update page state
def set_page(page):
    st.session_state.page = page

# Sidebar Navigation with Logo and Course Title
with st.sidebar:
    # Display the course code image at the top
    st.image("input/code.png", width=200)  # Course code image with 200px width
    
    # Display the main logo image
    st.image("input/logo.jpg", width=200)  # Logo at 200px width for a balanced look
    
    # Navigation buttons
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Fit Assessment", on_click=set_page, args=("Fit Assessment",))  # Fit Assessment for initial assessment
    st.button("Learning", on_click=set_page, args=("Learning",))  # Changed from "Learning Platform" to "Learning"
    st.button("Certificate", on_click=set_page, args=("Certificate",))  # Added Certificate tab
    st.button("Prices", on_click=set_page, args=("Prices",))  # Changed from "Enrollment" to "Prices"
    st.button("About", on_click=set_page, args=("About",))  # Place About as the last navigation option

    # Contact Information with Discord Link
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

# Display the selected page content based on the sidebar navigation
if st.session_state.page == "Home":
    home.show()
elif st.session_state.page == "Fit Assessment":  # Fit Assessment page for initial exploration
    fit.show()
elif st.session_state.page == "Learning":  # Changed from "Learning Platform" to "Learning"
    learning_platform.show()
elif st.session_state.page == "Certificate":  # Certificate page for showcasing course completion
    certificate.show()
elif st.session_state.page == "Prices":  # Changed from "Enrollment" to "Prices"
    enrollment.show()
elif st.session_state.page == "About":  # About as the last option
    about.show()

# Footer for all rights reserved
st.markdown("""
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        All rights reserved to <a href="https://www.habdulhaq.com" target="_blank" style="color: #1ABC9C;">habdulhaq.com</a> © 2024
    </div>
""", unsafe_allow_html=True)
