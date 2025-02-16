import streamlit as st
import base64
import pandas as pd
from ourtrainings import get_trainings, show_trainings
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
            Our **Steps-to-Expert** model is a structured, data-driven journey that helps participants
            move from beginners to advanced practitioners in five stages:

            1. **Simple Entry**  
               Get started with the fundamentals and hands-on basics.
            2. **Incremental Growth I**  
               Build upon core concepts with additional practical exercises.
            3. **Incremental Growth II**  
               Dive into more complex tasks, reinforcing knowledge through real-world examples.
            4. **Incremental Growth III**  
               Advance to high-level problem-solving and technical integrations.
            5. **Capstone Project**  
               Consolidate all your learning into a final project to demonstrate true expertise.
            """
        )

        # Display any existing training listings or functionality
        show_trainings()

    with tab2:
        prices.show()  # Calls the Pricing Page

    with tab3:
        show_certificate_database()
