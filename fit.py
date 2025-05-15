# gallery.py  –  Student Showcase
# -------------------------------------------------------------
# Dark-theme gallery that highlights real apps built during (or
# for) your courses.  Add or edit entries in the APPS list and
# the page updates automatically.

import streamlit as st

# ───────────────────────── Page config ─────────────────────────
st.set_page_config(page_title="Gallery • Student Showcase",
                   page_icon="🖼️",
                   layout="wide")

ACCENT   = "#1ABC9C"     # same teal you use everywhere
BG_DARK  = "#111111"     # nearly-black background
TEXT_LGT = "#EEEEEE"

# ───────────────────────── CSS styling ─────────────────────────
st.markdown(
    f"""
    <style>
    /* overall dark skin */
    .stApp {{ background:{BG_DARK}; color:{TEXT_LGT}; }}

    /* headings */
    h1, h2, h3, h4, h5, h6 {{ color:{ACCENT}; font-weight:bold; }}

    /* section subtitle */
    .subtitle {{ font-size:1.4rem; font-weight:bold; color:{TEXT_LGT}; }}

    /* card container */
    .card {{
        background-color:#000000;
        border:2px solid {ACCENT};
        border-radius:12px;
        padding:18px 20px 24px 20px;
        box-shadow:0px 4px 10px rgba(0,0,0,0.25);
        height:100%;
        display:flex;
        flex-direction:column;
        justify-content:space-between;
    }}

    .card-img {{
        width:100%;
        border-radius:10px;
        margin-bottom:15px;
        object-fit:cover;
    }}

    .skills span {{
        background:{ACCENT}22;
        padding:3px 8px;
        border-radius:6px;
        margin-right:6px;
        font-size:0.8rem;
    }}

    /* CTA button overrides */
    div.stButton>button:first-child {{
        background:{ACCENT};
        color:white;
        border-radius:8px;
        font-weight:bold;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ───────────────────────── App data ────────────────────────────
# • screenshot: local file or URL
# • demo_url   : external link (Streamlit Cloud, Render, etc.)
APPS = [
    {
        "title": "Cool Assistant",
        "tagline": "Location-aware, real-time survey & heat-map analytics",
        "screenshot": "https://raw.githubusercontent.com/AIforimpact22/coolassistant/main/docs/preview.png",
        "description": (
            "Collect emotional wellbeing data on a map, store everything in "
            "PostgreSQL, deduplicate automatically every hour, and share with "
            "one click via email or WhatsApp."
        ),
        "skills": ["Streamlit", "PostgreSQL", "Authentication", "Geospatial", "Data Cleaning"],
        "demo_url": "https://coolassistant.streamlit.app/",
        "code_url": "https://github.com/AIforimpact22/coolassistant",
    },
    {
        "title": "Inventory Tracker",
        "tagline": "Live stock monitoring for AMAS Hypermarket",
        "screenshot": "https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/inventory_demo.png",
        "description": (
            "Barcode-based intake, reorder-point alerts, expiry dashboards, and "
            "supplier scorecards – all driven from one shared database."
        ),
        "skills": ["SQL", "Pandas", "Streamlit AgGrid", "Plotly"],
        "demo_url": "https://inventory-demo.streamlit.app/",
        "code_url": None,   # hide button if None
    },
    {
        "title": "Supplier Portal",
        "tagline": "Self-service portal for vendor bids & delivery schedules",
        "screenshot": "https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/supplier_demo.png",
        "description": (
            "Suppliers log in, upload quotations, track purchase orders, and "
            "book delivery slots – reducing email back-and-forth by 70 %."
        ),
        "skills": ["Streamlit", "JWT Auth", "Async API", "Scheduling"],
        "demo_url": None,   # demo still private
        "code_url": None,
    },
]

# ───────────────────────── Hero / intro ────────────────────────
st.markdown(
    f"""
    <div style="width:100%;text-align:center;">
        <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/impact_wave.svg"
             style="width:100%;height:auto;display:block;">
    </div>
    <h1 style="text-align:center;margin-top:0;">🖼️ Student & Instructor Gallery</h1>
    <p class="subtitle" style="text-align:center;">
        Real projects that move from <em>idea</em> to <em>impact</em> – and that <strong>you</strong> will learn to build.
    </p>
    <hr style="border:none;border-top:2px solid {ACCENT};margin:0 0 35px 0;">
    """,
    unsafe_allow_html=True,
)

# ───────────────────────── Card renderer ───────────────────────
def render_card(app: dict):
    """Render a single app showcase card."""
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.image(app["screenshot"], use_column_width=True, output_format="auto", caption=None)
    st.markdown(f"### {app['title']}", unsafe_allow_html=True)
    st.markdown(f"<em>{app['tagline']}</em>", unsafe_allow_html=True)
    st.markdown(f"<p style='margin-top:10px;'>{app['description']}</p>", unsafe_allow_html=True)

    # skills badges
    if app["skills"]:
        skills_html = " ".join(f"<span>{skill}</span>" for skill in app["skills"])
        st.markdown(f"<p class='skills'>{skills_html}</p>", unsafe_allow_html=True)

    # buttons
    btn_cols = st.columns(2)
    if app.get("demo_url"):
        with btn_cols[0]:
            st.link_button("🖥️ Live Demo", app["demo_url"], use_container_width=True)
    if app.get("code_url"):
        with btn_cols[1]:
            st.link_button("📂 Source Code", app["code_url"], use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ───────────────────────── Gallery grid ────────────────────────
# Two cards per row on wide screens
for i in range(0, len(APPS), 2):
    cols = st.columns(2, gap="large")
    for col, app in zip(cols, APPS[i : i + 2]):
        with col:
            render_card(app)

# ───────────────────────── CTA banner ──────────────────────────
st.markdown(
    f"""
    <hr style="border:none;border-top:2px solid {ACCENT};margin:40px 0 20px 0;">
    <h2 style="text-align:center;">Ready to build and showcase your own project?</h2>
    """,
    unsafe_allow_html=True,
)
center = st.columns(3)[1]   # simple centering trick
with center:
    st.link_button("🚀 Apply Now", "https://docs.google.com/forms/d/e/1FAIpQLSdfISuw6xQvoXI-VFrPQ_HGkQ56ftr4uXr0BKrDCZM4GuKxHw/viewform?usp=header",
                   use_container_width=True)
