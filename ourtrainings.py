import streamlit as st

def get_trainings():
    """
    Returns a list of available trainings in the Micro Master Program, structured to highlight courses first,
    followed by program details, vision, target audience, and format.
    """
    trainings = {
        "courses": [
            {
                "name": "Course 1: Foundations of Python Programming and Applied Coding",
                "impact": (
                    "Participants will gain foundational skills in Python programming and learn to create robust "
                    "scripts, work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners "
                    "to automate tasks, process data, and build basic web applications."
                ),
                "chapters": [
                    "Week 1: Introduction to Coding",
                    "Week 2: Generate Comprehensive Codings",
                    "Week 3: Deploy Apps with GitHub and Streamlit",
                    "Week 4: Data Week",
                ],
                "availability": "✅ Included in Basic, Pro, and VIP Plans",
            },
            {
                "name": "Course 2: Advanced Machine Learning and Real-Time Deployment",
                "impact": (
                    "Participants will develop advanced skills in database management, machine learning, and real-time "
                    "application deployment. This course focuses on practical implementations, enabling learners to create "
                    "AI-driven solutions, deploy them in real-world scenarios, and integrate apps with cloud and database systems."
                ),
                "chapters": [
                    "Week 1: Advanced SQL and Databases",
                    "Week 2: Deploy Database",
                    "Week 3: Unsupervised Machine Learning",
                    "Week 4: Supervised Machine Learning",
                    "Week 5: Processing Data in Real-Time for Decision-Making",
                    "Week 6: Capstone Project",
                ],
                "availability": "✅ Included in Pro and VIP Plans (Not available in Basic Plan)",
            },
        ],

        "program": {
            "title": "Micro Master in Machine Learning and AI",
            "description": (
                "A comprehensive program designed for learners to build expertise in Python programming, "
                "machine learning, AI, databases, and real-time app deployment using industry-standard tools."
            ),
            "vision": (
                "Our vision is to empower learners to become pioneers in data science and artificial intelligence, "
                "capable of transforming raw data into actionable insights and innovative solutions. Participants will "
                "lead the future of AI-driven systems, bridging the gap between data and decision-making."
            ),
            "target_audience": (
                "Ideal for professionals working with data, businesses dealing with ERP systems, and anyone "
                "looking to leverage data for decision-making. Also suited for organizations aiming to adopt "
                "AI-powered solutions to optimize operations."
            ),
            "format": (
                "The course is personalized to fit your career development. It includes two sessions per week: "
                "one focused on theoretical concepts and one dedicated to hands-on practical exercises. "
                "This blended approach ensures participants can immediately apply their learning to real-world challenges."
            ),
        },
    }
    return trainings


def show_trainings():
    """
    Display the 'Micro Master in Machine Learning and AI' page content in the Streamlit app with a professional UI.
    """
    st.title("🎓 Micro Master in Machine Learning and AI")
    st.markdown("---")
    st.markdown(
        """
        ### Program Overview
        This program is designed to transform learners into skilled professionals, equipping them with cutting-edge tools 
        and techniques to excel in data analysis, machine learning, and AI-driven solutions.
        """
    )

    # Fetch training data
    training_data = get_trainings()

    # Display program-wide details in an appealing layout
    program = training_data["program"]
    with st.container():
        st.subheader("📋 Program Details")
        st.write(f"**Description:** {program['description']}")
        st.markdown(f"**🎯 Vision:** {program['vision']}")
        st.markdown(f"**👥 Target Audience:** {program['target_audience']}")
        st.markdown(f"**🕒 Format:** {program['format']}")

    st.markdown("---")
    
    # Custom CSS for the Request button
    st.markdown(
        """
        <style>
        .request-button {
            background-color: #286942 !important; /* Light green */
            border: none;
            color: white !important; /* White text */
            font-weight: bold !important; /* Bold text */
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display courses in a card-like layout with styled Request buttons
    st.subheader("📚 Courses in the Program")
    for course in training_data["courses"]:
        with st.container():
            st.markdown(f"### {course['name']}")
            st.write(f"**Impact:** {course['impact']}")
            st.write("**Course Chapters:**")
            for chapter in course["chapters"]:
                st.write(f"- {chapter}")
            
            # Availability based on pricing plans
            st.markdown(f"**📌 Availability:** {course['availability']}")

            # Request button linking to Calendly
            request_html = f"""
            <a class="request-button" href="https://calendly.com/hawkar_abdulhaq/ai-for-impact" target="_blank">Request</a>
            """
            st.markdown(request_html, unsafe_allow_html=True)
            st.markdown("---")
