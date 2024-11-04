import streamlit as st

def show():
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

    # Week 1 content
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

    # Week 2 content
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

    # Week 3 content
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
        st.write('**Discussion**: "GitHub & Streamlit: How Are You Using Them to Elevate Your Project?" – Share experiences on GitHub and Streamlit.')


    # Week 4 content
    with st.expander("Week 4: Draft Submission of Your Personalized Project"):
        st.write("**Learning Objectives**: Develop a personalized project based on skills learned, draft submission for feedback.")
        st.write("**Content**:")
        st.write("""
            - **Page**: "Your Personalized Project" – Guidelines for creating and customizing a project.
        """)
        st.write("**Assignment**: Submit your draft project for review and feedback.")

    # Week 5 content
    with st.expander("Week 5: Finalizing and Showcasing Your Personalized Project"):
        st.write("**Learning Objectives**: Complete the final version of the personalized project, create a portfolio, and prepare a coding portfolio.")
        st.write("**Content**:")
        st.write("""
            - **Page**: "Finalizing and Showcasing Your Personalized Project" – Steps for finalizing and presenting your project.
        """)
        st.write("**Assignment**: Submit the finalized project and develop a portfolio page to showcase work.")
