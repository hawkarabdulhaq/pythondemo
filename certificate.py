import streamlit as st
import base64
from dictionary import translate  # Import the centralized translate function

def load_image_as_base64(image_path):
    """Load an image and return it as a Base64 encoded string."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def show():
    language = st.session_state.language  # Retrieve the selected language

    st.markdown(f'<div class="title">{translate("certificate_title", language)}</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="content">
        {translate("certificate_description", language)}
    </div>
    """, unsafe_allow_html=True)

    # Load images as Base64
    portrait_image_base64 = load_image_as_base64("input/p.jpg")
    landscape_image_base64 = load_image_as_base64("input/l.jpg")

    # Apply custom CSS for secure display and zoom effect
    st.markdown(f"""
    <style>
        /* Container for zoom effect */
        .zoom-container {{
            position: relative;
            overflow: hidden;
        }}

        /* Zoom effect on hover */
        .zoom-container img {{
            transition: transform 0.3s ease-in-out;
            border-radius: 10px;
            border: 1px solid var(--border-color);
        }}

        .zoom-container:hover img {{
            transform: scale(1.2); /* Adjust zoom level */
        }}

        /* Disable right-click on images */
        .zoom-container img {{
            pointer-events: none;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Portrait Certificate
    st.markdown(f"<h3>{translate('portrait_certificate_title', language)}</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="zoom-container">
        <img src="data:image/jpeg;base64,{portrait_image_base64}" alt="{translate('portrait_certificate_alt', language)}" style="width: 100%;">
    </div>
    """, unsafe_allow_html=True)

    # Landscape Certificate
    st.markdown(f"<h3>{translate('landscape_certificate_title', language)}</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="zoom-container">
        <img src="data:image/jpeg;base64,{landscape_image_base64}" alt="{translate('landscape_certificate_alt', language)}" style="width: 100%;">
    </div>
    """, unsafe_allow_html=True)
