import streamlit as st
import base64

def load_image_as_base64(image_path):
    """Load an image and return it as a Base64 encoded string."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def show():
    st.markdown('<div class="title">Course Completion Certificates</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
        Trainees will receive a certificate upon successfully completing all course requirements. This certificate is a testament to your dedication, hard work, and mastery of Python programming and automation. Below are the two styles of certificates available:
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
    st.markdown("<h3>Portrait Certificate</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="zoom-container">
        <img src="data:image/jpeg;base64,{portrait_image_base64}" alt="Portrait Certificate" style="width: 100%;">
    </div>
    """, unsafe_allow_html=True)

    # Landscape Certificate
    st.markdown("<h3>Landscape Certificate</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="zoom-container">
        <img src="data:image/jpeg;base64,{landscape_image_base64}" alt="Landscape Certificate" style="width: 100%;">
    </div>
    """, unsafe_allow_html=True)
