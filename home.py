import streamlit as st

def show():
    st.markdown('<div class="title">Welcome to Personalized Python Training</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Perfect for beginners looking to learn coding in just one month and deploy their prototype projects.</div>', unsafe_allow_html=True)

    # Embed YouTube video
    st.markdown("""
    <div class="video-container">
        <h3>Watch the demo video and get to know about the course</h3>
        <iframe width="853" height="480" src="https://www.youtube.com/embed/Y_dxPZu1J6M" 
        title="Demo: Coding with Hawkar" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
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
    - <strong>Applying GitHub for App Creation</strong>: In this module, you'll learn to leverage GitHub to create a small app, setting the stage for your final project. By the end of the week, you’ll be equipped with the skills to develop, manage, and version control your project efficiently, all through GitHub.
    - <strong>Developing Your Final Project</strong>: Over the course of a week, you’ll work on a draft version of your final project, applying core coding concepts in a practical way. This phase will allow you to gather feedback, refine your approach, and ensure your project aligns with your goals.
    - <strong>Finalizing and Launching Your Project</strong>: In the final week, you’ll bring your project to completion. You’ll deploy the app, integrate key features, and showcase it within your community, creating a tangible outcome that reflects your learning journey.
    </div>
    """, unsafe_allow_html=True)

    # Pricing Information
    st.markdown('<div class="section-title">Pricing Options</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content">
    - <span class="highlight">One-on-One Session</span>: 435,000 IQD for a personalized experience<br>
    - <span class="highlight">Group Session (3+ people)</span>: 315,000 IQD per person (for a group of colleagues or friends)

    Choose the option that best fits your needs and learning preferences.
    </div>
    """, unsafe_allow_html=True)

    # Tabs for Enrollment and Demo Session
    col1, col2 = st.columns(2)
    with col1:
        # Styled button for Enroll the Course
        if st.button("Enroll the Course"):
            st.session_state.page = "Enrollment"  # Navigate to Enrollment page

    with col2:
        # Styled button for booking a demo session
        st.markdown(
            '<a href="https://calendly.com/hawkar_abdulhaq/introduction-to-coding-training-with-hawkar" target="_blank" style="text-decoration:none;">'
            '<button style="display:block; width:100%; padding:8px; background-color:#1ABC9C; color:white; border:none; border-radius:5px; font-size:16px;">Book a Demo Session</button>'
            '</a>',
            unsafe_allow_html=True
        )
