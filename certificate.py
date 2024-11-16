import streamlit as st

def show():
    st.markdown('<div class="title">Course Completion Certificates</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
        Trainees will receive a certificate upon successfully completing all course requirements. This certificate is a testament to your dedication, hard work, and mastery of Python programming and automation. Below are the two styles of certificates available:
    </div>
    """, unsafe_allow_html=True)

    # Apply custom CSS for zoom effect
    st.markdown("""
    <style>
        /* Container for zoom effect */
        .zoom-container {
            position: relative;
            overflow: hidden;
        }

        /* Zoom effect on hover */
        .zoom-container img {
            transition: transform 0.3s ease-in-out;
        }

        .zoom-container:hover img {
            transform: scale(1.2); /* Adjust zoom level */
        }
    </style>
    """, unsafe_allow_html=True)

    # Portrait Certificate
    st.markdown("<h3>Portrait Certificate</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="zoom-container">
        <img src="input/p.jpg" alt="Portrait Certificate" style="width: 100%; border: 1px solid var(--border-color); border-radius: 10px;">
    </div>
    """, unsafe_allow_html=True)

    # Landscape Certificate
    st.markdown("<h3>Landscape Certificate</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="zoom-container">
        <img src="input/l.jpg" alt="Landscape Certificate" style="width: 100%; border: 1px solid var(--border-color); border-radius: 10px;">
    </div>
    """, unsafe_allow_html=True)
