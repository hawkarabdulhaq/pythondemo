import streamlit as st
from dictionary import translate

def show():
    language = st.session_state.language  # Retrieve the selected language
    
    # Welcome section
    st.markdown(f"""
    <div class="title">{translate("welcome_title", language)}</div>
    <div class="subtitle"><strong>{translate("subtitle", language)}</strong></div>
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

    # What We Offer section
    st.markdown(f'<div class="section-title" style="color: #1ABC9C;">{translate("what_we_offer_title", language)}</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="content">
    - <strong>{translate("offer_1", language)}</strong><br><br>
    - <strong>{translate("offer_2", language)}</strong><br><br>
    - <strong>{translate("offer_3", language)}</strong><br><br>
    - <strong>{translate("offer_4", language)}</strong><br><br>
    - <strong>{translate("offer_5", language)}</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # Enrollment Button
    if st.button(translate("enroll_button", language)):
        st.session_state.page = "Enrollment"
