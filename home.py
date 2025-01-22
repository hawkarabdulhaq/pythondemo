import streamlit as st

def show():
    # Welcome section
    st.markdown("""
    <div class="title">Learn AI and Machine Learning Faster and Smarter</div>
    <div class="subtitle">Empower your business with cutting-edge skills and insights!</div>
    """, unsafe_allow_html=True)
    
    # Perfect for beginners
    st.markdown("""
    <div class="content"><strong>Designed for beginners and professionals alike!</strong></div>
    """, unsafe_allow_html=True)

    # Embed YouTube video
    st.markdown("""
    <div class="video-container">
        <h3>Watch Our Demo</h3>
        <iframe width="853" height="600" src="https://www.youtube.com/embed/G8BC2NIfpAs" 
        title="Fast Learning with Releafs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
        encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    # What We Offer Section
    st.markdown(
        '<div class="section-title" style="color: #1ABC9C;">Our Services</div>', 
        unsafe_allow_html=True
    )
    st.markdown("""
    <div class="content">
    - **Training**: Learn AI, Machine Learning, and Automation the fast and easy way.<br><br>
    - **Analysis**: Get a customized, data-driven plan to make your business smarter and more efficient.<br><br>
    - **Solutions**: Build powerful, data-driven tools tailored to your business needs.<br><br>
    </div>
    """, unsafe_allow_html=True)
    
    # Enrollment Button
    if st.button("Get Started Now"):
        st.session_state.page = "Prices"
        st.experimental_rerun()  # Force an immediate rerun
