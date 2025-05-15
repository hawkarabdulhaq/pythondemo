# gallery.py – polished showcase powered by input/gallery.json
import json, pathlib, streamlit as st

ACCENT   = "#1ABC9C"      # teal
BG_DARK  = "#0a0a0a"      # gradient start
BG_DARK2 = "#111111"      # gradient end

# ───────────────────────── data helpers ─────────────────────────
def load_cards():
    path = pathlib.Path("input/gallery.json")
    return json.loads(path.read_text()) if path.is_file() else []

# ───────────────────────── CSS (once) ───────────────────────────
def inject_css():
    if "gallery_css" in st.session_state:
        return
    st.session_state.gallery_css = True
    st.markdown(f"""
    <style>
    /* page bg */
    .stApp {{
        background:linear-gradient(135deg,{BG_DARK} 0%,{BG_DARK2} 100%);
        color:#EEE;
        font-family: "Segoe UI", Roboto, sans-serif;
    }}

    /* glowing frame */
    .gallery-wrapper {{
        border:2px solid {ACCENT}AA;
        border-radius:22px;
        padding:40px 32px 50px;
        max-width:1200px;
        margin:auto;
        box-shadow:0 0 18px {ACCENT}55;
        background:#00000088;
    }}

    /* headers inside frame */
    .gallery-wrapper h1,
    .gallery-wrapper h2,
    .gallery-wrapper h3 {{ color:{ACCENT}; }}

    /* card grid */
    .gallery-card {{
        background:#0d0d0d;
        border:1px solid #ffffff14;
        border-radius:14px;
        padding:22px 22px 28px;
        box-shadow:0 4px 10px #0004;
        transition:transform .22s ease, box-shadow .22s ease;
    }}
    .gallery-card:hover {{
        transform:translateY(-6px) scale(1.01);
        box-shadow:0 8px 18px #0006;
    }}

    /* screenshots */
    .gallery-card img {{
        width:100%;
        border-radius:10px;
        margin-bottom:16px;
    }}

    /* buttons */
    .gallery-card button {{
        background:{ACCENT};
        color:#FFF;
        border-radius:8px;
        font-weight:600;
    }}
    </style>
    """, unsafe_allow_html=True)

# ───────────────────────── card renderer ───────────────────────
def render_card(card: dict):
    st.markdown("<div class='gallery-card'>", unsafe_allow_html=True)

    if card.get("screenshot"):
        st.image(card["screenshot"], use_container_width=True)

    st.subheader(card.get("headline", "Untitled Showcase"))
    st.write(card.get("description", "—"))

    if feats := card.get("features"):
        st.markdown("<br>".join(f"• {f}" for f in feats), unsafe_allow_html=True)

    cols = st.columns(2, gap="small")
    if card.get("demo_url"):
        cols[0].link_button("🖥️ Live Demo", card["demo_url"],
                            use_container_width=True)
    if card.get("code_url"):
        cols[1].link_button("📂 Source Code", card["code_url"],
                            use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ───────────────────────── PUBLIC API ──────────────────────────
def show() -> None:
    """Render the Gallery page (called from app.py)."""
    inject_css()

    # ── outer glowing frame ──
    st.markdown("<div class='gallery-wrapper'>", unsafe_allow_html=True)

    # header
    st.markdown("""
    <h1 style='text-align:center;margin-bottom:4px;'>🖼️ Project&nbsp;Gallery</h1>
    <p style='text-align:center;font-size:1.15rem;margin-top:0'>
      Real examples you’ll build on the course.
    </p>
    <hr style='border:none;border-top:2px solid #1ABC9C;margin:20px 0 40px;'>
    """, unsafe_allow_html=True)

    # cards grid (2 per row on wide screens)
    cards = load_cards()
    if not cards:
        st.info("No showcase cards found — add some to `input/gallery.json`")
    else:
        for left, right in zip(cards[::2], cards[1::2] + [{}]):
            cols = st.columns(2, gap="large")
            with cols[0]:
                render_card(left)
            if right:
                with cols[1]:
                    render_card(right)

    st.markdown("</div>", unsafe_allow_html=True)  # close frame
