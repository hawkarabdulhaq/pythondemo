import streamlit as st

def show():
    """Display the home page with clickable cards for navigation."""
    
    # Banner Section (unchanged)
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

    # Subtitle and Heading (unchanged)
    # ...

    # Modified CSS to include cursor pointer
    st.markdown("""
    <style>
    .offer-container {
        display: flex; 
        justify-content: space-around; 
        flex-wrap: wrap; 
        text-align: center;
    }
    .offer-box {
        background-color: #000000; 
        padding: 20px; 
        border-radius: 10px; 
        width: 30%; 
        margin-bottom: 20px; 
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        cursor: pointer;  /* Add cursor pointer */
    }
    /* Rest of your CSS remains unchanged */
    </style>
    """, unsafe_allow_html=True)

    # Modified Offer Cards with JavaScript reload
    st.markdown("""
    <div class="offer-container">
    
        <!-- Training Card with reload -->
        <a href="?page=Trainings" onclick="window.location.href=this.href; window.location.reload(); return false;">
            <div class="offer-box">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg" alt="Training">
                <h3 style="color: #eeeeee;">Training</h3>
                <p style="color: #cccccc;">Learn AI, Machine Learning, and Automation quickly and effectively.</p>
            </div>
        </a>
        
        <!-- Analysis Card with reload -->
        <a href="?page=Business" onclick="window.location.href=this.href; window.location.reload(); return false;">
            <div class="offer-box">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg" alt="Analysis">
                <h3 style="color: #eeeeee;">Analysis</h3>
                <p style="color: #cccccc;">We analyze your business and provide a custom data-driven improvement plan.</p>
            </div>
        </a>
        
        <!-- Solutions Card with reload -->
        <a href="?page=Solutions" onclick="window.location.href=this.href; window.location.reload(); return false;">
            <div class="offer-box">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg" alt="Solutions">
                <h3 style="color: #eeeeee;">Solutions</h3>
                <p style="color: #cccccc;">Custom-built tools to solve problems and streamline your operations.</p>
            </div>
        </a>

    </div>
    """, unsafe_allow_html=True)

    # Handle query parameters using modern Streamlit methods
    query_params = st.query_params.get("page", None)
    if query_params:
        st.session_state.page = query_params
        st.rerun()
