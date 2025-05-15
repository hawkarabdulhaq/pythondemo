import json
import pathlib
import streamlit as st

def load_cards():
    path = pathlib.Path("input/gallery.json")
    return json.loads(path.read_text()) if path.is_file() else []

def show():
    st.title("🖼️ Project Gallery")
    st.markdown("---")

    # Minimal, clean CSS styling
    st.markdown("""
    <style>
        .card {
            background-color: #2f2f2f;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 3px 6px rgba(0,0,0,0.2);
            margin-bottom: 15px;
        }
        .card a {
            text-decoration: none;
            color: #1ABC9C;
        }
        .card a:hover {
            text-decoration: underline;
        }
        .card-title {
            font-size: 1.5em;
            margin-bottom: 10px;
        }
        .card p, .card li {
            color: #ffffff;
            line-height: 1.5;
        }
        ul.highlights {
            padding-left: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    cards = load_cards()

    if not cards:
        st.info("No gallery items found. Add cards to `input/gallery.json`.")
        return

    for card in cards:
        card_html = f"""
        <div class="card">
            <div class="card-title">
                <a href="{card.get('demo_url', '#')}" target="_blank">
                    {card.get('headline', 'Untitled')}
                </a>
            </div>
            <p>{card.get('description', '')}</p>
            <ul class="highlights">
        """

        if highlights := card.get("highlights"):
            for item in highlights:
                card_html += f"<li>{item}</li>"

        card_html += "</ul></div>"

        st.markdown(card_html, unsafe_allow_html=True)
