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

# 1) Ensure page is in session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# 2) Check if ?page= is present in query_params
params = st.query_params
if "page" in params:
    st.session_state.page = params["page"]

# 3) Define a helper to set session_state + update query params
def set_page(page):
    st.session_state.page = page
    st.query_params = {"page": page}  # this updates the URL to ?page=...

# ---- SIDEBAR ----
with st.sidebar:
    st.image("input/logo.jpg", width=200)

    # Buttons that change session state AND query params
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Trainings", on_click=set_page, args=("Trainings",))
    st.button("Business Analysis", on_click=set_page, args=("Business",))
    st.button("Solutions", on_click=set_page, args=("Solutions",))
    st.button("About", on_click=set_page, args=("About",))
    st.button("Contact", on_click=set_page, args=("Contact",))

    # Contact & Demo Info
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

# ---- MAIN PAGE CONTENT ----
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

# ---- FOOTER ----
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        releafs.co © 2024
    </div>
    """,
    unsafe_allow_html=True,
)
