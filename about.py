import streamlit as st

def show():
    """Display the About Us page."""

    # Banner Section with Background Image
    st.markdown(f"""
    <div style="
        position: relative;
        text-align: center;
        color: white;
        height: 300px;
        background-image: url('https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/about.jpg');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    ">
        <h1 style="margin: 0; font-size: 2.5em; font-weight: bold;">About Us</h1>
        <p style="margin-top: 10px; font-size: 1.2em;">Transforming businesses into data-driven, resilient, and sustainable enterprises.</p>
    </div>
    <hr style="margin: 30px 0; border: none; border-top: 2px solid #1ABC9C;">
    """, unsafe_allow_html=True)

    # Introduction Section
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-bottom: 10px;">
        Who We Are
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #eeeeee; margin-bottom: 30px;">
        We are an **AI and Sustainability startup**, leveraging expertise in **Climate Action, Environmental Sustainability, and Business Optimization** to create **Code for Impact**.
    </div>
    """, unsafe_allow_html=True)

    # Our Goal
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-top: 40px;">
        Our Goal
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #eeeeee; margin-bottom: 30px;">
        Our mission is to **help businesses transition into data-driven, resilient, and sustainable organizations** by integrating advanced AI solutions and data analytics.
    </div>
    """, unsafe_allow_html=True)

    # Call to Action
    st.markdown("""
    <div style="text-align: center; font-size: 1.5em; font-weight: bold; color: #1ABC9C; margin-top: 40px;">
        Ready to make your business data-driven?
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #eeeeee; margin-bottom: 30px;">
        Let’s collaborate to drive impact with AI-powered sustainability solutions.
    </div>
    """, unsafe_allow_html=True)
