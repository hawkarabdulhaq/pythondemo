import streamlit as st

def show():
    """Display the Contact page."""
    
    # Page Title
    st.title("Contact Us")
    
    # Contact Information Section
    st.markdown("""
    <div style="margin-top: 20px; font-size: 1.2em; color: #1ABC9C; text-align: center;">
        <p>We'd love to hear from you!</p>
        <p><strong>Email:</strong> <a href="mailto:ha@releafs.co" target="_blank" style="color: #1ABC9C;">ha@releafs.co</a></p>
        <p><strong>Phone:</strong> +123 456 789</p>
    </div>
    """, unsafe_allow_html=True)

    # Booking Section
    st.markdown("""
    <div style="margin-top: 40px; text-align: center; font-size: 1.1em;">
        <p><strong>Schedule a Meeting:</strong></p>
        <p><a href="https://calendly.com/hawkar_abdulhaq/introduction-to-coding-training-with-hawkar" target="_blank" 
        style="background-color: #1ABC9C; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;">Book a Demo</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Address Section
    st.markdown("""
    <div style="margin-top: 40px; text-align: center; font-size: 1.1em;">
        <p><strong>Our Office:</strong></p>
        <p>Releafs Co.</p>
        <p>Szeged, Hungary</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Social Media Links
    st.markdown("""
    <div style="margin-top: 50px; text-align: center; font-size: 1.1em;">
        <p>Follow us on:</p>
        <a href="https://www.linkedin.com" target="_blank" style="margin-right: 10px;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/linkedin.png" width="40">
        </a>
        <a href="https://twitter.com" target="_blank" style="margin-right: 10px;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/twitter.png" width="40">
        </a>
        <a href="https://www.facebook.com" target="_blank">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/facebook.png" width="40">
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer Note
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        releafs.co © 2024
    </div>
    """, unsafe_allow_html=True)
