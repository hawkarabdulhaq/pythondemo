# ourtrainings.py

def get_trainings():
    """
    Returns a list of available trainings in the Micro Master Program, structured to highlight courses first,
    followed by program details, impacts, target audience, and format.
    """
    trainings = [
        {
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
                        "Week 2: Supervised and Unsupervised Machine Learning",
                        "Week 3: Deploying AI Models with Streamlit",
                        "Week 4: Real-Time Deployment with GitHub and Cloud Integration",
                    ],
                },
            ],
        },
        {
            "title": "Micro Master in Machine Learning and AI",
            "description": (
                "A comprehensive program designed for learners to build expertise in Python programming, "
                "machine learning, AI, databases, and real-time app deployment using industry-standard tools."
            ),
            "impact": (
                "By completing this program, participants will become trusted professionals in data analysis, "
                "capable of building data-driven systems and creating interactive web applications. Graduates will "
                "be well-equipped to lead data-related projects and deliver insights that drive business success."
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
    ]
    return trainings
