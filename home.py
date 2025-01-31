import streamlit as st

def set_page(page):
    """Function to update the page session state."""
    st.session_state.page = page

def show():
    """Display the home page with interactive navigation."""
    
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

    # Columns for Interactive Sections
    col1, col2, col3 = st.columns(3)

    with col1:
        # Training Section
        if st.button("", key="trainings_button", on_click=set_page, args=("Trainings",)):
            pass  # Button click triggers page change
        st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg", use_column_width=True)
        st.markdown(
            '<h3 style="text-align: center; color: #eeeeee; cursor: pointer;">Training</h3>', 
            unsafe_allow_html=True
        )
        st.write("Learn AI, Machine Learning, and Automation quickly and effectively.")

    with col2:
        # Business Analysis Section
        if st.button("", key="business_button", on_click=set_page, args=("Business",)):
            pass  # Button click triggers page change
        st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg", use_column_width=True)
        st.markdown(
            '<h3 style="text-align: center; color: #eeeeee; cursor: pointer;">Analysis</h3>', 
            unsafe_allow_html=True
        )
        st.write("We analyze your business and provide a custom data-driven improvement plan.")

    with col3:
        # Solutions Section
        if st.button("", key="solutions_button", on_click=set_page, args=("Solutions",)):
            pass  # Button click triggers page change
        st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg", use_column_width=True)
        st.markdown(
            '<h3 style="text-align: center; color: #eeeeee; cursor: pointer;">Solutions</h3>', 
            unsafe_allow_html=True
        )
        st.write("Custom-built tools to solve problems and streamline your operations.")
