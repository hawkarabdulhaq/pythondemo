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
    st.markdown("""
    <style>
    .offer-container {
        display: flex; 
        justify-content: space-around; 
        flex-wrap: wrap; 
        text-align: center;
    }
    .offer-box {
        background-color: ##000000; 
        padding: 20px; 
        border-radius: 10px; 
        width: 30%; 
        margin-bottom: 20px; 
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        cursor: pointer;
    }
    .offer-box img {
        border-radius: 10px; 
        margin-bottom: 15px; 
        width: 100%; 
        height: auto;
    }
    </style>
    <div class="offer-container">
        <div class="offer-box" onclick="setTraining()">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg" alt="Training">
            <h3 style="color: #eeeeee;">Training</h3>
            <p>Learn AI, Machine Learning, and Automation quickly and effectively.</p>
        </div>
        <div class="offer-box" onclick="setBusiness()">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg" alt="Analysis">
            <h3 style="color: #eeeeee;">Analysis</h3>
            <p>We analyze your business and provide a custom data-driven improvement plan.</p>
        </div>
        <div class="offer-box" onclick="setSolutions()">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg" alt="Solutions">
            <h3 style="color: #eeeeee;">Solutions</h3>
            <p>Custom-built tools to solve problems and streamline your operations.</p>
        </div>
    </div>
    <script>
        function setTraining() {{
            window.location.href = "?page=Trainings";
        }}
        function setBusiness() {{
            window.location.href = "?page=Business";
        }}
        function setSolutions() {{
            window.location.href = "?page=Solutions";
        }}
    </script>
    """, unsafe_allow_html=True)

    # Handle Navigation using Session State
    if st.query_params.get("page"):
        selected_page = st.query_params["page"]
        if selected_page == "Trainings":
            st.session_state.page = "Trainings"
        elif selected_page == "Business":
            st.session_state.page = "Business"
        elif selected_page == "Solutions":
            st.session_state.page = "Solutions"
