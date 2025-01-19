import streamlit as st
import base64
import pandas as pd
from dictionary import translate  # Import the centralized translate function

def load_image_as_base64(image_path):
    """Load an image and return it as a Base64 encoded string."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def show_certificate_system():
    language = st.session_state.language  # Retrieve the selected language

    st.markdown(f'<div class="title">{translate("certificate_title", language)}</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="content">
        {translate("certificate_description", language)}
    </div>
    """, unsafe_allow_html=True)

    # Load images as Base64
    portrait_image_base64 = load_image_as_base64("input/p.jpg")
    landscape_image_base64 = load_image_as_base64("input/l.jpg")

    # Apply custom CSS for secure display and zoom effect
    st.markdown(f"""
    <style>
        /* Container for zoom effect */
        .zoom-container {{
            position: relative;
            overflow: hidden;
        }}

        /* Zoom effect on hover */
        .zoom-container img {{
            transition: transform 0.3s ease-in-out;
            border-radius: 10px;
            border: 1px solid var(--border-color);
        }}

        .zoom-container:hover img {{
            transform: scale(1.2);
        }}

        /* Disable right-click on images */
        .zoom-container img {{
            pointer-events: none;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Portrait Certificate
    st.markdown(f"<h3>{translate('portrait_certificate_title', language)}</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="zoom-container">
        <img src="data:image/jpeg;base64,{portrait_image_base64}" alt="{translate('portrait_certificate_alt', language)}" style="width: 100%;">
    </div>
    """, unsafe_allow_html=True)

    # Landscape Certificate
    st.markdown(f"<h3>{translate('landscape_certificate_title', language)}</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="zoom-container">
        <img src="data:image/jpeg;base64,{landscape_image_base64}" alt="{translate('landscape_certificate_alt', language)}" style="width: 100%;">
    </div>
    """, unsafe_allow_html=True)

def show_certificate_database():
    language = st.session_state.language  # Retrieve the selected language

    st.title(translate("certificate_database_title", language))

    # Load the CSV data
    df = pd.read_csv("input/certificate.csv")

    # Filter rows where the participant has completed the course.
    completed_df = df[df["date of completion"].notna() & (df["date of completion"] != "")]

    if completed_df.empty:
        st.write(translate("no_participants_message", language))
    else:
        # Display each completed participant's info and certificate
        for _, participant_info in completed_df.iterrows():
            st.markdown(f"### {participant_info['name']}")

            col1, col2 = st.columns([1, 2])
            with col1:
                st.write(f"**{translate('name', language)}:** {participant_info['name']}")
                st.write(f"**{translate('date_of_joining', language)}:** {participant_info['date of joining']}")
                st.write(f"**{translate('date_of_completion', language)}:** {participant_info['date of completion']}")
                st.write(f"**{translate('credential', language)}:** {participant_info['credential']}")

            with col2:
                # Load and display their certificate
                cert_path = participant_info["certificate"]
                cert_base64 = load_image_as_base64(cert_path)
                st.markdown(f"""
                <div class="zoom-container" style="margin-top: 10px;">
                    <img src="data:image/jpeg;base64,{cert_base64}" alt="{translate('certificate_alt', language)}" style="width: 100%;">
                </div>
                """, unsafe_allow_html=True)

            st.markdown("---")  # Divider between participants

def show():
    """Existing show function to maintain compatibility in app.py"""
    tab1, tab2 = st.tabs(["Our Certificate System", "Certificate database"])

    with tab1:
        show_certificate_system()

    with tab2:
        show_certificate_database()
