import streamlit as st
import base64
import pandas as pd

def load_image_as_base64(image_path):
    """Load an image and return it as a Base64 encoded string."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image at path {image_path} not found.")
        return ""

def show():
    st.title("Certificate Database")

    # Load the CSV data
    try:
        df = pd.read_csv("input/certificate.csv")
    except FileNotFoundError:
        st.error("Certificate database file not found.")
        return

    # Filter rows where the participant has completed the course
    completed_df = df[df["date of completion"].notna() & (df["date of completion"] != "")]

    if completed_df.empty:
        st.write("No participants have completed the course yet.")
    else:
        # Display each completed participant's info and certificate
        for _, participant_info in completed_df.iterrows():
            st.markdown(f"### {participant_info['name']}")

            col1, col2 = st.columns([1, 2])
            with col1:
                st.write(f"**Name:** {participant_info['name']}")
                st.write(f"**Date of Joining:** {participant_info['date of joining']}")
                st.write(f"**Date of Completion:** {participant_info['date of completion']}")
                st.write(f"**Credential:** {participant_info['credential']}")

            with col2:
                # Load and display their certificate
                cert_path = participant_info["certificate"]
                cert_base64 = load_image_as_base64(cert_path)
                if cert_base64:
                    st.markdown(f"""
                    <div class="zoom-container" style="margin-top: 10px;">
                        <img src="data:image/jpg;base64,{cert_base64}" alt="Certificate" style="width: 100%;">
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown("---")  # Divider between participants
