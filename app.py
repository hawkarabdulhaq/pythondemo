import streamlit as st
import home
import testimony
import learning_platform
import enrollment

# Initialize session state for page tracking
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Function to update page state
def set_page(page):
    st.session_state.page = page

# Custom CSS for styling
st.markdown("""
    <style>
    /* Set the default font to Courier */
    * {
        font-family: "Courier", monospace;
    }
    
    /* Styling the title */
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #2C3E50;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    /* Styling for section titles */
    .section-title {
        font-size: 1.7em;
        font-weight: bold;
        color: #34495E;
        margin-top: 30px;
        margin-bottom: 10px;
        border-bottom: 2px solid #34495E;
        padding-bottom: 5px;
    }
    
    /* General content styling */
    .content {
        font-size: 1.1em;
        color: #2C3E50;
        line-height: 1.6;
        text-align: justify;
        margin-bottom: 20px;
    }

    /* Highlighting important sections */
    .highlight {
        font-weight: bold;
        color: #1ABC9C;
    }
    
    /* Style for video container */
    .video-container {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation with Course Title
with st.sidebar:
    st.title("Personalized Python Training")  # Course Title
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Testimonials", on_click=set_page, args=("Testimonials",))
    st.button("Learning Platform", on_click=set_page, args=("Learning Platform",))
    st.button("Enrollment", on_click=set_page, args=("Enrollment",))

    # Contact Information
    st.markdown("""
        <div style="margin-top: 30px; font-size: 1.1em; color: #2C3E50;">
            <p><strong>Contact:</strong></p>
            <p>Email: <a href="mailto:connect@habdulhaq.com" target="_blank" style="color: #1ABC9C;">connect@habdulhaq.com</a></p>
            <p>Website: <a href="https://www.habdulhaq.com" target="_blank" style="color: #1ABC9C;">www.habdulhaq.com</a></p>
        </div>
        <div style="margin-top: 20px; font-size: 1.1em;">
            <p><strong>Book a Free Demo Session:</strong></p>
            <p><a href="https://calendly.com/hawkar_abdulhaq/introduction-to-coding-training-with-hawkar" target="_blank" style="color: #1ABC9C;">Schedule a Demo on Calendly</a></p>
        </div>
    """, unsafe_allow_html=True)

# Display the selected page content
if st.session_state.page == "Home":
    home.show()
elif st.session_state.page == "Testimonials":
    testimony.show()
elif st.session_state.page == "Learning Platform":
    learning_platform.show()
elif st.session_state.page == "Enrollment":
    enrollment.show()
