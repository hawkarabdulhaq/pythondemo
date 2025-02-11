import streamlit as st
import requests

def show():
    # Fetch the SVG content from your GitHub repository
    svg_url = "https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/impact_wave.svg"
    response = requests.get(svg_url)
    if response.status_code == 200:
        svg_content = response.text
        st.markdown(svg_content, unsafe_allow_html=True)
    else:
        st.error("Failed to load the impact wave graphic.")

    # The rest of your Home page content remains unchanged

    # Subtitle
    st.markdown("""
    <div style="text-align: center; font-size: 1.5em; font-weight: bold; color: #eeeeee; margin-bottom: 20px;">
        Optimizing businesses for resilience and sustainable growth with AI!
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
        <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg" alt="Training" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #eeeeee;">Training</h3>
            <p>Learn AI, Machine Learning, and Automation quickly and effectively.</p>
        </div>
        <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg" alt="Analysis" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #eeeeee;">Analysis</h3>
            <p>We analyze your business and provide a custom data-driven improvement plan.</p>
        </div>
        <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg" alt="Solutions" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #eeeeee;">Solutions</h3>
            <p>Custom-built tools to solve problems and streamline your operations.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
