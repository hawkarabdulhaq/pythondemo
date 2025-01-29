import streamlit as st

def show():
    # Banner Section with Image Background
    st.markdown(f"""
    <div style="
        position: relative;
        text-align: center;
        color: White;
        height: 300px;
        background-image: url('https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/waves.jpg');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    ">
        <h1 style="margin: 0; font-size: 2.5em; font-weight: bold;">Utilize AI and Machine Learning Faster and Smarter</h1>
        <p style="margin-top: 10px; font-size: 1.2em;">Transform your business into a data-driven, more resilient enterprise with us!</p>
    </div>
    <hr style="margin: 30px 0; border: none; border-top: 2px solid #1ABC9C;">
    """, unsafe_allow_html=True)

    # Subtitle
    st.markdown("""
    <div style="text-align: center; font-size: 1.5em; font-weight: bold; color: #34495E; margin-bottom: 20px;">
        Perfect for Beginners and Professionals Alike!
    </div>
    """, unsafe_allow_html=True)

    # What We Offer Section
    st.markdown("""
    <div style="text-align: center; font-size: 2em; font-weight: bold; color: #1ABC9C; margin-bottom: 20px;">
        What We Offer
    </div>
    """, unsafe_allow_html=True)

    # Offer Details
    st.markdown("""
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
        <div style="background-color: ##000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg" alt="Training" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #34495E;">Training</h3>
            <p>Learn AI, Machine Learning, and Automation quickly and effectively.</p>
        </div>
        <div style="background-color: ##000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg" alt="Analysis" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #34495E;">Analysis</h3>
            <p>We analyze your business and provide a custom data-driven improvement plan.</p>
        </div>
        <div style="background-color: ##000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg" alt="Solutions" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #34495E;">Solutions</h3>
            <p>Custom-built tools to solve problems and streamline your operations.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
