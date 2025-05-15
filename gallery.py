import json
import pathlib
import streamlit as st

def load_cards():
    path = pathlib.Path("input/gallery.json")
    return json.loads(path.read_text()) if path.is_file() else []

def render_card(card: dict):
    with st.container():
        st.markdown(
            f"""
            <div class="card">
                <h3>{card.get('headline', 'Showcase')}</h3>
                <img class="card-img" src="{card.get('screenshot', '')}" alt="{card.get('headline', '')}">
                <p>{card.get('description', '')}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if feats := card.get("features"):
            st.markdown(
                "<ul>" + "".join(f"<li>{feat}</li>" for feat in feats) + "</ul>",
                unsafe_allow_html=True,
            )

        cols = st.columns(2)

        if card.get("demo_url"):
            cols[0].link_button(
                "🖥️ Live Demo", card["demo_url"], use_container_width=True
            )

        if card.get("code_url"):
            cols[1].link_button(
                "📂 Source Code", card["code_url"], use_container_width=True
            )

def show():
    st.title("🖼️ Project Gallery")
    st.markdown("---")

    # CSS for styling (consistent with trainings.py)
    st.markdown(
        """
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
        }
        .card h3 {
            color: #ffffff;
            margin-bottom: 10px;
        }
        .card-img {
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
        @media screen and (max-width: 768px) {
            .card {
                flex: 1 1 100%;
                max-width: 100%;
            }
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    cards = load_cards()

    if not cards:
        st.info("No gallery items found. Add some cards to `input/gallery.json`.")
        return

    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    for card in cards:
        render_card(card)

    st.markdown("</div>", unsafe_allow_html=True)
