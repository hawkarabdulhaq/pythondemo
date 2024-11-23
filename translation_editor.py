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

# Check if the "Category" column exists
if "Category" not in df.columns:
    st.error(
        "The 'Category' column is missing in the master CSV file. "
        "Please add a 'Category' column and reload."
    )
else:
    # Initialize App State
    if "selected_category" not in st.session_state:
        st.session_state.selected_category = None

    # Sidebar Navigation
    st.sidebar.title("Translation Management")
    st.sidebar.markdown("### Select a category to edit:")
    categories = df["Category"].unique()

    # Create buttons for each category
    for category in categories:
        if st.sidebar.button(category):
            st.session_state.selected_category = category

    # Main Content
    if st.session_state.selected_category:
        selected_category = st.session_state.selected_category
        st.title(f"Editing Translations for: {selected_category}")
        
        # Filter rows by the selected category
        category_df = df[df["Category"] == selected_category].reset_index(drop=True)

        if not category_df.empty:
            updated_translations = []

            # Display translations in a table
            st.markdown("### Translation Table")
            for idx, row in category_df.iterrows():
                key = row["Key"]
                st.write(f"**{key}**")
                col1, col2 = st.columns([1, 1])
                
                # Use unique keys for text_input widgets
                col1.text_input(
                    "English",
                    value=row["EN"],
                    disabled=True,
                    key=f"{key}_EN_{idx}"  # Unique key
                )
                new_kurdish = col2.text_input(
                    "Kurdish",
                    value=row["KU"],
                    key=f"{key}_KU_{idx}"  # Unique key
                )
                updated_translations.append({"Category": selected_category, "Key": key, "EN": row["EN"], "KU": new_kurdish})

            # Save button with callback
            def on_save_click():
                updated_df = pd.DataFrame(updated_translations)
                save_translations_csv(updated_df)

            st.button("Save Changes", on_click=on_save_click)
        else:
            st.error("No translations found for this category.")
    else:
        st.title("Welcome to the Translation Management Tool")
        st.markdown("""
        This tool allows you to manage translations for your app.
        - Select a category from the sidebar to start editing.
        - Edit Kurdish translations and save your changes.
        """)
