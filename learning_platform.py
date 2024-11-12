import streamlit as st
import pstudent  # Import the new Student Projects module

def show():
    # Define five tabs for Canvas, Course Content, Testimonials, Course Participants, and Student Projects
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Canvas", "Course Content", "Testimonials", "Course Participants", "Student Projects"])

    # Canvas Tab Content
    with tab1:
        st.markdown('<div class="title">Learning Platform</div>', unsafe_allow_html=True)
        
        # Display the image for the learning platform
        st.image("https://i.imgur.com/sLdcUzF.jpg", caption="Canvas: Your Interactive Learning Platform", use_column_width=True)

        # Platform description
        st.markdown("""
        <div class="content">
            Our dedicated learning platform is hosted on <strong>Canvas</strong>, designed to guide you through a structured and interactive 5-week program. Each week includes:
            <ul>
                <li><strong>One-on-One Online Session</strong> to kickstart the week, allowing you to discuss your goals and clear any doubts in a personalized setting.</li>
                <li><strong>Pre-recorded Lectures</strong> covering the core concepts and topics in detail.</li>
                <li><strong>Explanatory Modules</strong> breaking down complex ideas with clear, digestible explanations.</li>
                <li><strong>Interactive Discussions</strong> on key topics to deepen your understanding.</li>
                <li><strong>Assignments</strong> to apply what you’ve learned and receive feedback.</li>
            </ul>
            This interactive platform encourages engagement and ensures you have the support needed to achieve your learning objectives.
        </div>
        """, unsafe_allow_html=True)

    # Course Content Tab Content
    with tab2:
        st.markdown('<div class="title">Course Content</div>', unsafe_allow_html=True)
        # Add weekly content and details as per previous setup
        # Content for weeks would go here (Week 1, Week 2, etc.), similar to previous example

    # Testimonials Tab Content
    with tab3:
        st.markdown('<div class="title">Participant Testimonials</div>', unsafe_allow_html=True)
        # Testimonials from course participants as per previous setup

    # Course Participants Tab Content
    with tab4:
        st.markdown('<div class="title">Course Participants</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="content">
                Explore the profiles of course participants and their journey in mastering Python.
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <a href="https://habdulhaq87.github.io/python_training/" target="_blank" style="font-size: 1.2em; font-weight: bold; color: #1ABC9C; text-decoration: none;">
                    Open Participant Showcase in Full Screen
                </a>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div style="margin-top: 20px;">
                <iframe src="https://habdulhaq87.github.io/python_training/" width="100%" height="800px" style="border:none;"></iframe>
            </div>
        """, unsafe_allow_html=True)

    # Student Projects Tab Content
    with tab5:
        st.markdown('<div class="title">Student Projects</div>', unsafe_allow_html=True)
        pstudent.show()  # Display content from the pstudent.py file

