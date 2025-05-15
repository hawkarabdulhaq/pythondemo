# gallery.py  –  Showcase driven by input/gallery.json
import json, pathlib, streamlit as st

# ───────────────────────── config & style ─────────────────────────
ACCENT, BG = "#1ABC9C", "#111111"
st.set_page_config("Gallery", page_icon="🖼️", layout="wide")

st.markdown(f"""
<style>
.stApp {{ background:{BG}; color:#EEE; }}
h1, h2, h3 {{ color:{ACCENT}; }}
.card {{
  background:#000; border:2px solid {ACCENT}; border-radius:12px;
  padding:20px; box-shadow:0 4px 8px #0006;
}}
.card img {{ width:100%; border-radius:8px; margin-bottom:14px; }}
.card button {{ background:{ACCENT}; color:#FFF; border-radius:8px; font-weight:bold; }}
</style>
""", unsafe_allow_html=True)

# ───────────────────────── helpers ────────────────────────────────
def load_cards():
    path = pathlib.Path("input/gallery.json")
    if path.is_file():
        with path.open() as f:
            return json.load(f)
    return []

def render_card(card: dict):
    """Renders a single gallery card."""
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    # Screenshot
    if card.get("screenshot"):
        st.image(card["screenshot"], use_container_width=True)

    # Copy
    st.subheader(card.get("headline", "Untitled Showcase"))
    st.write(card.get("description", "—"))

    # Feature bullets
    if feats := card.get("features"):
        st.markdown("\n".join(f"- {f}" for f in feats))

    # Buttons (labels made unique by including the headline)
    cols = st.columns(2)
    if card.get("demo_url"):
        cols[0].link_button(
            f"🖥️ Live Demo · {card['headline']}",    # unique label
            card["demo_url"],
            use_container_width=True,
        )
    if card.get("code_url"):
        cols[1].link_button(
            f"📂 Source Code · {card['headline']}",
            card["code_url"],
            use_container_width=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ───────────────────────── page content ───────────────────────────
st.markdown("""
<h1 style='text-align:center'>🖼️ Project Gallery</h1>
<p style='text-align:center;font-size:1.2rem;'>
  Real examples you’ll be able to build after the course.
</p>
<hr style='border:none;border-top:2px solid #1ABC9C;margin:0 0 35px 0;'>
""", unsafe_allow_html=True)

cards = load_cards()
if not cards:
    st.info("No showcase cards defined yet — add some to `input/gallery.json`")
else:
    for card in cards:
        render_card(card)
        st.markdown("<!-- spacer -->", unsafe_allow_html=True)
