# enrollment.py
import streamlit as st
import gspread
import price  # Import price for displaying pricing information
import discounts  # Import discounts for displaying discount information
from google.oauth2.service_account import Credentials

# Function to connect to Google Sheets
def connect_to_google_sheet(sheet_name):
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(st.secrets["spreadsheet"]["sheet_id"])
    return sheet.worksheet(sheet_name)

def show():
    st.markdown('<div class="title">Enrollment</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content">
            If you would like to enroll in the course, please select your preferred training type below and review the pricing and discounts. Once you decide, complete the enrollment form as directed. You will receive a bill with payment instructions after submission.
        </div>
    """, unsafe_allow_html=True)

    # Tabs for Prices and Discounts
    tab1, tab2 = st.tabs(["Prices", "Discounts"])

    # Prices Tab
    with tab1:
        price.show()  # Display pricing options from price.py

    # Discounts Tab
    with tab2:
        discounts.show()  # Display discounts content from discounts.py
