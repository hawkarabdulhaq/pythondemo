import streamlit as st

def show():
    language = "EN"  # Set default language

    # Welcome section
    st.markdown("""
    <div class="title">Welcome to Our Platform</div>
    <div class="subtitle">Your gateway to innovative learning!</div>
    """, unsafe_allow_html=True)
    
    # Perfect for beginners
    st.markdown("""
    <div class="content"><strong>Perfect for beginners!</strong></div>
    """, unsafe_allow_html=True)

    # Embed YouTube video
    st.markdown("""
    <div class="video-container">
        <h3>Watch Demo</h3>
        <iframe width="853" height="600" src="https://www.youtube.com/embed/G8BC2NIfpAs" 
        title="Coding Training with Hawkar" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
        encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    # What We Offer Section
    st.markdown(
        '<div class="section-title" style="color: #1ABC9C;">What We Offer</div>', 
        unsafe_allow_html=True
    )
    st.markdown("""
    <div class="content">
    - Comprehensive Coding Courses<br><br>
    - Live and Interactive Sessions<br><br>
    - Dedicated Mentorship<br><br>
    - Career Development Guidance<br><br>
    - Flexible and Affordable Options
    </div>
    """, unsafe_allow_html=True)
    
    # Enrollment Button
    if st.button("Enroll Now"):
        st.session_state.page = "Prices"
        st.experimental_rerun()  # Force an immediate rerun
