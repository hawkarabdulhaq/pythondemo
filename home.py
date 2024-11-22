import streamlit as st
from dictionary import translations

def translate(key):
    return translations.get(key, {}).get(st.session_state.language, key)

def show():
    # Welcome section
    st.markdown(f"""
    <div class="title">{translate("welcome_title")}</div>
    <div class="subtitle"><strong>{translate("subtitle")}</strong></div>
    """, unsafe_allow_html=True)
    
    # Perfect for beginners
    st.markdown(f"""
    <div class="content"><strong>{translate("perfect_for_beginners")}</strong></div>
    """, unsafe_allow_html=True)

    # Embed YouTube video
    st.markdown(f"""
    <div class="video-container">
        <h3>{translate("watch_demo")}</h3>
        <iframe width="853" height="600" src="https://www.youtube.com/embed/G8BC2NIfpAs" 
        title="ڕاهێنانی کۆدینگ لەگەڵ هاوکار" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
        encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    # What We Offer section
    st.markdown(f'<div class="section-title" style="color: #1ABC9C;">{translate("what_we_offer_title")}</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="content">
    - <strong>{translate("offer_1")}</strong><br><br>
    - <strong>{translate("offer_2")}</strong><br><br>
    - <strong>{translate("offer_3")}</strong><br><br>
    - <strong>{translate("offer_4")}</strong><br><br>
    - <strong>{translate("offer_5")}</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # Enrollment Button
    if st.button(translate("enroll_button")):
        st.session_state.page = "Enrollment"
