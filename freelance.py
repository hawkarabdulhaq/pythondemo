import streamlit as st
import pandas as pd

def show():
    st.title("💼 Freelance Opportunities")
    st.write("Explore the latest freelance opportunities available. Below are detailed listings for you to consider.")

    # Load freelance opportunities from CSV
    try:
        # Update the path to your CSV file if necessary
        df = pd.read_csv("input/freelance_opportunities.csv")
    except FileNotFoundError:
        st.error("The opportunities file is missing. Please ensure the `freelance_opportunities.csv` file exists in the `input` directory.")
        return

    # Check if the CSV contains the required columns
    required_columns = {"title", "description", "requirements", "deliverables", "timeline", "budget", "type", "location", "contact"}
    if not required_columns.issubset(df.columns):
        st.error("The CSV file does not contain the required columns. Please check the file format.")
        return

    # Iterate over rows in the DataFrame and display opportunities as cards
    for _, row in df.iterrows():
        st.markdown(
            f"""
            <div style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f9f9f9;">
                <h4 style="color: #1abc9c;">{row['title']}</h4>
                <p><strong>Description:</strong> {row['description']}</p>
                <p><strong>Requirements:</strong> {row['requirements']}</p>
                <p><strong>Deliverables:</strong> {row['deliverables']}</p>
                <p><strong>Timeline:</strong> {row['timeline']}</p>
                <p><strong>Budget:</strong> {row['budget']}</p>
                <p><strong>Type:</strong> {row['type']}</p>
                <p><strong>Location:</strong> {row['location']}</p>
                <div style="text-align: center; margin-top: 20px;">
                    <a href="{row['contact']}" target="_blank" style="background-color: #28a745; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Apply</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Optional footer with instructions
    st.markdown(
        """
        ---
        **Need help or have questions?** Reach out to us at [connect@habdulhaq.com](mailto:connect@habdulhaq.com).
        """
    )
