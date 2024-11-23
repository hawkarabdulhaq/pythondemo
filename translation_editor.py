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

# Display the app title
st.title("Translation Management")

if not df.empty:
    # Create editable table for translations
    st.markdown("### Edit Translations Below")
    updated_translations = []

    for index, row in df.iterrows():
        st.write(f"**{row['Key']}**")
        col1, col2 = st.columns(2)
        en_value = col1.text_input("English", value=row["EN"], key=f"{row['Key']}_EN")
        ku_value = col2.text_input("Kurdish", value=row["KU"], key=f"{row['Key']}_KU")
        updated_translations.append({"Key": row["Key"], "EN": en_value, "KU": ku_value})

    # Save button with callback
    def on_save_click():
        updated_df = pd.DataFrame(updated_translations)
        save_translations_csv(updated_df)

    st.button("Save Changes", on_click=on_save_click)

else:
    st.error("No translations found in the CSV file. Please upload a valid file.")
