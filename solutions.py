import streamlit as st

def show():
    """Display the Steps-to-Solutions page."""
    
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
        <h1 style="margin: 0; font-size: 2.5em; font-weight: bold;">Steps-to-Solutions</h1>
        <p style="margin-top: 10px; font-size: 1.2em;">Custom-built tools to solve problems, streamline operations, and drive innovation.</p>
    </div>
    <hr style="margin: 30px 0; border: none; border-top: 2px solid #1ABC9C;">
    """, unsafe_allow_html=True)

    # Introduction to Steps-to-Solutions
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-bottom: 10px;">
        Tailored Data Solutions for Every Business
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #eeeeee; margin-bottom: 30px;">
        Through Steps-to-Solutions, we design, develop, and implement the tools you need to optimize decision-making, efficiency, and automation.
    </div>
    """, unsafe_allow_html=True)

    # Solutions We Offer
    st.markdown("""
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center;">
        <div style="width: 30%; background-image: url('https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/GIS.jpg'); background-size: cover; background-position: center; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); color: white;">
            <h3 style="color: white;">Mapping & GIS Solutions</h3>
            <p>Visualize and analyze geographic data to make location-based decisions with greater accuracy and clarity.</p>
        </div>
        <div style="width: 30%; background-image: url('https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/machine learning.jpg'); background-size: cover; background-position: center; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); color: white;">
            <h3 style="color: white;">Machine Learning Solutions</h3>
            <p>Leverage AI-driven models to predict trends, automate processes, and power smarter business operations.</p>
        </div>
        <div style="width: 30%; background-image: url('https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/businesses.jpg'); background-size: cover; background-position: center; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); color: white;">
            <h3 style="color: white;">Business Data Solutions</h3>
            <p>Implement real-time data pipelines, dashboards, and automation tools to optimize your organization's decision-making.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Custom Solutions Section
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-top: 40px;">
        Need a Custom Data Solution?
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #eeeeee; margin-bottom: 30px;">
        Whether you need AI-driven models, mapping tools, or business automation, Steps-to-Solutions can tailor an approach to meet your specific needs.
    </div>
    """, unsafe_allow_html=True)
