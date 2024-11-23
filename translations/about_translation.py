import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets configuration
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SHEET_ID = "1BHQV2bmeSMMhmjdzajjH6A_FwnBMEqq3G6PqqM2fmMQ"  # Your sheet's ID
TAB_NAME = "about_translation.py"  # Tab name in the Google Sheet

def fetch_translations():
    """
    Fetch translations from the specified Google Sheet tab and return as a dictionary.
    """
    try:
        # Authenticate using st.secrets
        credentials = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"], scopes=SCOPES
        )
        client = gspread.authorize(credentials)

        # Open the Google Sheet and the specific tab
        sheet = client.open_by_key(SHEET_ID)
        worksheet = sheet.worksheet(TAB_NAME)

        # Fetch all rows from the sheet
        data = worksheet.get_all_values()

        # Process the data
        headers = data[0]  # First row contains headers
        rows = data[1:]  # Remaining rows contain translation data

        translations = {}
        for row in rows:
            if not row or not row[0].strip():
                continue  # Skip empty rows or rows without a key

            key = row[0].strip()  # Key column
            en_value = row[1].strip() if len(row) > 1 else ""  # English translation
            ku_value = row[2].strip() if len(row) > 2 else ""  # Kurdish translation

            translations[key] = {
                "EN": en_value,
                "KU": ku_value,
            }

        return translations

    except Exception as e:
        st.error(f"Error fetching translations: {e}")
        st.exception(e)
        return {}

# Fetch translations and assign to the variable without changing its name
about_translations = fetch_translations()

# For debugging: display the translations
st.write("about_translations:", about_translations)
