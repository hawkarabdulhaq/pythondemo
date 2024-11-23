import streamlit as st
import pandas as pd
from github import Github
from io import StringIO

# Define paths and constants
CSV_FILE_PATH = "translations/csv/master_translation.csv"
GITHUB_REPO = "hawkarabdulhaq/pythondemo"
CSV_GITHUB_PATH = "translations/csv/master_translation.csv"
ACCESS_CODE = "demo2024"  # Define your access code here

# Authenticate with GitHub
def authenticate_github():
    """Authenticate with GitHub using the token from secrets."""
    try:
        token = st.secrets["github_token"]  # Token stored in secrets.toml
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
        return pd.read_csv(StringIO(csv_data))
    except Exception as e:
        st.error(f"Error loading translations from GitHub: {e}")
        st.exception(e)
        return pd.DataFrame()

# Save translations back to the GitHub repository
def save_translations_to_github(updated_df):
    """Save the updated translations to the GitHub repository."""
    try:
        g = authenticate_github()
        if g is None:
            st.sidebar.error("GitHub authentication failed.")
            return
        repo = g.get_repo(GITHUB_REPO)
        
        # Fetch the latest file contents to get the latest sha
        contents = repo.get_contents(CSV_GITHUB_PATH)
        
        # Convert DataFrame back to CSV format
        csv_data = updated_df.to_csv(index=False)
        
        # Update the file in the repository
        commit_message = "Updated translations via Streamlit app"
        update_response = repo.update_file(
            path=CSV_GITHUB_PATH,
            message=commit_message,
            content=csv_data,
            sha=contents.sha,
            branch="main"  # Replace with the correct branch name
        )
        st.sidebar.success("Translations updated successfully on GitHub!")
        st.sidebar.write(f"Update response: {update_response}")
    except Exception as e:
        st.sidebar.error(f"Error saving translations to GitHub: {e}")
        st.exception(e)

# Authentication for access
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("Authentication Required")
    code = st.text_input("Enter Access Code", type="password")
    if st.button("Submit"):
        if code == ACCESS_CODE:
            st.session_state.authenticated = True
            st.success("Access granted!")
            st.rerun()
        else:
            st.error("Incorrect access code. Please try again.")
else:
    # Test GitHub Access
    test_github_access()
    
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
            en_value = col1.text_area(
                "English",
                value=row["EN"],
                height=100,  # Adjust height if needed
                key=f"{row['Key']}_EN_{index}"  # Unique key
            )
            ku_value = col2.text_area(
                "Kurdish",
                value=row["KU"],
                height=100,  # Adjust height if needed
                key=f"{row['Key']}_KU_{index}"  # Unique key
            )
            updated_translations.append({"Key": row["Key"], "EN": en_value, "KU": ku_value})
    
        # Add Save button to the sidebar
        def on_save_click():
            updated_df = pd.DataFrame(updated_translations)
            st.write("Updated DataFrame:")
            st.dataframe(updated_df)
            save_translations_to_github(updated_df)
    
        st.sidebar.title("Save Changes")
        st.sidebar.button("Save Translations", on_click=on_save_click)
    else:
        st.error("No translations found in the GitHub repository. Please check your configuration.")
