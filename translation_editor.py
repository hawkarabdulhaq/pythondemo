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
    """Authenticate with GitHub using the token from .streamlit/secrets.toml."""
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
        st.sidebar.info("Loading translations from GitHub...")
        g = authenticate_github()
        if g is None:
            return pd.DataFrame()
        repo = g.get_repo(GITHUB_REPO)
        file_content = repo.get_contents(CSV_GITHUB_PATH)
        csv_data = file_content.decoded_content.decode("utf-8")
        st.sidebar.success("Translations loaded successfully!")
        return pd.read_csv(StringIO(csv_data))
    except Exception as e:
        st.error(f"Error loading translations from GitHub: {e}")
        return pd.DataFrame()

# Save translations back to the GitHub repository
def save_translations_to_github(updated_df):
    """Save the updated translations to the GitHub repository."""
    try:
        st.sidebar.info("Saving translations to GitHub...")
        g = authenticate_github()
        if g is None:
            return
        repo = g.get_repo(GITHUB_REPO)

        # Fetch the latest file content to get the correct SHA
        file_content = repo.get_contents(CSV_GITHUB_PATH)
        latest_csv_data = file_content.decoded_content.decode("utf-8")
        latest_df = pd.read_csv(StringIO(latest_csv_data))

        # Merge updated_df with latest_df to ensure no conflicts
        merged_df = updated_df.copy()

        # Convert DataFrame back to CSV format
        csv_data = merged_df.to_csv(index=False, encoding="utf-8")

        # Commit the updated file to GitHub
        commit_response = repo.update_file(
            path=CSV_GITHUB_PATH,
            message="Updated translations via Streamlit app",
            content=csv_data,
            sha=file_content.sha,  # Required to identify the file version being updated
        )

        st.sidebar.success("Translations updated successfully on GitHub!")
        st.sidebar.write("Updated CSV Preview:")
        st.sidebar.dataframe(updated_df)  # Show the updated DataFrame as confirmation
        print(f"Commit Response: {commit_response}")  # Log the commit response for debugging
    except Exception as e:
        st.sidebar.error(f"Error saving translations to GitHub: {e}")
        print(f"Error Details: {e}")

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
            st.experimental_rerun()
        else:
            st.error("Incorrect access code. Please try again.")
else:
    # Load translations into a DataFrame
    df = load_translations_from_github()

    # Display the app title
    st.title("Translation Management")

    if not df.empty:
        # Initialize updated_translations in session state if not already
        if "updated_translations" not in st.session_state:
            st.session_state.updated_translations = df.to_dict('records')

        st.markdown("### Edit Translations Below")

        # Display translations and collect updates
        for index, row in enumerate(st.session_state.updated_translations):
            st.write(f"**{row['Key']}**")
            col1, col2 = st.columns(2)
            en_value = col1.text_area(
                "English",
                value=row["EN"],
                height=100,
                key=f"{row['Key']}_EN_{index}"
            )
            ku_value = col2.text_area(
                "Kurdish",
                value=row["KU"],
                height=100,
                key=f"{row['Key']}_KU_{index}"
            )
            # Update the values in session_state
            st.session_state.updated_translations[index]["EN"] = en_value
            st.session_state.updated_translations[index]["KU"] = ku_value

        # Add Save button to the sidebar
        def on_save_click():
            updated_df = pd.DataFrame(st.session_state.updated_translations)
            save_translations_to_github(updated_df)

        st.sidebar.title("Save Changes")
        st.sidebar.button("Save Translations", on_click=on_save_click)
    else:
        st.error("No translations found in the GitHub repository. Please check your configuration.")
