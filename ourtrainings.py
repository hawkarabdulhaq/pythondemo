import streamlit as st

def get_trainings():
    """
    Returns a list of available training courses with details, including prices and banner images.
    """
    trainings = {
        "courses": [
            {
                "name": "Foundations of Python Programming and Applied Coding (Basic Plan)",
                "image": "https://i.imgur.com/tITld9S.jpeg",
                "impact": (
                    "Participants will gain foundational skills in Python programming and learn to create robust scripts, "
                    "work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners to automate "
                    "tasks, process data, and build basic web applications."
                ),
                "chapters": [
                    "Week 1: Introduction to Coding",
                    "Week 2: Generate Comprehensive Codings",
                    "Week 3: Deploy Apps with GitHub and Streamlit",
                    "Week 4: Data Week",
                    "Week 5: Project Capstone",
                    "4 Weeks, each week contain a theorical and practical session",
                ],
                "availability": "Basic Plan",
                "price": "250$",
            },
            {
                "name": "Foundations of Python Programming and Applied Coding (Pro Plan)",
                "image": "https://i.imgur.com/NWELv8b.jpeg",
                "impact": (
                    "Participants will gain foundational skills in Python programming and learn to create robust scripts, "
                    "work with APIs, and utilize tools like Google Colab and GitHub. This course enables learners to automate "
                    "tasks, process data, and build basic web applications."
                ),
                "chapters": [
                    "Week 1: Introduction to Coding",
                    "Week 2: Generate Comprehensive Codings",
                    "Week 3: Deploy Apps with GitHub and Streamlit",
                    "Week 4: Data Week",
                    "Week 5: Project Capstone",
                    "4 Weeks, each week contain a theorical and practical session + 2 Project Mentorship Sessions",
                ],
                "availability": "Pro Plan",
                "price": "350$",
            },
            {
                "name": "Advanced Machine Learning and Real-Time Deployment (VIP Plan)",
                "image": "https://i.imgur.com/iIMdWOn.jpeg",
                "impact": (
                    "Participants will develop advanced skills in database management, machine learning, and real-time "
                    "application deployment. This course focuses on practical implementations, enabling learners to create "
                    "AI-driven solutions, deploy them in real-world scenarios, and integrate apps with cloud and database systems."
                ),
                "chapters": [
                    "Week 1: Advanced SQL and Databases",
                    "Week 2: Fundumental of Statistics for Machine Learning",
                    "Week 3: Unsupervised Machine Learning",
                    "Week 4: Supervised Machine Learning",
                    "Week 5: Processing Data in Real-Time for Decision-Making",
                    "Week 6: Capstone Project",
                    "6 Weeks, each week contain a theorical and practical sessions",
                ],
                "availability": "VIP Plan",
                "price": "900$",
            },
            {
                "name": "Mastering App Automation with Apps Script (Basic Plan)",
                "image": "https://i.imgur.com/XXmFKXq.jpeg",
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
                    "5 Weeks, each week contain a theorical and practical session",
                ],
                "availability": "Basic Plan",
                "price": "250$",
            },
            {
                "name": "Mastering App Automation with Google Apps Script (Pro Plan)",
                "image": "https://i.imgur.com/V5JuNm3.jpeg",
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
                    "5 Weeks, each week contain a theorical and practical session + 2 Project Mentorship Sessions",
                ],
                "availability": "Pro Plan",
                "price": "350$",
            },
        ]
    }
    return trainings

def show_trainings():
    """
    Display the training courses in a card-style layout, including prices and images.
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
        .card img {
            width: 100%;
            height: auto;
            border-radius: 10px;
            margin-bottom: 15px;
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
        course_html = f"""
        <div class="card">
            <h3>{course['name']}</h3>
            <img src="{course['image']}" alt="{course['name']}"/>
            <p><strong>Impact:</strong> {course['impact']}</p>
            <p><strong>Course Chapters:</strong></p>
            <ul>
        """
        for chapter in course["chapters"]:
            course_html += f"<li>{chapter}</li>"
        course_html += f"""
            </ul>
            <p><strong>Availability:</strong> {course['availability']}</p>
            <p><strong>Price:</strong> {course['price']}</p>
            <a class="request-button" href="https://calendar.app.google/o6eQcsxCDwofXNn59" target="_blank">Request</a>
        </div>
        """
        st.markdown(course_html, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
