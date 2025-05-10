import streamlit as st
import home
import trainings  # Replaces stepstoexpert
import prices
import certificate
import about
import contact
import style

# Set the title and icon for the browser tab
st.set_page_config(page_title="AI for Impact", page_icon="📊")

# Apply custom styles from style.py
style.apply_custom_styles()

# Initialize session state for page tracking
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

def set_page(page):
    """Update the session state's page value."""
    st.session_state["page"] = page

# Sidebar Navigation
with st.sidebar:
    # Display logo
    st.image("input/logo.jpg", width=200)

    # Navigation buttons
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Trainings", on_click=set_page, args=("Trainings",))  # Renamed label
    st.button("Pricing", on_click=set_page, args=("Pricing",))
    st.button("Certificate", on_click=set_page, args=("Certificate",))
    st.button("About", on_click=set_page, args=("About",))
    st.button("Contact", on_click=set_page, args=("Contact",))

    # Contact Information
    st.markdown(
        """
        <div style="margin-top: 30px; font-size: 1.1em; color: #eeeeee;">
            <p><strong>Contact:</strong></p>
            <p>Email: <a href="mailto:connect@aiforimpact.net" target="_blank" style="color: #1ABC9C;">connect@aiforimpact.net</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Main Page Content
page = st.session_state.get("page", "Home")

if page == "Home":
    try:
        home.show()
    except AttributeError:
        st.error("Error: The Home page is not defined properly.")
elif page == "Trainings":
    try:
        ourtrainings.show()
    except AttributeError:
        st.error("Error: The Trainings page is not defined properly.")
elif page == "Pricing":
    try:
        prices.show()
    except AttributeError:
        st.error("Error: The Pricing page is not defined properly.")
elif page == "Certificate":
    try:
        certificate.show()
    except AttributeError:
        st.error("Error: The Certificate page is not defined properly.")
elif page == "About":
    try:
        about.show()
    except AttributeError:
        st.error("Error: The About page is not defined properly.")
elif page == "Contact":
    try:
        contact.show()
    except AttributeError:
        st.error("Error: The Contact page is not defined properly.")

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        aiforimpact © 2024<br>
        Powered by Climate Resilience Fundraising Platform B.V.
    </div>
    """,
    unsafe_allow_html=True,
)
