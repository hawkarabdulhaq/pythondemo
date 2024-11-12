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

        # Weekly content with expanders for each week
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

        with st.expander("Week 2: Generate Comprehensive Codings"):
            st.write("**Learning Objectives**: Build multi-functional scripts, integrate automation, and work with spatial data in Google Earth Engine.")
            st.write("**Content**:")
            st.write("""
                - **Video**: "Presentation 2 One-on-One Session" – In-depth exploration of Week 2 topics.
                - **Pages**:
                    - "Merging and Reversing Scripts: Essential Skills for Python" – Guidance on combining and breaking down scripts.
                    - "The Importance of Google Apps Script" – Why Apps Script is valuable.
                    - "Understanding Google Earth Engine for Spatial Data Access" – Introduction to using Google Earth Engine.
            """)
            st.write("**Assignments**:")
            st.write("""
                - Assignment 1: "Image Analysis and Rectangle Detection in Python" – Analyze images for specific shapes.
                - Assignment 2: "Urban Analysis with Geospatial Data in Python" – Work on urban data analysis with Python.
            """)
            st.write("**Additional Resources**:")
            st.write("""
                - "About Google Earth Engine" – Overview of Earth Engine capabilities.
                - "Top 10 Essential Prompts for Accessing Data in Google Earth Engine".
                - "Create Google Form by One Click" – Guide to Google Forms automation.
            """)

        with st.expander("Week 3: Deploy App through GitHub and Streamlit"):
            st.write("**Learning Objectives**: Set up a project for deployment, use GitHub for version control, and create interactive applications with Streamlit.")
            st.write("**Content**:")
            st.write("""
                - **Pages**:
                    - "Building Interactive Data Apps with GitHub & Streamlit" – How to create and deploy data applications.
                    - "Do You Know You Can Do a Lot with Streamlit?" – Exploring the capabilities of Streamlit.
                    - "Top 10 Prompt Engineering Techniques for ChatGPT to Optimize GitHub Scripting" – Using ChatGPT prompts for efficient coding.
            """)
            st.write("**Assignments**:")
            st.write("""
                - Assignment: "Building an Interactive Urban Analysis Dashboard Using Streamlit" – Develop a Streamlit dashboard for visualizing urban analysis data.
            """)
            st.write("**Discussion**: 'GitHub & Streamlit: How Are You Using Them to Elevate Your Project?' – Share experiences on GitHub and Streamlit.")

        with st.expander("Week 4: Draft Submission of Your Personalized Project"):
            st.write("**Learning Objectives**: Develop a personalized project based on skills learned, draft submission for feedback.")
            st.write("**Content**:")
            st.write("- **Page**: 'Your Personalized Project' – Guidelines for creating and customizing a project.")
            st.write("**Assignment**: Submit your draft project for review and feedback.")

        with st.expander("Week 5: Finalizing and Showcasing Your Personalized Project"):
            st.write("**Learning Objectives**: Complete the final version of the personalized project, create a portfolio, and prepare a coding portfolio.")
            st.write("**Content**:")
            st.write("- **Page**: 'Finalizing and Showcasing Your Personalized Project' – Steps for finalizing and presenting your project.")
            st.write("**Assignment**: Submit the finalized project and develop a portfolio page to showcase work.")

    # Testimonials Tab Content
    with tab3:
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

        # Testimonial from Akam Namq Abdulkareem
        with st.expander("Akam Namq Abdulkareem"):
            st.markdown("""
            <blockquote>
                "Taking this course was initially a personal hobby, but I have dreams of using these skills in finance and academics. Writing my first script was an exciting milestone. I faced challenges, like connecting Google Drive with Colab, but I overcame them by practicing. I plan to use these skills to build financial applications in the future. I would recommend this course to others, especially if they already have a solid background in computer knowledge."
            </blockquote>
            <p><strong>GitHub:</strong> <a href="https://github.com/akampython" target="_blank">akampython (to be updated soon)</a></p>
            """, unsafe_allow_html=True)

        # Testimonial from Haval Hassan Ali
        with st.expander("Haval Hassan Ali"):
            st.markdown("""
            <blockquote>
                "I wanted to acquire a valuable skill, and this course certainly delivered. Completing assignments was especially impactful, providing practical, hands-on experience. I faced challenges in deploying scripts due to setup and troubleshooting issues, but Dr. Hawkar’s guidance was invaluable. He suggested alternative tools that made the process much smoother, helping me complete deployment successfully. I’m now working on a project I hope to finish soon and plan to use these skills in a pharmacy-related project. I highly recommend this course for its practical approach and encourage future participants to stay engaged and seek support when needed."
            </blockquote>
            <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/haval-ali-72308a19b/" target="_blank">Haval Ali</a></p>
            """, unsafe_allow_html=True)

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
