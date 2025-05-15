# gallery.py – nicer layout: all content inside one green frame
import json, pathlib, streamlit as st

ACCENT, BG = "#1ABC9C", "#111111"

# ───────────────────────── helpers ─────────────────────────
def load_cards():
    p = pathlib.Path("input/gallery.json")
    return json.loads(p.read_text()) if p.is_file() else []

def render_card(card: dict):
    """Render one showcase card (inside the frame)."""
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    if card.get("screenshot"):
        st.image(card["screenshot"], use_container_width=True)

    st.subheader(card.get("headline", "Untitled Showcase"))
    st.write(card.get("description", "—"))

    if feats := card.get("features"):
        st.markdown("\n".join(f"- {f}" for f in feats))

    cols = st.columns(2)
    if card.get("demo_url"):
        cols[0].link_button("🖥️ Live Demo", card["demo_url"],
                            use_container_width=True)
    if card.get("code_url"):
        cols[1].link_button("📂 Source Code", card["code_url"],
                            use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ───────────────────────── PUBLIC API ─────────────────────
def show() -> None:
    """Render the Gallery page (called from app.py)."""

    # Inject CSS once
    if "gallery_css_loaded" not in st.session_state:
        st.session_state.gallery_css_loaded = True
        st.markdown(f"""
        <style>
        .stApp {{ background:{BG}; color:#EEE; }}

        /* big outer frame */
        .gallery-frame {{
            border:3px solid {ACCENT};
            border-radius:18px;
            padding:35px 28px 40px;
            margin-top:10px;
            background:#000;           /* subtle contrast with page BG */
        }}

        /* section titles */
        h1, h2, h3 {{ color:{ACCENT}; }}

        /* individual cards */
        .card {{
            background:#0d0d0d;
            border:1px solid {ACCENT}55;  /* lighter, so frame stands out */
            border-radius:12px;
            padding:20px;
            box-shadow:0 4px 8px #0004;
            margin-bottom:32px;
        }}
        .card img {{
            width:100%;
            border-radius:8px;
            margin-bottom:14px;
        }}
        .card button {{
            background:{ACCENT};
            color:#FFF;
            border-radius:8px;
            font-weight:bold;
        }}
        </style>
        """, unsafe_allow_html=True)

    # ──────── open frame ────────
    st.markdown("<div class='gallery-frame'>", unsafe_allow_html=True)

    # header
    st.markdown("""
    <h1 style='text-align:center'>🖼️ Project Gallery</h1>
    <p style='text-align:center;font-size:1.2rem;'>
      Real examples you’ll be able to build after the course.
    </p>
    <hr style='border:none;border-top:2px solid #1ABC9C;margin:0 0 35px 0;'>
    """, unsafe_allow_html=True)

    # cards
    cards = load_cards()
    if not cards:
        st.info("No showcase cards found — add some to `input/gallery.json`")
    else:
        for card in cards:
            render_card(card)

    # ──────── close frame ────────
    st.markdown("</div>", unsafe_allow_html=True)
