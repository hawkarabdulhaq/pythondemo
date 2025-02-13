import streamlit as st

def show():
    # --- Banner Section using SVG with overlay text ---
    st.markdown(
        """
        <style>
            .banner-container {
                position: relative;
                width: 100%;
                color: white;
                text-align: center;
            }
            .banner-image {
                width: 100%;
                height: auto;
                display: block;
            }
            .banner-overlay {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 100%;
                padding: 20px;
            }
            .banner-title {
                margin: 0;
                font-size: 2.5em;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            }
            .banner-subtitle {
                margin-top: 10px;
                font-size: 1.2em;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
            }
        </style>
        <div class="banner-container">
            <img class="banner-image" src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/impact_wave.svg" alt="Impact Wave">
            <div class="banner-overlay">
                <h1 class="banner-title">Utilize AI and Machine Learning Faster and Smarter</h1>
                <p class="banner-subtitle">Transform your business into a data-driven, more resilient enterprise with us!</p>
            </div>
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
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg" alt="Training" 
                     style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
                <h3 style="color: #eeeeee;">Training</h3>
                <p style="color: #eeeeee;">Learn AI, Machine Learning, and Automation quickly and effectively.</p>
            </div>
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg" alt="Analysis" 
                     style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
                <h3 style="color: #eeeeee;">Analysis</h3>
                <p style="color: #eeeeee;">We analyze your business and provide a custom data-driven improvement plan.</p>
            </div>
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg" alt="Solutions" 
                     style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
                <h3 style="color: #eeeeee;">Solutions</h3>
                <p style="color: #eeeeee;">Custom-built tools to solve problems and streamline your operations.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
