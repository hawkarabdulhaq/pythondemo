import streamlit as st

def show():
    # Title
    st.markdown("### Discount Opportunities")
    
    # Description and Discount Details
    st.markdown("""
        Take advantage of our discount options to make learning more affordable and rewarding!
        
        - **Earn Discounts with Friend Referrals**: Invite a friend, and they receive a **15% discount** on the course fee. You also receive a **15% discount** as a thank-you!
        - **Refer Three, Get Your Course Free**: Successfully refer three friends who enroll in the course, and your entire course fee will be **completely waived**.
        - **Student Discount for 3rd and 4th-Year Students**: If you're a 3rd or 4th-year student, you’re eligible for an **80% discount** on the total course price.
    """)

    # Contact Information
    st.markdown("""
        For more information, reach out to us at [connect@habdulhaq.com](mailto:connect@habdulhaq.com).
    """)

# Display content on the Streamlit page
show()
