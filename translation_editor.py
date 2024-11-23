import streamlit as st
import pandas as pd
import os

# Define paths
CSV_FILE_PATH = "translations/csv/master_translation.csv"

# Function to load translations from the CSV file
def load_translations_csv():
    """Load translations from the master CSV file."""
    try:
        if not os.path.exists(CSV_FILE_PATH):
            st.error("Translation CSV file not found!")
            return pd.DataFrame()
        return pd.read_csv(CSV_FILE_PATH)
    except Exception as e:
        st.error(f"Error loading translations: {e}")
        return pd.DataFrame()

# Function to save updated translations to the CSV file
def save_translations_csv(updated_df):
    """Save the updated translations to the master CSV file."""
    try:
        updated_df.to_csv(CSV_FILE_PATH, index=False, encoding="utf-8")
        st.success("Translations saved successfully!")
    except Exception as e:
        st.error(f"Error saving translations: {e}")

# Load translations into a DataFrame
df = load_translations_csv()

# Initialize App State
if "selected_key" not in st.session_state:
    st.session_state.selected_key = None

# Sidebar Navigation
st.sidebar.title("Translation Management")
st.sidebar.markdown("### Select a key to edit:")

if not df.empty:
    # Create a list of keys to choose from
    keys = df["Key"].tolist()
    selected_key = st.sidebar.selectbox("Select a key", options=keys)
    st.session_state.selected_key = selected_key

    # Main Content
    if st.session_state.selected_key:
        st.title(f"Editing Translation for Key: {st.session_state.selected_key}")

        # Get the row corresponding to the selected key
        row = df[df["Key"] == st.session_state.selected_key].iloc[0]

        # Display translations
        st.markdown("### Translation")
        col1, col2 = st.columns([1, 1])

        # Use unique keys for text_input widgets
        col1.text_input(
            "English",
            value=row["EN"],
            disabled=True,
            key=f"{row['Key']}_EN"
        )
        new_kurdish = col2.text_input(
            "Kurdish",
            value=row["KU"],
            key=f"{row['Key']}_KU"
        )

        # Save button with callback
        def on_save_click():
            # Update the DataFrame with the new Kurdish translation
            df.loc[df["Key"] == row["Key"], "KU"] = new_kurdish
            save_translations_csv(df)

        st.button("Save Changes", on_click=on_save_click)
else:
    st.title("Welcome to the Translation Management Tool")
    st.markdown("""
    This tool allows you to manage translations for your app.
    - Select a key from the sidebar to start editing.
    - Edit the Kurdish translation and save your changes.
    """)

