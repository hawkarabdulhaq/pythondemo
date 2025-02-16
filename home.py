import streamlit as st

def show():
    # --- Banner Section using SVG (no text overlay) ---
    st.markdown(
        """
        <div style="width: 100%; text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/impact_wave.svg"
                 alt="Impact Wave"
                 style="width: 100%; height: auto; display: block;">
        </div>
        <hr style="margin: 30px 0; border: none; border-top: 2px solid #1ABC9C;">
        """,
        unsafe_allow_html=True
    )

    # --- Subtitle ---
    st.markdown(
        """
        <div style="text-align: center; font-size: 1.5em; font-weight: bold; color: #eeeeee; margin-bottom: 20px;">
            Optimizing businesses for resilience and sustainable growth with AI!
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- What We Offer Section ---
    st.markdown(
        """
        <div style="text-align: center; font-size: 2em; font-weight: bold; color: #1ABC9C; margin-bottom: 20px;">
            What We Offer
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Service Cards ---
    st.markdown(
        """
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg" alt="Steps-to-Expert" 
                     style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
                <h3 style="color: #eeeeee;">Steps-to-Expert</h3>
                <p style="color: #eeeeee;">Learn AI, Machine Learning, and Automation quickly and effectively.</p>
            </div>
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg" alt="Steps-to-Impact" 
                     style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
                <h3 style="color: #eeeeee;">Steps-to-Impact</h3>
                <p style="color: #eeeeee;">We analyze your business and provide a custom data-driven improvement plan.</p>
            </div>
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg" alt="Steps-to-Solutions" 
                     style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
                <h3 style="color: #eeeeee;">Steps-to-Solutions</h3>
                <p style="color: #eeeeee;">Custom-built tools to solve problems and streamline your operations.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
