import json, pathlib, streamlit as st

ACCENT, BG, CARD_BG = "#1ABC9C", "#111111", "#181818"

# ──────────────────────────── helpers ────────────────────────────
def load_cards():
    p = pathlib.Path("input/gallery.json")
    return json.loads(p.read_text()) if p.is_file() else []

def render_card(card: dict):
    st.markdown("<div class='gallery-card'>", unsafe_allow_html=True)

    # Image section
    if card.get("screenshot"):
        st.image(card["screenshot"], use_container_width=True)

    # Text section
    st.markdown(
        f"<h3 class='card-title'>{card.get('headline','Showcase')}</h3>",
        unsafe_allow_html=True
    )
    st.markdown(f"<p>{card.get('description','')}</p>", unsafe_allow_html=True)

    # Feature list (bullet style)
    if feats := card.get("features"):
        feat_html = "<ul>" + "".join(f"<li>{f}</li>" for f in feats) + "</ul>"
        st.markdown(feat_html, unsafe_allow_html=True)

    # Buttons (side-by-side, evenly spaced)
    cols = st.columns(2)
    if card.get("demo_url"):
        cols[0].link_button("🖥️ Live Demo", card["demo_url"],
                            use_container_width=True)
    if card.get("code_url"):
        cols[1].link_button("📂 Source Code", card["code_url"],
                            use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ──────────────────────────── PUBLIC API ────────────────────────────
def show() -> None:
    """Render the Gallery page (called from app.py)."""

    # Inject CSS once
    if "gallery_css_loaded" not in st.session_state:
        st.session_state.gallery_css_loaded = True
        st.markdown(f"""
        <style>
        /* General app styling */
        .stApp {{
            background-color:{BG}; color:#E4E4E4;
        }}

        /* Gallery frame styling */
        .gallery-frame {{
            border: 3px solid {ACCENT};
            border-radius: 20px;
            padding: 30px;
            background-color: {CARD_BG};
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
            margin-bottom: 50px;
        }}

        /* Card styling */
        .gallery-card {{
            border-radius: 15px;
            padding: 20px;
            background-color: {BG};
            box-shadow: 0 3px 10px rgba(0,0,0,0.6);
            margin-bottom: 30px;
        }}

        /* Card title */
        .card-title {{
            color: {ACCENT};
            margin-top: 15px;
            margin-bottom: 10px;
        }}

        /* Bullet styling */
        .gallery-card ul {{
            margin-left: 18px;
            margin-bottom: 20px;
        }}

        /* Button styling override */
        .stButton > button, .stLinkButton > a {{
            background-color: {ACCENT};
            color: #FFFFFF;
            font-weight: bold;
            border-radius: 8px;
        }}

        h1 {{
            color: {ACCENT};
            font-size: 2.5rem;
        }}

        hr {{
            border:none;
            border-top: 2px solid {ACCENT};
            margin: 20px 0;
        }}
        </style>
        """, unsafe_allow_html=True)

    # Open main gallery frame
    st.markdown("<div class='gallery-frame'>", unsafe_allow_html=True)

    # Header area
    st.markdown("""
    <h1 style='text-align:center'>🖼️ Project Gallery</h1>
    <p style='text-align:center;font-size:1.2rem; margin-bottom:30px;'>
      Real-world projects you will build, deploy, and showcase.
    </p>
    <hr>
    """, unsafe_allow_html=True)

    # Load and display cards
    cards = load_cards()
    if not cards:
        st.info("No showcase cards yet — add examples in `input/gallery.json`.")
    else:
        for card in cards:
            render_card(card)

    # Close main gallery frame
    st.markdown("</div>", unsafe_allow_html=True)
