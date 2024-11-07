import streamlit as st

def show():
    # Define two tabs for Learning Platform and Testimonials
    tab1, tab2 = st.tabs(["Learning Platform", "Testimonials"])

    # Learning Platform Tab Content
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
            This interactive platform encourages engagement and ensures you have the support needed to achieve your learning objectives. Below, you can explore the specific content for each week.
        </div>
        """, unsafe_allow_html=True)

        # Weekly content with expanders
        with st.expander("Week 1: Introduction to Coding"):
            st.write("**Learning Objectives**: Introduce foundational coding concepts, set up Python, and use Google Colab.")
            st.write("**Content**:")
            st.write("""
                - **Video**: "Week 1 Presentation: Learning Python with Hawkar" – Introduction to Python basics.
                - **Pages**:
                    - "What is in the Python Script?" – Explanation of Python script components.
                    - "Introduction to Python Libraries" – Overview of essential Python libraries.
                    - "Getting Started with Coding in Google Colab" – Guide on setting up and coding in Google Colab.
                    - "Accessing Google Sheets Data in Google Colab" – How to retrieve data from Google Sheets.
            """)
            st.write("**Assignments**:")
            st.write("""
                - Assignment 1: "Week 1 – Mapping Coordinates" – Write a script to plot geographic coordinates and calculate distances.
                - Assignment 2: "Analyzing Real-Time Earthquake Data" – Using APIs to gather and visualize earthquake data.
            """)
            st.write("**Additional Resources**:")
            st.write("""
                - "Automate Your Tasks with Google Apps Script" – Introduction to Apps Script.
                - "Top 10 Powerful ChatGPT Prompts for Google Apps Script" – Prompt suggestions for automation.
            """)

        # Additional weekly content can be similarly added for Weeks 2 through 5 as per your original content

    # Testimonials Tab Content
    with tab2:
        st.markdown('<div class="title">Participant Testimonials</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="content">
            These testimonials were gathered from participants who have completed the course. Each story reflects their unique journey, goals, and achievements in mastering Python and applying it to their personal or professional projects.
        </div>
        """, unsafe_allow_html=True)

        # Testimonial from Hakari Jalal Mohammed
        with st.expander("Hakari Jalal Mohammed, Bibani"):
            st.markdown("""
            <blockquote>
                "I joined this course to deepen my understanding and practical skills in developing web applications, especially to create tools that enhance learning and make quality educational resources more accessible. The hands-on projects were the most impactful, allowing me to apply my learning in real-time and engage with Dr. Hawkar, who fostered a supportive learning environment. A memorable experience was integrating AI into coding, sparking my interest in using AI for data analysis. I even developed a web application to assist students with chemistry calculations, which received positive feedback from users! This course has expanded my skill set and motivated me to pursue more projects in technology and education."
            </blockquote>
            <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/hakary-bibani-796779334" target="_blank">Hakari-Bibani</a> &nbsp;&nbsp;<strong>GitHub:</strong> <a href="https://github.com/Hakari-Bibani" target="_blank">Hakari-Bibani</a></p>
            """, unsafe_allow_html=True)

        # Add more testimonials in a similar way as needed
