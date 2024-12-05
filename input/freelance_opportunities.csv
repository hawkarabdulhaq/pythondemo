import streamlit as st
import pandas as pd

def show():
    st.title("Freelance Opportunities")
    st.write("Explore the latest freelance opportunities available. Click on an opportunity to see full details.")

    # Load freelance opportunities from CSV
    try:
        # Update the path to your CSV file if necessary
        df = pd.read_csv("input/freelance_opportunities.csv")
    except FileNotFoundError:
        st.error("The opportunities file is missing. Please upload the `freelance_opportunities.csv` file.")
        return

    # Check if the CSV contains the required columns
    required_columns = {"title", "description", "requirements", "deliverables", "timeline", "budget", "contact"}
    if not required_columns.issubset(df.columns):
        st.error("The CSV file does not contain the required columns.")
        return

    # Iterate over rows in the DataFrame and display opportunities
    for _, row in df.iterrows():
        with st.expander(row["title"]):  # Collapsible section for each opportunity
            st.markdown(f"**Description:** {row['description']}")
            st.markdown(f"**Requirements:** {row['requirements']}")
            st.markdown(f"**Deliverables:** {row['deliverables']}")
            st.markdown(f"**Timeline:** {row['timeline']}")
            st.markdown(f"**Budget:** {row['budget']}")
            st.markdown(f"**Contact:** [Email Us](mailto:{row['contact']})")

    # Optionally add an upload feature for CSV
    uploaded_file = st.file_uploader("Update Freelance Opportunities", type="csv")
    if uploaded_file:
        try:
            new_df = pd.read_csv(uploaded_file)
            # Validate the uploaded file
            if required_columns.issubset(new_df.columns):
                new_df.to_csv("input/freelance_opportunities.csv", index=False)
                st.success("Opportunities updated successfully!")
            else:
                st.error("The uploaded CSV does not have the required columns.")
        except Exception as e:
            st.error(f"Error reading the uploaded file: {e}")

