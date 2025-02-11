import streamlit as st

def show():
    # Ensure the content is at the top of the page
    st.set_page_config(page_title="Home", layout="wide")

    # Custom HTML & CSS for top banner
    st.markdown(f"""
    <style>
        /* Ensures full-width banner */
        .banner-container {{
            position: relative;
            text-align: center;
            color: white;
            height: 350px;
            width: 100%;
            background-image: url('https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/waves.jpg');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            padding: 20px;
        }}
        /* Responsive adjustments */
        @media screen and (max-width: 768px) {{
            .banner-container {{
                height: 280px;
            }}
        }}
    </style>

    <div class="banner-container">
        <h1 style="margin: 0; font-size: 2.5em; font-weight: bold;">Utilize AI and Machine Learning Faster and Smarter</h1>
        <p style="margin-top: 10px; font-size: 1.2em;">Transform your business into a data-driven, more resilient enterprise with us!</p>
    </div>
    <hr style="margin: 30px 0; border: none; border-top: 2px solid #1ABC9C;">
    """, unsafe_allow_html=True)

    # Subtitle
    st.markdown("""
    <div style="text-align: center; font-size: 1.5em; font-weight: bold; color: #dddddd; margin-bottom: 20px;">
        Optimizing businesses for resilience and sustainable growth with AI!
    </div>
    """, unsafe_allow_html=True)

    # What We Offer Section
    st.markdown("""
    <div style="text-align: center; font-size: 2em; font-weight: bold; color: #1ABC9C; margin-bottom: 20px;">
        What We Offer
    </div>
    """, unsafe_allow_html=True)

    # Offer Details (Improved responsive layout)
    st.markdown("""
    <style>
        .offer-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 20px;
        }
        .offer-box {
            background-color: #000000;
            padding: 20px;
            border-radius: 10px;
            width: 30%;
            min-width: 280px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .offer-box img {
            border-radius: 10px;
            margin-bottom: 15px;
            width: 100%;
            height: auto;
        }
        .offer-box h3 {
            color: #1ABC9C;
        }
        @media screen and (max-width: 768px) {
            .offer-container {
                flex-direction: column;
                align-items: center;
            }
            .offer-box {
                width: 90%;
            }
        }
    </style>

    <div class="offer-container">
        <div class="offer-box">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg" alt="Training">
            <h3>Training</h3>
            <p>Learn AI, Machine Learning, and Automation quickly and effectively.</p>
        </div>
        <div class="offer-box">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg" alt="Analysis">
            <h3>Analysis</h3>
            <p>We analyze your business and provide a custom data-driven improvement plan.</p>
        </div>
        <div class="offer-box">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg" alt="Solutions">
            <h3>Solutions</h3>
            <p>Custom-built tools to solve problems and streamline your operations.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
