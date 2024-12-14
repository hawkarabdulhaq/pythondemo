import streamlit as st
from dictionary import translate  # Import the centralized translate function

def show():
    language = st.session_state.language  # Retrieve the selected language

    # Welcome section
    st.markdown(f"""
    <div class="title">{translate("welcome_title", language)}</div>
    <div class="subtitle">{translate("subtitle", language)}</div>
    """, unsafe_allow_html=True)
    
    # Perfect for beginners
    st.markdown(f"""
    <div class="content"><strong>{translate("perfect_for_beginners", language)}</strong></div>
    """, unsafe_allow_html=True)

    # Embed YouTube video
    st.markdown(f"""
    <div class="video-container">
        <h3>{translate("watch_demo", language)}</h3>
        <iframe width="853" height="600" src="https://www.youtube.com/embed/G8BC2NIfpAs" 
        title="ڕاهێنانی کۆدینگ لەگەڵ هاوکار" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
        encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    # What We Offer Section
    st.markdown(
        f'<div class="section-title" style="color: #1ABC9C;">{translate("what_we_offer_title", language)}</div>', 
        unsafe_allow_html=True
    )
    st.markdown(f"""
    <div class="content">
    - {translate("offer_1", language)}<br><br>
    - {translate("offer_2", language)}<br><br>
    - {translate("offer_3", language)}<br><br>
    - {translate("offer_4", language)}<br><br>
    - {translate("offer_5", language)}
    </div>
    """, unsafe_allow_html=True)
    
    # Enrollment Button - Clicking this should take the user to the "Prices" page
    if st.button(translate("enroll_button", language)):
        st.session_state.page = "Prices"
