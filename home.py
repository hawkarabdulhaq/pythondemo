import streamlit as st

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

    # Offer Details with Clickable Navigation
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg", use_column_width=True):
            st.session_state.page = "Trainings"
        if st.markdown("### Training"):
            st.session_state.page = "Trainings"
        if st.markdown("Learn AI, Machine Learning, and Automation quickly and effectively."):
            st.session_state.page = "Trainings"

    with col2:
        if st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg", use_column_width=True):
            st.session_state.page = "Business"
        if st.markdown("### Analysis"):
            st.session_state.page = "Business"
        if st.markdown("We analyze your business and provide a custom data-driven improvement plan."):
            st.session_state.page = "Business"

    with col3:
        if st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg", use_column_width=True):
            st.session_state.page = "Solutions"
        if st.markdown("### Solutions"):
            st.session_state.page = "Solutions"
        if st.markdown("Custom-built tools to solve problems and streamline your operations."):
            st.session_state.page = "Solutions"
