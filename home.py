import streamlit as st

def show():
    # Title
    st.markdown("<h1 style='text-align: center; color: white;'>Utilize AI and Machine Learning Faster and Smarter</h1>", unsafe_allow_html=True)

    # GitHub-hosted SVG URL (Ensure it's a direct raw URL)
    svg_url = "https://github.com/hawkarabdulhaq/pythondemo/blob/main/impact_wave.svg"

    # Display SVG as an Image
    st.image(svg_url, use_column_width=True)

    # Subtitle
    st.markdown("""
    <div style="text-align: center; font-size: 1.5em; font-weight: bold; color: #eeeeee; margin-top: 20px;">
        Transform your business into a data-driven, more resilient enterprise with us!
    </div>
    """, unsafe_allow_html=True)
