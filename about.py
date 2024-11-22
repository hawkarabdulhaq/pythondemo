import streamlit as st
from dictionary import translate  # Import the centralized translate function

def show():
    language = st.session_state.language  # Retrieve the selected language

    # Display the title
    st.markdown(f'<div class="title">{translate("about_title", language)}</div>', unsafe_allow_html=True)

    # Display the profile photo
    st.image(
        "input/me.jpg",
        width=250,
        caption=translate("about_caption", language),
        use_column_width="auto",
    )

    # Profile Overview
    st.markdown(f"""
    <div class="content">
        {translate("about_overview", language)}
    </div>
    """, unsafe_allow_html=True)

    # Section: Early Career and Education
    st.markdown(f"""
    <div class="section-title">{translate("about_early_career_title", language)}</div>
    <div class="content">
        {translate("about_early_career_content", language)}
    </div>
    """, unsafe_allow_html=True)

    # Section: Hasar Organization and PhD Studies
    st.markdown(f"""
    <div class="section-title">{translate("about_hasar_title", language)}</div>
    <div class="content">
        {translate("about_hasar_content", language)}
    </div>
    """, unsafe_allow_html=True)

    # Section: Research and Publications
    st.markdown(f"""
    <div class="section-title">{translate("about_research_title", language)}</div>
    <div class="content">
        {translate("about_research_content", language)}
        <ul>
            <li><strong>{translate("about_publication_1", language)}</strong></li>
            <li><strong>{translate("about_publication_2", language)}</strong></li>
            <li><strong>{translate("about_publication_3", language)}</strong></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Section: A Passion for Coding and Innovation
    st.markdown(f"""
    <div class="section-title">{translate("about_coding_title", language)}</div>
    <div class="content">
        {translate("about_coding_content", language)}
    </div>
    """, unsafe_allow_html=True)

    # Section: Entrepreneurial Ventures
    st.markdown(f"""
    <div class="section-title">{translate("about_ventures_title", language)}</div>
    <div class="content">
        {translate("about_ventures_content", language)}
    </div>
    """, unsafe_allow_html=True)

    # Section: Call to Action
    st.markdown(f"""
    <div class="content" style="margin-top: 40px;">
        <p>{translate("about_call_to_action", language)}</p>
    </div>
    """, unsafe_allow_html=True)
