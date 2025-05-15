# gallery.py  –  Card data loaded from input/gallery.json
import json
import pathlib
import streamlit as st

# ───────────────── Config & constants ─────────────────
ACCENT = "#1ABC9C"      # teal accent everywhere
BG     = "#111111"      # background
DATA_FILE = pathlib.Path(__file__).parent / "input" / "gallery.json"

st.set_page_config("Gallery", page_icon="🖼️", layout="centered")

# ───────────────── CSS (one small block) ──────────────
st.markdown(
    f"""
    <style>
    .stApp {{ background:{BG}; color:#EEE; }}
    h1 {{ color:{ACCENT}; text-align:center; margin-bottom:0.2em; }}
    .card {{
        background:#000; border:2px solid {ACCENT}; border-radius:12px;
        padding:20px; box-shadow:0 4px 8px #0006;
    }}
    .card img {{ width:100%; border-radius:8px; margin-bottom:14px; }}
    .card button {{
        background:{ACCENT}; color:#FFF; border-radius:8px;
        font-weight:bold; width:100%;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ───────────────── Helper to load JSON ─────────────────
@st.cache_data(show_spinner=False)
def load_cards(path: pathlib.Path):
    if not path.exists():
        st.error(f"📂 No gallery file found at `{path}`")
        return []
    with path.open(encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            st.error(f"⚠️ JSON error in `{path.name}`\n\n{e}")
            return []

cards = load_cards(DATA_FILE)

# ───────────────── Header ─────────────────────────────
st.markdown(
    """
    <h1>🖼️ Project Gallery</h1>
    <p style='text-align:center;font-size:1.2rem;'>
      Real examples you’ll be able to build after the course.
    </p>
    <hr style='border:none;border-top:2px solid #1ABC9C;margin:0 0 35px 0;'>
    """,
    unsafe_allow_html=True,
)

# ───────────────── Card renderer ──────────────────────
def render_card(card: dict):
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    # screenshot
    st.image(card["image"], use_column_width=True)

    # optional headline
    if card.get("headline"):
        st.subheader(card["headline"])

    # description (supports markdown)
    st.markdown(card["description"], unsafe_allow_html=True)

    # highlights list
    if card.get("highlights"):
        st.markdown("\n".join(f"- {line}" for line in card["highlights"]), unsafe_allow_html=True)

    # optional demo button
    if card.get("demo_url"):
        st.link_button("🖥️ Live Demo", card["demo_url"], key=card["demo_url"])

    st.markdown("</div>", unsafe_allow_html=True)

# ───────────────── Render gallery grid ────────────────
if not cards:
    st.info("No showcase cards defined yet — add some to `input/gallery.json`.")
else:
    for card_dict in cards:
        render_card(card_dict)
        st.markdown("<!-- spacer -->", unsafe_allow_html=True)
