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

    # Course Overview
    st.markdown('<div class="section-title">Course Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content">
    Here’s a quick summary of what we’ll cover:

    - <strong>Setting Up Python</strong>: We’ll start by preparing your Python environment, ensuring you’re ready to begin your learning journey with a strong foundation.
    - <strong>Hawkar's Workflow</strong>: I’ll introduce my structured approach to learning Python, focusing on breaking down complex concepts into manageable steps for an efficient learning process.
    - <strong>Applying GitHub for App Creation</strong>: In this module, you'll learn to leverage GitHub to create a small app, setting the stage for your final project.
    - <strong>Developing Your Final Project</strong>: Over the course of a week, you’ll work on a draft version of your final project, applying core coding concepts in a practical way.
    - <strong>Finalizing and Launching Your Project</strong>: In the final week, you’ll bring your project to completion. You’ll deploy the app, integrate key features, and showcase it within your community.
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
