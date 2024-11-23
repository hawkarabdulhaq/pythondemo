import streamlit as st
import csv
import os
import pandas as pd

# Path to the CSV file
TRANSLATION_CSV_PATH = os.path.join("translations", "csv", "master_translation.csv")

# Load CSV into a DataFrame
@st.cache_data
def load_translations_csv():
    """Load translations from the master CSV file into a DataFrame."""
    try:
        return pd.read_csv(TRANSLATION_CSV_PATH, encoding="utf-8")
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
        return pd.DataFrame()

# Save the updated DataFrame back to CSV
def save_translations_csv(df):
    """Save updated translations back to the CSV file."""
    try:
        df.to_csv(TRANSLATION_CSV_PATH, index=False, encoding="utf-8")
        st.success("Translations have been saved successfully!")
    except Exception as e:
        st.error(f"Error saving CSV file: {e}")
        st.exception(e)

# Initialize app state
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# Load translations
translations_df = load_translations_csv()

# Sidebar Navigation
st.sidebar.title("Translation Management")
st.sidebar.markdown("### Select a category to edit:")
if not translations_df.empty:
    categories = translations_df["Key"].str.split("_", expand=True)[0].unique()
    for category in categories:
        if st.sidebar.button(category):
            st.session_state.selected_category = category

# Main Content
if st.session_state.selected_category:
    category = st.session_state.selected_category
    st.title(f"Editing Translations for Category: {category}")

    # Filter translations for the selected category
    category_df = translations_df[translations_df["Key"].str.startswith(category)].copy()

    if not category_df.empty:
        updated_translations = []

        # Display translations in a table
        st.markdown("### Translation Table")
        for idx, row in category_df.iterrows():
            key = row["Key"]
            st.write(f"**{key}**")
            col1, col2 = st.columns([1, 1])
            col1.text_input("English", value=row["EN"], disabled=True, key=f"{key}_EN")
            new_kurdish = col2.text_input("Kurdish", value=row["KU"], key=f"{key}_KU")
            updated_translations.append({"Key": key, "EN": row["EN"], "KU": new_kurdish})

        # Save button with callback
        def on_save_click():
            updated_df = pd.DataFrame(updated_translations)
            save_translations_csv(updated_df)

        st.button("Save Changes", on_click=on_save_click)
    else:
        st.error(f"No translations found for the selected category: {category}")
else:
    st.title("Welcome to the Translation Management Tool")
    st.markdown("""
    This tool allows you to manage translations for your app.
    - Select a category from the sidebar to start editing.
    - Edit Kurdish translations and save your changes.
    """)

