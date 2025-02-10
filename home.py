import streamlit as st

def show():
    # Custom Styling
    st.markdown(
        """
        <style>
        /* Center Align the IFrame */
        .iframe-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Title Text (Centered)
    st.markdown("<h1 style='text-align: center; color: white;'>Utilize AI and Machine Learning Faster and Smarter</h1>", unsafe_allow_html=True)

    # Embed the SVG via iframe (Replace with your actual hosted URL)
    svg_url = "https://github.com/hawkarabdulhaq/pythondemo/blob/main/impact_wave.svg"

    # Display SVG using an iframe
    st.markdown(f"""
        <div class="iframe-container">
            <iframe src="{svg_url}" width="800" height="450" style="border: none;"></iframe>
        </div>
    """, unsafe_allow_html=True)

    # Subtitle Text
    st.markdown("""
    <div style="text-align: center; font-size: 1.5em; font-weight: bold; color: #eeeeee; margin-top: 20px;">
        Transform your business into a data-driven, more resilient enterprise with us!
    </div>
    """, unsafe_allow_html=True)
