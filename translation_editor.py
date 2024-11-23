import streamlit as st
import pandas as pd
import os
from github import Github  # PyGithub library for interacting with GitHub
from io import StringIO  # Correct StringIO import

# Define paths and constants
CSV_FILE_PATH = "translations/csv/master_translation.csv"
GITHUB_REPO = "hawkarabdulhaq/pythondemo"
CSV_GITHUB_PATH = "translations/csv/master_translation.csv"

# Authenticate with GitHub
def authenticate_github():
    """Authenticate with GitHub using the token from .streamlit/config.toml."""
    try:
        token = st.secrets["github_token"]  # Token stored in .streamlit/secrets.toml
        return Github(token)
    except KeyError:
        st.error("GitHub token not found in secrets!")
        return None

# Load translations from the GitHub repository
def load_translations_from_github():
    """Load translations CSV from the GitHub repository."""
    try:
        g = authenticate_github()
        if g is None:
            return pd.DataFrame()
        repo = g.get_repo(GITHUB_REPO)
        file_content = repo.get_contents(CSV_GITHUB_PATH)
        csv_data = file_content.decoded_content.decode("utf-8")
        return pd.read_csv(StringIO(csv_data))  # Corrected StringIO usage
    except Exception as e:
        st.error(f"Error loading translations from GitHub: {e}")
        return pd.DataFrame()

# Save translations back to the GitHub repository
def save_translations_to_github(updated_df):
    """Save the updated translations to the GitHub repository."""
    try:
        g = authenticate_github()
        if g is None:
            return
        repo = g.get_repo(GITHUB_REPO)
        file_content = repo.get_contents(CSV_GITHUB_PATH)

        # Convert DataFrame back to CSV format
        csv_data = updated_df.to_csv(index=False, encoding="utf-8")

        # Commit the updated file to GitHub
        repo.update_file(
            path=CSV_GITHUB_PATH,
            message="Updated translations via Streamlit app",
            content=csv_data,
            sha=file_content.sha,  # Required to identify the file version being updated
        )
        st.success("Translations updated successfully on GitHub!")
    except Exception as e:
        st.error(f"Error saving translations to GitHub: {e}")

# Load translations into a DataFrame
df = load_translations_from_github()

# Display the app title
st.title("Translation Management")

if not df.empty:
    # Create editable table for translations
    st.markdown("### Edit Translations Below")
    updated_translations = []

    for index, row in df.iterrows():
        st.write(f"**{row['Key']}**")
        col1, col2 = st.columns(2)
        en_value = col1.text_input(
            "English",
            value=row["EN"],
            key=f"{row['Key']}_EN_{index}"  # Unique key
        )
        ku_value = col2.text_input(
            "Kurdish",
            value=row["KU"],
            key=f"{row['Key']}_KU_{index}"  # Unique key
        )
        updated_translations.append({"Key": row["Key"], "EN": en_value, "KU": ku_value})

    # Save button with callback
    def on_save_click():
        updated_df = pd.DataFrame(updated_translations)
        save_translations_to_github(updated_df)

    st.button("Save Changes", on_click=on_save_click)

else:
    st.error("No translations found in the GitHub repository. Please check your configuration.")
