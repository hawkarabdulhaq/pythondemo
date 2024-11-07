import streamlit as st

def show():
    st.markdown('<div class="title">Welcome to Personalized Python Programming and Automating Training</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Perfect for beginners looking to learn coding, programming, and automating in just one month and deploy their prototype projects.</div>', unsafe_allow_html=True)

    # Embed YouTube video
    st.markdown("""
    <div class="video-container">
        <h3>Watch the demo video and get to know about the course</h3>
        <iframe width="853" height="480" src="https://www.youtube.com/embed/G8BC2NIfpAs" 
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
    - <strong>Applying GitHub for App Creation</strong>: In this module, you'll learn to leverage GitHub to create a small app, setting the stage for your final project. By the end of the week, you’ll be equipped with the skills to develop, manage, and version control your project efficiently, all through GitHub.
    - <strong>Developing Your Final Project</strong>: Over the course of a week, you’ll work on a draft version of your final project, applying core coding concepts in a practical way. This phase will allow you to gather feedback, refine your approach, and ensure your project aligns with your goals.
    - <strong>Finalizing and Launching Your Project</strong>: In the final week, you’ll bring your project to completion. You’ll deploy the app, integrate key features, and showcase it within your community, creating a tangible outcome that reflects your learning journey.
    </div>
    """, unsafe_allow_html=True)

    # What We Offer Section
    st.markdown('<div class="section-title highlight">What We Offer You</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content">
    - <span class="highlight">Accelerated Learning Path:</span> Quickly master Python programming with a targeted curriculum designed for beginners and hands-on learners.<br><br>
    - <span class="highlight">Automate Your Daily Tasks:</span> Learn to streamline and automate workflows, saving both time and money.<br><br>
    - <span class="highlight">Build Real-World Skills:</span> Develop hands-on projects to add directly to your CV, highlighting your ability to solve practical, real-world problems.<br><br>
    - <span class="highlight">Enhance Your Professional Profile:</span> Acquire a highly sought-after skill that enhances your career potential across fields, from productivity and operations to data analysis and beyond.<br><br>
    - <span class="highlight">Join the 'Code for Good' Community:</span> Become part of a vibrant network that provides access to job opportunities, research co-authorship, and expanded market reach.
    </div>
    """, unsafe_allow_html=True)
    
    # Enrollment Button
    if st.button("Enroll the Course"):
        st.session_state.page = "Enrollment"
