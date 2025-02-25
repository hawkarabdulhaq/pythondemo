import streamlit as st

def get_trainings():
    """
    Returns a list of available training courses with details.
    """
    trainings = {
        "courses": [
            {
                "name": "Course 1 Basic Plan: Foundations of Python Programming and Applied Coding",
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
                    "Week 5: Project Capstone",
                ],
                # No "availability" key here
            },
            {
                "name": "Course 1 Pro Plan: Foundations of Python Programming and Applied Coding (Project Mentorship)",
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
                    "Week 5: Project Capstone",
                ],
                # No "availability" key here
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
            {
                "name": "Course 3: Mastering App Automation with Google Apps Script",
                "impact": (
                    "Participants will learn to leverage Google Apps Script to automate routine tasks, streamline workflows, "
                    "and build custom applications that integrate with various Google services. This course empowers learners "
                    "to create efficient and scalable automation solutions for data processing, communication, and collaboration."
                ),
                "chapters": [
                    "Week 1: Introduction to Google Apps Script and Automation",
                    "Week 2: Building Custom Functions and Triggers",
                    "Week 3: Automating Data Collection and Processing",
                    "Week 4: Integrating Google APIs and Third-Party Services",
                    "Week 5: Capstone Project: Automating a Real-World Workflow",
                ],
                "availability": "✅ Included in Pro and VIP Plans (Not available in Basic Plan)",
            },
        ]
    }
    return trainings

def show_trainings():
    """
    Display the training courses in a card-style layout.
    """
    st.title("Our Courses")
    st.markdown("---")
    
    # Custom CSS for card layout and button styling with dark grey cards
    st.markdown(
        """
        <style>
        .card-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .card {
            background: #2f2f2f;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            flex: 1 1 calc(50% - 20px);
            max-width: calc(100% - 20px);
            margin-bottom: 20px;
        }
        .card h3 {
            color: #ffffff;
            margin-bottom: 10px;
        }
        .card p {
            color: #ffffff;
            line-height: 1.5;
        }
        .card ul {
            padding-left: 20px;
            color: #ffffff;
        }
        .request-button {
            background-color: #ffffff;
            border: none;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin-top: 10px;
            cursor: pointer;
            border-radius: 12px;
        }
        @media screen and (max-width: 768px) {
            .card {
                flex: 1 1 100%;
                max-width: 100%;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    training_data = get_trainings()
    courses = training_data["courses"]
    
    # Container for card layout
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    
    for course in courses:
        # Determine button text and link based on the course name
        if course["name"] == "Course 1: Foundations of Python Programming and Applied Coding":
            button_text = "Basic Plan: 250$"
            button_link = "https://checkout.revolut.com/pay/8236b9e9-36c4-4692-911b-735aba86a138"
        elif course["name"] == "Course 1 Pro Plan: Foundations of Python Programming and Applied Coding (Project Mentorship)":
            button_text = "Buy Pro Plan 350$"
            button_link = "https://checkout.revolut.com/payment-link/8c157d7f-8079-4359-9f66-db08e83f962e"
        else:
            button_text = "Request"
            button_link = "https://calendar.app.google/o6eQcsxCDwofXNn59"
        
        course_html = f"""
        <div class="card">
            <h3>{course['name']}</h3>
            <p><strong>Impact:</strong> {course['impact']}</p>
            <p><strong>Course Chapters:</strong></p>
            <ul>
        """
        for chapter in course["chapters"]:
            course_html += f"<li>{chapter}</li>"
        course_html += "</ul>"
        
        # Only show availability if it exists
        if "availability" in course:
            course_html += f"""
            <p><strong>Availability:</strong> {course['availability']}</p>
            """
        
        course_html += f"""
            <a class="request-button" href="{button_link}" target="_blank">{button_text}</a>
        </div>
        """
        
        st.markdown(course_html, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
