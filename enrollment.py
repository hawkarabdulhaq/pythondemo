import streamlit as st

def show():
    st.markdown('<div class="title">Enrollment</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">If you want to participate in the course, please complete the enrollment form below. Once submitted, you will receive a bill with the payment instructions.</div>', unsafe_allow_html=True)

    # Enrollment Form
    with st.form("enrollment_form"):
        # Basic Information
        st.write("### Personal Information")
        name = st.text_input("Name")
        email = st.text_input("Email")
        location = st.text_input("Location")
        gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

        # Course Discovery
        st.write("### How did you hear about the course?")
        course_discovery = st.selectbox("Select one", ["Telegram", "YouTube", "Facebook", "Website", "Friend"])

        # Enrollment Options
        st.write("### Enrollment Type")
        enrollment_type = st.radio("Choose your enrollment type", ["One-on-One Session", "Group Session (3+ people)"])

        # Conditional Agreement Statements Based on Enrollment Type
        if enrollment_type == "One-on-One Session":
            st.write("I confirm that I want to participate in the One-on-One session. I understand the payment is **435,000 IQD**.")
            one_on_one_agreement = st.checkbox("I agree to the terms above.")
        elif enrollment_type == "Group Session (3+ people)":
            st.write("I confirm that this is a Group Session enrollment for three or more colleagues. I understand the payment is **315,000 IQD per person**.")
            st.write("Please enter your group's name below.")
            group_name = st.text_input("Group Name")
            group_agreement = st.checkbox("I agree to the terms above.")

        # Form Submission
        submit_button = st.form_submit_button("Submit Enrollment")

    # Processing the Form Submission
    if submit_button:
        if enrollment_type == "One-on-One Session" and not one_on_one_agreement:
            st.warning("Please agree to the terms to proceed with the One-on-One Session enrollment.")
        elif enrollment_type == "Group Session (3+ people)" and not group_agreement:
            st.warning("Please agree to the terms to proceed with the Group Session enrollment.")
        else:
            st.success("Thank you for your enrollment request! You will receive a bill shortly with payment instructions.")
