import streamlit as st

def show():
    st.markdown('<div class="title">Course Completion Certificates</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
        Trainees will receive a certificate upon successfully completing all course requirements. This certificate is a testament to your dedication, hard work, and mastery of Python programming and automation. Below are the two styles of certificates available:
    </div>
    """, unsafe_allow_html=True)

    # Display portrait certificate
    st.markdown("<h3>Portrait Certificate</h3>", unsafe_allow_html=True)
    st.image("input/p.jpg", caption="Portrait Certificate", use_column_width=True)

    # Display landscape certificate
    st.markdown("<h3>Landscape Certificate</h3>", unsafe_allow_html=True)
    st.image("input/l.jpg", caption="Landscape Certificate", use_column_width=True)
