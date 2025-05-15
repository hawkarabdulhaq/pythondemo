import json
import pathlib
import streamlit as st

ACCENT = "#1ABC9C"

def load_cards():
    p = pathlib.Path("input/gallery.json")
    return json.loads(p.read_text()) if p.is_file() else []

def render_card(card: dict):
    chapters_html = ""
    if features := card.get("features"):
        chapters_html += "<ul>"
        for feat in features:
            chapters_html += f"<li>{feat}</li>"
        chapters_html += "</ul>"

    demo_btn = (f'<a class="button" href="{card["demo_url"]}" target="_blank">'
                f'🖥️ Live Demo</a>') if card.get("demo_url") else ""

    code_btn = (f'<a class="button" href="{card["code_url"]}" target="_blank">'
                f'📂 Source Code</a>') if card.get("code_url") else ""

    buttons_html = f"{demo_btn} {code_btn}"

    card_html = f"""
        <div class="card">
            <h3>{card.get('headline', 'Untitled Showcase')}</h3>
            <img src="{card.get('screenshot')}" alt="{card.get('headline')}"/>
            <p>{card.get('description', '')}</p>
            {chapters_html}
            <div style="margin-top:15px;">{buttons_html}</div>
        </div>
    """

    st.markdown(card_html, unsafe_allow_html=True)

def show():
    st.title("🖼️ Project Gallery")
    st.markdown("---")

    st.markdown(
        f"""
        <style>
        .gallery-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            padding: 20px;
            border: 3px solid {ACCENT};
            border-radius: 20px;
            background-color: #181818;
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
        }}
        .card {{
            background: #2f2f2f;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            flex: 1 1 calc(50% - 20px);
            max-width: calc(50% - 20px);
            margin-bottom: 20px;
        }}
        .card h3 {{
            color: {ACCENT};
            margin-bottom: 12px;
        }}
        .card img {{
            width: 100%;
            border-radius: 10px;
            margin-bottom: 15px;
        }}
        .card p, .card ul {{
            color: #ffffff;
            line-height: 1.5;
        }}
        .card ul {{
            padding-left: 20px;
        }}
        .button {{
            display: inline-block;
            background-color: {ACCENT};
            color: white !important;
            font-weight: bold;
            text-decoration: none;
            padding: 8px 12px;
            border-radius: 10px;
            margin-right: 8px;
        }}
        @media (max-width: 768px) {{
            .card {{
                flex: 1 1 100%;
                max-width: 100%;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    cards = load_cards()

    if not cards:
        st.info("No showcase cards yet — add examples in `input/gallery.json`.")
        return

    st.markdown('<div class="gallery-container">', unsafe_allow_html=True)

    for card in cards:
        render_card(card)

    st.markdown('</div>', unsafe_allow_html=True)
