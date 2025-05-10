import streamlit as st
import base64
import pandas as pd
import prices  # Import Prices Module
import os

# GitHub raw base URL
GITHUB_BASE_URL = "https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/"

def show_certificate_database():
    """Display the 'Certificate Database' tab content."""
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
                # Get certificate path
                cert_path = str(participant_info["certificate"])
                if cert_path.startswith("certificates/"):
                    # Load from GitHub raw URL
                    cert_url = GITHUB_BASE_URL + cert_path
                    st.image(cert_url, caption="Certificate", use_container_width=True)
                else:
                    # Load from local file
                    if os.path.exists(cert_path):
                        st.image(cert_path, caption="Certificate", use_container_width=True)
                    else:
                        st.warning(f"Certificate not found: {cert_path}")
            st.markdown("---")  # Divider between participants

def show():
    """Display the tabs for the Streamlit app."""
    tab1, tab2, tab3 = st.tabs([
        "Steps-to-Expert",
        "Pricing Plans",
        "Certificate Database"
    ])

    with tab1:
        st.title("Steps-to-Expert: Our Incremental Learning Model")
        st.write(
            """
            Welcome to the **Steps-to-Expert** training model – a structured, data-driven journey designed to take you from beginner to expert in five progressive phases:

            1. **Simple Entry**  
               Begin with the fundamentals to build a strong foundation.
            2. **Incremental Growth I**  
               Enhance your skills with targeted, practical exercises.
            3. **Incremental Growth II**  
               Apply your knowledge through real-world challenges.
            4. **Incremental Growth III**  
               Advance further with complex problem-solving and technical integrations.
            5. **Capstone Project**  
               Demonstrate your mastery by completing a comprehensive, hands-on project.
            """
        )
        show_trainings()

