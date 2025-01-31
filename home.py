import streamlit as st

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Function to update the page state
def set_page(page):
    st.session_state.page = page

def show():
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

    # Display clickable sections for Training, Analysis, and Solutions
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg", use_column_width=True)
        if st.button("📚 Training"):
            set_page("Trainings")

    with col2:
        st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg", use_column_width=True)
        if st.button("📊 Analysis"):
            set_page("Business")

    with col3:
        st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg", use_column_width=True)
        if st.button("🛠 Solutions"):
            set_page("Solutions")

