import streamlit as st
import gspread
import price  # Make sure price.py is correctly imported
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
    st.markdown('<div class="content">If you would like to enroll in the course, please select your preferred training type below and complete the enrollment form. Once submitted, you will receive a bill with payment instructions.<br><br>This course is hosted on an online platform and includes a weekly live session, giving you the opportunity for one-on-one learning. You should plan for approximately <strong>one hour per week</strong> for the live session, along with <strong>2 to 3 hours</strong> for completing assignments and following the course material.</div>', unsafe_allow_html=True)

    # Tabs for Prices, Individual Training, and Group Training
    tab1, tab2, tab3 = st.tabs(["Prices", "Individual Training", "Group Training"])

    # Prices Tab
    with tab1:
        st.markdown('<div class="section-title">Course Pricing Options</div>', unsafe_allow_html=True)
        price.show()  # Display pricing options from price.py

    # Individual Training Tab
    with tab2:
        st.markdown('<div class="section-title">Individual Training Enrollment</div>', unsafe_allow_html=True)
        
        with st.form("individual_training_form"):
            # Basic Information
            st.write("### Personal Information")
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=0, max_value=120, step=1)
            job = st.text_input("Job")
            email = st.text_input("Email")
            location = st.text_input("Location")
            gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

            # Course Discovery
            st.write("### How did you hear about the course?")
            course_discovery = st.selectbox("Select one", ["Telegram", "YouTube", "Facebook", "Search", "Friend"])

            # Payment Method
            st.write("### Preferred Payment Method")
            payment_method = st.selectbox("Choose your payment method", ["FIB", "Paypal", "Revolut"])

            # Agreement
            st.write("### Agreement")
            st.write("I confirm that I want to participate in the One-on-One session. I understand the payment is **395,000 IQD**.")
            individual_agreement = st.checkbox("I agree to the terms in the [Terms and Conditions](https://docs.google.com/document/d/1K-WNovtVP7EPylKVyHc6rGCXMGjw-eFwkaNLO2noiPE/edit?usp=sharing).")

            # Form Submission
            individual_submit_button = st.form_submit_button("Submit Individual Enrollment")

        # Process Individual Training Submission
        if individual_submit_button:
            if not individual_agreement:
                st.warning("Please agree to the terms to proceed with the Individual Training enrollment.")
            else:
                # Save to Google Sheet
                sheet = connect_to_google_sheet("one")
                sheet.append_row([name, age, job, email, location, gender, course_discovery, payment_method])
                st.success("Thank you for your enrollment request! You will receive a bill shortly with payment instructions.")

    # Group Training Tab
    with tab3:
        st.markdown('<div class="section-title">Group Training Enrollment</div>', unsafe_allow_html=True)

        with st.form("group_training_form"):
            # Basic Information
            st.write("### Personal Information")
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=0, max_value=120, step=1)
            job = st.text_input("Job")
            email = st.text_input("Email")
            location = st.text_input("Location")
            gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

            # Course Discovery
            st.write("### How did you hear about the course?")
            course_discovery = st.selectbox("Select one", ["Telegram", "YouTube", "Facebook", "Website", "Friend"])

            # Group Details
            st.write("### Group Details")
            group_size = st.selectbox("How many people are in your group?", [3, 4, 5, 6])
            group_names = st.text_area("Please enter the names of all group members (one name per line):")

            # Payment Method
            st.write("### Preferred Payment Method")
            payment_method = st.selectbox("Choose your payment method", ["FIB", "Paypal", "Revolut"])

            # Agreement
            st.write("### Agreement")
            st.write("I confirm that this is a Group Session enrollment for three or more colleagues. I understand the payment is **295,000 IQD per person**.")
            group_representative_agreement = st.checkbox("I confirm that I am representing the group.")
            group_terms_agreement = st.checkbox("I agree to the terms in the [Terms and Conditions](https://docs.google.com/document/d/1K-WNovtVP7EPylKVyHc6rGCXMGjw-eFwkaNLO2noiPE/edit?usp=sharing).")

            # Form Submission
            group_submit_button = st.form_submit_button("Submit Group Enrollment")

        # Process Group Training Submission
        if group_submit_button:
            if not group_representative_agreement:
                st.warning("Please confirm that you are representing the group.")
            elif not group_terms_agreement:
                st.warning("Please agree to the terms to proceed with the Group Training enrollment.")
            elif group_size and not group_names:
                st.warning("Please enter the names of all group members.")
            else:
                # Save to Google Sheet
                sheet = connect_to_google_sheet("group")
                sheet.append_row([name, age, job, email, location, gender, course_discovery, group_size, group_names, payment_method])
                st.success("Thank you for your enrollment request! You will receive a bill shortly with payment instructions.")
