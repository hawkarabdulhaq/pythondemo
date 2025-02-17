import streamlit as st
import home
import stepstoexpert  # Notice the module name is stepstoexpert (no hyphens)
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

    # Notice we use the same exact string ("Steps-to-Expert") in the button and the check
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Steps-to-Expert", on_click=set_page, args=("Steps-to-Expert",))
    st.button("Steps-to-Impact", on_click=set_page, args=("Steps-to-Impact",))
    st.button("Steps-to-Solutions", on_click=set_page, args=("Steps-to-Solutions",))
    st.button("About", on_click=set_page, args=("About",))
    st.button("Contact", on_click=set_page, args=("Contact",))

    # Contact Information
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
        st.error("Error: The Home page is not defined properly.")
elif st.session_state.page == "Steps-to-Expert":
    try:
        # Must call stepstoexpert.show(), not steps-to-expert.show()
        stepstoexpert.show()
    except AttributeError:
        st.error("Error: The Steps-to-Expert page is not defined properly.")
elif st.session_state.page == "Steps-to-Impact":
    try:
        business.show()
    except AttributeError:
        st.error("Error: The Business page is not defined properly.")
elif st.session_state.page == "Steps-to-Solutions":
    try:
        solutions.show()
    except AttributeError:
        st.error("Error: The Solutions page is not defined properly.")
elif st.session_state.page == "About":
    try:
        about.show()
    except AttributeError:
        st.error("Error: The About page is not defined properly.")
elif st.session_state.page == "Contact":
    try:
        contact.show()
    except AttributeError:
        st.error("Error: The Contact page is not defined properly.")

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        aiforimpact © 2024
    </div>
    """,
    unsafe_allow_html=True,
)
