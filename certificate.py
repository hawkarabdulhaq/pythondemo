import streamlit as st

def show():
    st.markdown('<div class="title">Course Completion Certificate</div>', unsafe_allow_html=True)

    # Description about the certificates
    st.markdown("""
    <div class="content">
        Congratulations on taking a step toward enhancing your skills with the <strong>Personalized Python Programming and Automating Training</strong>. 
        Trainees who successfully complete the course requirements will be awarded a <strong>Certificate of Completion</strong>. This certificate serves as a 
        testament to your hard work, dedication, and newly acquired programming expertise.
    </div>
    """, unsafe_allow_html=True)

    # Display portrait certificate
    st.markdown("<h3>Portrait Certificate</h3>", unsafe_allow_html=True)
    st.image('/input/p.jpg', caption='Portrait Certificate', use_column_width=True)

    # Display landscape certificate
    st.markdown("<h3>Landscape Certificate</h3>", unsafe_allow_html=True)
    st.image('/input/l.jpg', caption='Landscape Certificate', use_column_width=True)

    # Additional information
    st.markdown("""
    <div class="content">
        Both styles of certificates are available and will be customized with your name and completion details upon fulfilling the course requirements.
    </div>
    """, unsafe_allow_html=True)
