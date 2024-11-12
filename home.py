import streamlit as st

def show():
    st.markdown('<div class="title">Welcome to Personalized Python Programming and Automating Training</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Perfect for beginners looking to learn coding, programming, and automating in just one month and deploy their prototype projects.</div>', unsafe_allow_html=True)

    # Embed YouTube video
    st.markdown("""
    <div class="video-container">
        <h3>Watch the demo video and get to know about the course</h3>
        <iframe width="853" height="600" src="https://www.youtube.com/embed/G8BC2NIfpAs" 
        title="ڕاهێنانی کۆدینگ لەگەڵ هاوکار" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
        encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    # What We Offer Section
    st.markdown('<div class="section-title" style="color: #1ABC9C;">What We Offer You</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content">
    - <strong>Accelerated Learning Path:</strong> Quickly master Python programming with a focused curriculum.<br><br>
    - <strong>Automate Your Daily Tasks:</strong> Streamline workflows to save time and money.<br><br>
    - <strong>Build Real-World Skills:</strong> Create projects to add directly to your CV, showcasing your problem-solving abilities.<br><br>
    - <strong>Enhance Your Professional Profile:</strong> Acquire in-demand skills that boost career potential across various fields.<br><br>
    - <strong>Join the 'Code for Impact' Community:</strong> Access job opportunities, research co-authorship, and a broader market network.
    </div>
    """, unsafe_allow_html=True)
    
    # Enrollment Button
    if st.button("Enroll the Course"):
        st.session_state.page = "Enrollment"
