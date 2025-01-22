import streamlit as st

def show():
    # Welcome section
    st.markdown("""
    <div class="title" style="text-align: center; font-size: 2.5em; font-weight: bold; color: #1ABC9C; margin-top: 20px;">
        Learn AI and Machine Learning Faster and Smarter
    </div>
    <div class="subtitle" style="text-align: center; font-size: 1.2em; color: #2C3E50; margin-top: 10px;">
        Empower your business with cutting-edge skills and insights!
    </div>
    <hr style="margin-top: 20px; margin-bottom: 20px; border: none; border-top: 2px solid #1ABC9C;">
    """, unsafe_allow_html=True)

    # Perfect for beginners section
    st.markdown("""
    <div style="text-align: center; font-size: 1.2em; font-weight: bold; color: #2C3E50; margin-bottom: 20px;">
        Perfect for Beginners and Professionals Alike!
    </div>
    """, unsafe_allow_html=True)

    # What We Offer Section
    st.markdown("""
    <div class="section-title" style="text-align: center; font-size: 2em; font-weight: bold; color: #1ABC9C; margin-bottom: 20px;">
        What We Offer
    </div>
    <div style="display: flex; justify-content: space-around; text-align: center; margin-bottom: 30px;">
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); width: 30%;">
            <h3 style="color: #34495E;">Training</h3>
            <p>Learn AI, Machine Learning, and Automation quickly and effectively.</p>
        </div>
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); width: 30%;">
            <h3 style="color: #34495E;">Analysis</h3>
            <p>We analyze your business and provide a custom data-driven improvement plan.</p>
        </div>
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); width: 30%;">
            <h3 style="color: #34495E;">Solutions</h3>
            <p>Custom-built tools to solve problems and streamline your operations.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Call-to-Action Button
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <a href="#" style="background-color: #1ABC9C; color: white; padding: 15px 30px; font-size: 1.2em; font-weight: bold; text-decoration: none; border-radius: 5px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);">
            Get Started Now
        </a>
    </div>
    """, unsafe_allow_html=True)
