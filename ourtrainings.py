import streamlit as st

def get_trainings():
    """
    Returns a list of available training courses with details.
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
        ]
    }
    return trainings

def show_trainings():
    """
    Display the training courses in the Streamlit app.
    """
    st.title("Our Courses")
    st.markdown("---")
    
    # Fetch training data
    training_data = get_trainings()
    
    # Custom CSS for the Request button
    st.markdown(
        """
        <style>
        .request-button {
            background-color: #286942 !important;
            border: none;
            color: white !important;
            font-weight: bold !important;
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
    st.subheader("📚 Courses")
    for course in training_data["courses"]:
        with st.container():
            st.markdown(f"### {course['name']}")
            st.write(f"**Impact:** {course['impact']}")
            st.write("**Course Chapters:**")
            for chapter in course["chapters"]:
                st.write(f"- {chapter}")
            
            st.markdown(f"**📌 Availability:** {course['availability']}")
            
            # Request button linking to Calendly
            request_html = (
                '<a class="request-button" href="https://calendly.com/hawkar_abdulhaq/ai-for-impact" '
                'target="_blank">Request</a>'
            )
            st.markdown(request_html, unsafe_allow_html=True)
            st.markdown("---")
