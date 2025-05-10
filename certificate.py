import streamlit as st
import base64
import pandas as pd
import os

# GitHub raw base URL
GITHUB_BASE_URL = "https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/"

def show():
    """Display the Certificate Database page."""
    st.title("🎓 Certificate Database")

    # Load the certificate CSV
    try:
        df = pd.read_csv("input/certificate.csv")
    except FileNotFoundError:
        st.error("Certificate database file not found.")
        return

    # Filter: only show entries with a completion date
    completed_df = df[df["date of completion"].notna() & (df["date of completion"] != "")]

    if completed_df.empty:
        st.info("No participants have completed the course yet.")
    else:
        for _, participant in completed_df.iterrows():
            st.markdown(f"### {participant['name']}")
            col1, col2 = st.columns([1, 2])

            with col1:
                st.write(f"**Name:** {participant['name']}")
                st.write(f"**Date of Joining:** {participant['date of joining']}")
                st.write(f"**Date of Completion:** {participant['date of completion']}")
                st.write(f"**Credential:** {participant['credential']}")

            with col2:
                cert_path = str(participant["certificate"])

                if cert_path.startswith("certificates/"):
                    cert_url = GITHUB_BASE_URL + cert_path
                    st.image(cert_url, caption="Certificate", use_container_width=True)
                elif os.path.exists(cert_path):
                    st.image(cert_path, caption="Certificate", use_container_width=True)
                else:
                    st.warning(f"Certificate not found: {cert_path}")

            st.markdown("---")  # Divider between entries
