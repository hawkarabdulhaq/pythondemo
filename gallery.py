# Improved gallery.py
import json, pathlib, streamlit as st

ACCENT, BG, CARD_BG = "#1ABC9C", "#111111", "#000000"

def load_cards():
    p = pathlib.Path("input/gallery.json")
    return json.loads(p.read_text()) if p.exists() else []

def render_card(card: dict):
    card_html = f"""
    <div class='card'>
        <img src='{card.get("screenshot")}' alt='Preview'>
        <h3>{card.get("headline", "Untitled")}</h3>
        <p>{card.get("description", "—")}</p>
        <ul>
            {''.join(f"<li>{feat}</li>" for feat in card.get("features", []))}
        </ul>
        <div class='links'>
            {"<a href='" + card["demo_url"] + "' target='_blank'>🖥️ Live Demo</a>" if card.get("demo_url") else ""}
            {"<a href='" + card["code_url"] + "' target='_blank'>📂 Source Code</a>" if card.get("code_url") else ""}
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

def show() -> None:
    if "gallery_css_loaded" not in st.session_state:
        st.session_state.gallery_css_loaded = True
        st.markdown(f"""
        <style>
        .stApp {{
            background-color: {BG};
            color: #EEEEEE;
            font-family: 'Segoe UI', sans-serif;
        }}
        .gallery-frame {{
            border: 3px solid {ACCENT};
            border-radius: 20px;
            padding: 40px;
            background: {CARD_BG};
            box-shadow: 0 0 15px rgba(0,0,0,0.6);
        }}
        h1 {{
            color: {ACCENT};
            text-align: center;
            margin-bottom: 5px;
        }}
        h3 {{
            color: {ACCENT};
            margin-top: 10px;
        }}
        .card {{
            background: #080808;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            transition: transform 0.3s, box-shadow 0.3s;
            margin-bottom: 25px;
        }}
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.6);
        }}
        .card img {{
            width: 100%;
            border-radius: 8px;
            margin-bottom: 15px;
        }}
        .card ul {{
            margin-left: 18px;
            margin-bottom: 15px;
        }}
        .card .links a {{
            display: inline-block;
            background: {ACCENT};
            color: #FFF;
            padding: 8px 12px;
            border-radius: 8px;
            text-decoration: none;
            margin-right: 10px;
            font-weight: bold;
        }}
        </style>
        """, unsafe_allow_html=True)

    # Start frame
    st.markdown("<div class='gallery-frame'>", unsafe_allow_html=True)

    # Header
    st.markdown("""
    <h1>🖼️ Project Showcase</h1>
    <p style='text-align:center;'>Real examples demonstrating practical skills you'll master.</p>
    <hr style='border:none;border-top:2
