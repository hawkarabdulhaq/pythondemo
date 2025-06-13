import streamlit as st
import home
import trainings
import prices
import gallery
import certificate
import about
import contact
import style

# ADD ▼
import participants   # ← make sure participants.py sits next to app.py
# END ADD ▲

# ───────── Page-wide config ─────────
st.set_page_config(
    page_title="AI for Impact",
    page_icon="input/logo_improved.png",
)
style.apply_custom_styles()

# ───────── Session-state helper ─────
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

def set_page(page: str):
    st.session_state["page"] = page

# ───────── Sidebar navigation ───────
with st.sidebar:
    st.image("input/logo_improved.png", width=200)

    st.button("Home",        on_click=set_page, args=("Home",))
    st.button("Trainings",   on_click=set_page, args=("Trainings",))
    st.button("Pricing",     on_click=set_page, args=("Pricing",))
    st.button("Gallery",     on_click=set_page, args=("Gallery",))
    st.button("Certificate", on_click=set_page, args=("Certificate",))
    st.button("About",       on_click=set_page, args=("About",))
    st.button("Contact",     on_click=set_page, args=("Contact",))
    # ADD ▼
    st.button("Participants", on_click=set_page, args=("Participants",))
    # END ADD ▲

    st.markdown(
        """
        <div style="margin-top: 30px; font-size: 1.1em; color: #eeeeee;">
            <p><strong>Contact:</strong></p>
            <p>Email: <a href="mailto:connect@aiforimpact.net"
                         target="_blank"
                         style="color: #1ABC9C;">connect@aiforimpact.net</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ───────── Main router ──────────────
page = st.session_state.get("page", "Home")

try:
    if page == "Home":
        home.show()
    elif page == "Trainings":
        trainings.show_trainings()
    elif page == "Pricing":
        prices.show()
    elif page == "Gallery":
        gallery.show()
    elif page == "Certificate":
        certificate.show()
    elif page == "About":
        about.show()
    elif page == "Contact":
        contact.show()
    # ADD ▼
    elif page == "Participants":
        participants.show()
    # END ADD ▲
except AttributeError:
    st.error(f"Error: the {page} page is not defined properly.")

# ───────── Footer ───────────────────
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        aiforimpact © 2024<br>
        Powered by Climate Resilience Fundraising Platform B.V.
    </div>
    """,
    unsafe_allow_html=True,
)
