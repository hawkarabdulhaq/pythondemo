
import streamlit as st
import home
import stepstoexpert
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

def set_page(page):
    """Update the session state's page value."""
    st.session_state.page = page

# Sidebar Navigation
with st.sidebar:
    # Display logo
    st.image("input/logo.jpg", width=200)

    # Navigation buttons (each button sets a different page)
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Steps-to-Expert", on_click=set_page, args=("Steps-to-Expert",))
    st.button("Business Analysis", on_click=set_page, args=("Business",))
    st.button("Solutions", on_click=set_page, args=("Solutions",))
    st.button("About", on_click=set_page, args=("About",))
    st.button("Contact", on_click=set_page, args=("Contact",))

    # Contact Information with email and demo link
    st.markdown(
        """
        <div style="margin-top: 30px; font-size: 1.1em; color: #eeeeee;">
            <p><strong>Contact:</strong></p>
            <p>Email: <a href="mailto:connect@habdulhaq.com" target="_blank" style="color: #1ABC9C;">connect@habdulhaq.com</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Main Page Content
if st.session_state.page == "Home":
    try:
        home.show()
    except AttributeError:
        st.error("Error: The Home page is not defined properly. Please ensure home.py contains a top-level 'show()' function.")
elif st.session_state.page == "steps-to-expert":
    try:
        steps-to-expert.show()
    except AttributeError:
        st.error("Error: The steps-to-expert page is not defined properly. Please ensure steps-to-expert.py contains a top-level 'show()' function.")
elif st.session_state.page == "Business":
    try:
        business.show()
    except AttributeError:
        st.error("Error: The Business page is not defined properly. Please ensure business.py contains a top-level 'show()' function.")
elif st.session_state.page == "Solutions":
    try:
        solutions.show()
    except AttributeError:
        st.error("Error: The Solutions page is not defined properly. Please ensure solutions.py contains a top-level 'show()' function.")
elif st.session_state.page == "About":
    try:
        about.show()
    except AttributeError:
        st.error("Error: The About page is not defined properly. Please ensure about.py contains a top-level 'show()' function.")
elif st.session_state.page == "Contact":
    try:
        contact.show()
    except AttributeError:
        st.error("Error: The Contact page is not defined properly. Please ensure contact.py contains a top-level 'show()' function.")

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        aiforimpact © 2024
    </div>
    """,
    unsafe_allow_html=True,
)
