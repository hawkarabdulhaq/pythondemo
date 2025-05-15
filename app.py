

import streamlit as st
import home
import trainings
import prices
import gallery          # NEW ⬅️  (make sure gallery.py exists)
import certificate
import about
import contact
import style

# ─────────────────────────── Page-wide config ───────────────────────────
st.set_page_config(
    page_title="AI for Impact",
    page_icon="input/logo_improved.png",
)
style.apply_custom_styles()

# ─────────────────────────── Session-state helper ───────────────────────
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

def set_page(page: str):
    st.session_state["page"] = page

# ─────────────────────────── Sidebar navigation ─────────────────────────
with st.sidebar:
    st.image("input/logo_improved.png", width=200)

    st.button("Home",        on_click=set_page, args=("Home",))
    st.button("Trainings",   on_click=set_page, args=("Trainings",))
    st.button("Pricing",     on_click=set_page, args=("Pricing",))
    st.button("Gallery",     on_click=set_page, args=("Gallery",))   # NEW ⬅️
    st.button("Certificate", on_click=set_page, args=("Certificate",))
    st.button("About",       on_click=set_page, args=("About",))
    st.button("Contact",     on_click=set_page, args=("Contact",))

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

# ─────────────────────────── Main router ────────────────────────────────
page = st.session_state.get("page", "Home")

try:
    if page == "Home":
        home.show()

    elif page == "Trainings":
        trainings.show_trainings()

    elif page == "Pricing":
        prices.show()

    elif page == "Gallery":               # NEW ⬅️
        gallery.show()                    # gallery.py must define show()

    elif page == "Certificate":
        certificate.show()

    elif page == "About":
        about.show()

    elif page == "Contact":
        contact.show()

except AttributeError:
    st.error(f"Error: the {page} page is not defined properly.")

# ─────────────────────────── Footer ─────────────────────────────────────
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        aiforimpact © 2024<br>
        Powered by Climate Resilience Fundraising Platform B.V.
    </div>
    """,
    unsafe_allow_html=True,
)
