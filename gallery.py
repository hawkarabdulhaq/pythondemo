import json
import pathlib
import streamlit as st

def load_cards():
    path = pathlib.Path("input/gallery.json")
    return json.loads(path.read_text()) if path.is_file() else []

def render_card(card: dict):
    button_html = ""
    if card.get("demo_url"):
        button_html = f"""
        <a class="demo-button" href="{card['demo_url']}" target="_blank">
            🖥️ Live Demo
        </a>
        """

    card_html = f"""
    <div class="card">
        <h3>{card.get('headline', 'Showcase')}</h3>
        <img src="{card.get('screenshot', '')}" alt="{card.get('headline', '')}"/>
        <p>{card.get('description', '')}</p>
    """

    if feats := card.get("features"):
        card_html += "<ul>" + "".join(f"<li>{feat}</li>" for feat in feats) + "</ul>"

    card_html += button_html + "</div>"

    st.markdown(card_html, unsafe_allow_html=True)

def show():
    st.title("🖼️ Project Gallery")
    st.markdown("---")

    # CSS for styling
    st.markdown("""
    <style>
        .card-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .card {
            background: #2f2f2f;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            flex: 1 1 calc(50% - 20px);
            max-width: calc(100% - 20px);
            margin-bottom: 20px;
            position: relative;
        }
        .card h3 {
            color: #ffffff;
            margin-bottom: 10px;
        }
        .card img {
            width: 100%;
            height: auto;
            border-radius: 10px;
            margin-bottom: 15px;
        }
        .card p, .card ul {
            color: #ffffff;
            line-height: 1.5;
        }
        .card ul {
            padding-left: 20px;
        }
        .demo-button {
            display: inline-block;
            background-color: #1ABC9C;
            color: #ffffff !important;
            padding: 10px 20px;
            border-radius: 8px;
            text-decoration: none;
            margin-top: 10px;
            font-weight: bold;
        }
        .demo-button:hover {
            opacity: 0.8;
        }
        @media screen and (max-width: 768px) {
            .card {
                flex: 1 1 100%;
                max-width: 100%;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    cards = load_cards()

    if not cards:
        st.info("No gallery items found. Add some cards to `input/gallery.json`.")
        return

    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    for card in cards:
        render_card(card)

    st.markdown('</div>', unsafe_allow_html=True)
