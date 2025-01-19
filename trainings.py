import streamlit as st
import base64
import pandas as pd
from dictionary import translations  # Import translations dictionary

def load_image_as_base64(image_path):
    """Load an image and return it as a Base64 encoded string."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image at path {image_path} not found.")
        return ""

def translate(key):
    """Retrieve the translated text based on the current language."""
    return translations.get(key, {}).get(st.session_state.language, key).strip()

def show_trainings():
    """Display the 'Our Trainings' tab content."""
    language = st.session_state.language  # Retrieve the selected language
    st.title(translate("our_trainings_tab_title"))

    trainings = [
        "Python Programming through Generative AI for Beginners",
        "Micro Master Machine Learning and Data-Driven Systems",
        "Business Optimization through Advanced Automation",
    ]

    st.markdown("<h3>Our Trainings</h3>", unsafe_allow_html=True)
    for training in trainings:
        st.markdown(f"- {training}")

def show_certificate_system():
    language = st.session_state.language  # Retrieve the selected language

    st.markdown(f'<div class="title">{translate("certificate_title")}</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="content">
        {translate("certificate_description")}
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
            max-width: 100%;
            height: auto;
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
    st.markdown(f"<h3>{translate('portrait_certificate_title')}</h3>", unsafe_allow_html=True)
    if portrait_image_base64:
        st.markdown(f"""
        <div class="zoom-container">
            <img src="data:image/jpeg;base64,{portrait_image_base64}" alt="{translate('portrait_certificate_alt')}" style="width: 100%;">
        </div>
        """, unsafe_allow_html=True)

    # Landscape Certificate
    st.markdown(f"<h3>{translate('landscape_certificate_title')}</h3>", unsafe_allow_html=True)
    if landscape_image_base64:
        st.markdown(f"""
        <div class="zoom-container">
            <img src="data:image/jpeg;base64,{landscape_image_base64}" alt="{translate('landscape_certificate_alt')}" style="width: 100%;">
        </div>
        """, unsafe_allow_html=True)

def show_certificate_database():
    language = st.session_state.language  # Retrieve the selected language

    st.title(translate("certificate_database_title"))

    # Load the CSV data
    try:
        df = pd.read_csv("input/certificate.csv")
    except FileNotFoundError:
        st.error("Certificate database file not found.")
        return

    # Filter rows where the participant has completed the course.
    completed_df = df[df["date of completion"].notna() & (df["date of completion"] != "")]

    if completed_df.empty:
        st.write(translate("no_participants_message"))
    else:
        # Display each completed participant's info and certificate
        for _, participant_info in completed_df.iterrows():
            st.markdown(f"### {participant_info['name']}")

            col1, col2 = st.columns([1, 2])
            with col1:
                st.write(f"**{translate('name')}**: {participant_info['name']}")
                st.write(f"**{translate('date_of_joining')}**: {participant_info['date of joining']}")
                st.write(f"**{translate('date_of_completion')}**: {participant_info['date of completion']}")
                st.write(f"**{translate('credential')}**: {participant_info['credential']}")

            with col2:
                # Load and display their certificate
                cert_path = participant_info["certificate"]
                cert_base64 = load_image_as_base64(cert_path)
                if cert_base64:
                    st.markdown(f"""
                    <div class="zoom-container" style="margin-top: 10px;">
                        <img src="data:image/jpeg;base64,{cert_base64}" alt="{translate('certificate_alt')}" style="width: 100%;">
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown("---")  # Divider between participants

def show():
    """Display the tabs for the Streamlit app."""
    tab1, tab2, tab3 = st.tabs([
        translate("our_trainings_tab_title"),
        translate("our_certificate_system_tab_title"),
        translate("certificate_database_tab_title")
    ])

    with tab1:
        show_trainings()

    with tab2:
        show_certificate_system()

    with tab3:
        show_certificate_database()
