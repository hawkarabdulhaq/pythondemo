import streamlit as st
import home
import gallery
import learning_platform
import enrollment
import demo_booking  # Import the demo booking script

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

# Sidebar Navigation using Buttons
with st.sidebar:
    st.title("Navigation")
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Gallery", on_click=set_page, args=("Gallery",))
    st.button("Learning Platform", on_click=set_page, args=("Learning Platform",))
    st.button("Enrollment", on_click=set_page, args=("Enrollment",))
    st.button("Demo Session", on_click=set_page, args=("Demo Session",))  # New Demo Session tab

    # Contact Information
    st.markdown("""
        <div style="margin-top: 30px; font-size: 1.1em; color: #2C3E50;">
            <p><strong>Contact:</strong></p>
            <p>Email: <a href="mailto:connect@habdulhaq.com" target="_blank" style="color: #1ABC9C;">connect@habdulhaq.com</a></p>
            <p>Website: <a href="https://www.habdulhaq.com" target="_blank" style="color: #1ABC9C;">www.habdulhaq.com</a></p>
        </div>
    """, unsafe_allow_html=True)

# Display the selected page content
if st.session_state.page == "Home":
    home.show()
elif st.session_state.page == "Gallery":
    gallery.show()
elif st.session_state.page == "Learning Platform":
    learning_platform.show()
elif st.session_state.page == "Enrollment":
    enrollment.show()
elif st.session_state.page == "Demo Session":
    demo_booking.show()  # Display the Demo Session page
