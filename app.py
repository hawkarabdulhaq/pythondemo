import streamlit as st
import home
import trainings
import business
import solutions
import about
import contact
import style

# Apply custom styles from style.py
style.apply_custom_styles()

# Initialize session state for page tracking
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Function to update the page state
def set_page(page):
    st.session_state.page = page

# Check if a navigation event has been triggered
if "navigate_to" in st.session_state:
    st.session_state.page = st.session_state.navigate_to
    del st.session_state.navigate_to  # Remove trigger after navigation

# Sidebar Navigation
with st.sidebar:
    # Display logo
    st.image("input/logo.jpg", width=200)

    # Navigation buttons
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Trainings", on_click=set_page, args=("Trainings",))
    st.button("Business Analysis", on_click=set_page, args=("Business",))
    st.button("Solutions", on_click=set_page, args=("Solutions",))
    st.button("About", on_click=set_page, args=("About",))
    st.button("Contact", on_click=set_page, args=("Contact",))

    # Contact Information with email and demo link
    st.markdown(
        """
        <div style="margin-top: 30px; font-size: 1.1em; color: #eeeeee;">
            <p><strong>Contact:</strong></p>
            <p>Email: <a href="mailto:ha@releafs.co" target="_blank" style="color: #1ABC9C;">ha@releafs.co</a></p>
        </div>
        <div style="margin-top: 20px; font-size: 1.1em;">
            <p><strong>Book a Demo:</strong></p>
            <p><a href="https://calendly.com/hawkar_abdulhaq/introduction-to-coding-training-with-hawkar" target="_blank" style="color: #1ABC9C;">Schedule a Demo</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Main Page Content
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
elif st.session_state.page == "Contact":
    contact.show()

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        releafs.co © 2024
    </div>
    """,
    unsafe_allow_html=True,
)
