import streamlit as st
import home
import testimony
import learning_platform
import enrollment
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
    # Display the logo image with a specified width
    st.image("input/logo.jpg", width=200)  # Set the width to 150 pixels (adjust as needed)
    
    # Course title
    st.title("Personalized Python Training")
    
    # Navigation buttons
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Testimonials", on_click=set_page, args=("Testimonials",))
    st.button("Learning Platform", on_click=set_page, args=("Learning Platform",))
    st.button("Enrollment", on_click=set_page, args=("Enrollment",))

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

# Display the selected page content
if st.session_state.page == "Home":
    home.show()
elif st.session_state.page == "Testimonials":
    testimony.show()
elif st.session_state.page == "Learning Platform":
    learning_platform.show()
elif st.session_state.page == "Enrollment":
    enrollment.show()
