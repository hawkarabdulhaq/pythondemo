import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Function to connect to Google Sheets
def connect_to_google_sheet(sheet_name):
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(st.secrets["spreadsheet"]["sheet_id"])
    return sheet.worksheet(sheet_name)

def show():
    # Enrollment section
    st.markdown('<div class="title">Enrollment</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content">
            Join our courses today and take the first step towards mastering new skills and achieving your goals.
        </div>
    """, unsafe_allow_html=True)

    # Content about enrollment
    st.markdown("""
    <div class="content">
        Here are the steps to enroll in our program:
        <ul>
            <li>Browse through the available courses.</li>
            <li>Sign up using our online form.</li>
            <li>Start your journey with us.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
