import streamlit as st

def show():
    """Display the Solutions page."""
    
    # Banner Section with Background Image
    st.markdown(f"""
    <div style="
        position: relative;
        text-align: center;
        color: white;
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
        <h1 style="margin: 0; font-size: 2.5em; font-weight: bold;">Data-Driven Solutions for Your Business</h1>
        <p style="margin-top: 10px; font-size: 1.2em;">Custom-built tools to solve problems and streamline operations.</p>
    </div>
    <hr style="margin: 30px 0; border: none; border-top: 2px solid #1ABC9C;">
    """, unsafe_allow_html=True)

    # Introduction to Solutions
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-bottom: 10px;">
        Tailored Data Solutions for Businesses & Organizations
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #34495E; margin-bottom: 30px;">
        We design, develop, and implement data-driven solutions to optimize decision-making, efficiency, and automation.
    </div>
    """, unsafe_allow_html=True)

    # Solutions We Offer
    st.markdown("""
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center;">
        <div style="width: 30%; background-color: #f4f8fb; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/mapping.jpg" alt="Mapping Solutions" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #34495E;">Mapping & GIS Solutions</h3>
            <p>Developing spatial intelligence solutions to visualize and analyze geographic data for better decision-making.</p>
        </div>
        <div style="width: 30%; background-color: #f4f8fb; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/machine_learning.jpg" alt="Machine Learning" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #34495E;">Machine Learning Solutions</h3>
            <p>Leveraging AI-driven models to analyze data, predict trends, and automate processes for smarter business operations.</p>
        </div>
        <div style="width: 30%; background-color: #f4f8fb; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/business_data.jpg" alt="Business Data Solutions" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #34495E;">Business Data Solutions</h3>
            <p>Developing real-time data pipelines, dashboards, and automation tools to optimize business decision-making.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Custom Solutions Section
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-top: 40px;">
        Need a Custom Data Solution?
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #34495E; margin-bottom: 30px;">
        Whether you need AI-driven models, mapping tools, or business automation, we tailor solutions to your needs.
    </div>
    """, unsafe_allow_html=True)
