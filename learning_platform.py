import streamlit as st

def show():
    # Define four tabs for Canvas, Course Content, Testimonials, and an extra if needed
    tab1, tab2, tab3, tab4 = st.tabs(["Canvas", "Course Content", "Testimonials", "Additional Tab"])

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
                <li><strong>One-on-One Online Session</strong> to discuss goals and clear doubts in a personalized setting.</li>
                <li><strong>Pre-recorded Lectures</strong> covering the core concepts and topics in detail.</li>
                <li><strong>Explanatory Modules</strong> breaking down complex ideas with clear explanations.</li>
                <li><strong>Interactive Discussions</strong> on key topics to deepen your understanding.</li>
                <li><strong>Assignments</strong> to apply what you’ve learned and receive feedback.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Course Content Tab
    with tab2:
        st.markdown('<div class="title">Course Content</div>', unsafe_allow_html=True)

        # Weekly content with expanders for each week
        with st.expander("Week 1: Introduction to Coding"):
            st.write("**Learning Objectives**: Introduce foundational coding concepts, set up Python, and use Google Colab.")
            st.write("**Assignments**: Mapping coordinates, analyzing real-time earthquake data.")
            st.write("**Additional Resources**: Automate tasks with Google Apps Script.")

        with st.expander("Week 2: Generate Comprehensive Codings"):
            st.write("**Learning Objectives**: Build scripts, integrate automation, work with spatial data in Google Earth Engine.")
            st.write("**Assignments**: Image analysis, urban data analysis with geospatial data.")

        with st.expander("Week 3: Deploy App through GitHub and Streamlit"):
            st.write("**Learning Objectives**: Set up for deployment, create applications with Streamlit.")
            st.write("**Assignments**: Build an interactive urban analysis dashboard.")

        with st.expander("Week 4: Draft Submission of Your Personalized Project"):
            st.write("**Learning Objectives**: Develop a personalized project for feedback.")

        with st.expander("Week 5: Finalizing and Showcasing Your Project"):
            st.write("**Learning Objectives**: Finalize and present your personalized project.")

    # Testimonials Tab
    with tab3:
        st.markdown('<div class="title">Participant Testimonials</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="content">
            Testimonials from participants who completed the course. Each story reflects their unique journey and achievements.
        </div>
        """, unsafe_allow_html=True)

        with st.expander("Hakari Jalal Mohammed, Bibani"):
            st.markdown("""
            <blockquote>
                "I joined to deepen my skills in web applications. Hands-on projects allowed real-time application and support from Dr. Hawkar."
            </blockquote>
            <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/hakary-bibani-796779334" target="_blank">Hakari-Bibani</a></p>
            """, unsafe_allow_html=True)

        with st.expander("Akam Namq Abdulkareem"):
            st.markdown("""
            <blockquote>
                "This course started as a hobby, now it's a gateway to building financial applications. Highly recommend it!"
            </blockquote>
            <p><strong>GitHub:</strong> <a href="https://github.com/akampython" target="_blank">akampython</a></p>
            """, unsafe_allow_html=True)

        with st.expander("Haval Hassan Ali"):
            st.markdown("""
            <blockquote>
                "Valuable skills with practical assignments. Dr. Hawkar's guidance made deployment challenges manageable."
            </blockquote>
            <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/haval-ali-72308a19b/" target="_blank">Haval Ali</a></p>
            """, unsafe_allow_html=True)

        # Embed external HTML page for more testimonials
        st.markdown("""
            <div style="margin-top: 40px;">
                <h3>Course Participants</h3>
                <iframe src="https://habdulhaq87.github.io/python_training/" width="100%" height="500px" style="border:none;"></iframe>
            </div>
        """, unsafe_allow_html=True)

    # Additional Tab Content
    with tab4:
        st.markdown('<div class="title">Additional Information</div>', unsafe_allow_html=True)
        st.markdown("<div class='content'>Content for future expansion or additional resources can be placed here.</div>", unsafe_allow_html=True)
