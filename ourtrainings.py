from typing import List, Dict
from shadcn.ui import Card, CardContent
from shadcn.ui.button import Button

# Function to return available trainings with detailed content
def get_trainings() -> List[Dict[str, any]]:
    """
    Returns a detailed list of available trainings, including their titles, descriptions, and weeks.
    """
    trainings = [
        {
            "title": "Python Programming through Generative AI for Beginners",
            "description": "Learn Python programming fundamentals with a focus on leveraging generative AI tools.",
            "weeks": [
                "Week 1: Python Basics and Generative AI Overview",
                "Week 2: Advanced Python Concepts",
                "Week 3: Building Your First AI-Powered Application"
            ]
        },
        {
            "title": "Micro Master in Machine Learning and AI",
            "description": "Comprehensive training in coding, databases, machine learning, and real-time AI app deployment.",
            "weeks": [
                "Week 1: Introduction to Coding",
                "Week 2: Generate Comprehensive Codings",
                "Week 3: Deploy App through GitHub and Streamlit",
                "Week 4: Data Week",
                "Course 2: Advanced SQL and Databases",
                "Course 3: Supervised and Unsupervised Machine Learning",
                "Course 4: Deploying AI Models with Streamlit",
                "Course 5: Real-Time Deployment with GitHub and Cloud Integration",
                "Capstone Project"
            ]
        },
        {
            "title": "Business Optimization through Advanced Automation",
            "description": "Master automation tools to streamline business processes and increase efficiency.",
            "weeks": [
                "Week 1: Automation Basics",
                "Week 2: Workflow Optimization",
                "Week 3: Advanced Business Automation Tools"
            ]
        }
    ]
    return trainings

# UI rendering function for displaying trainings in Streamlit
import streamlit as st

def render_trainings_ui():
    """
    Renders a detailed, user-friendly UI for the available trainings using Streamlit.
    """
    st.title("Our Trainings")
    trainings = get_trainings()

    for training in trainings:
        with st.container():
            st.subheader(training["title"])
            st.write(training["description"])

            # Render the weeks in a collapsible format
            with st.expander("Course Details"):
                for week in training["weeks"]:
                    st.write(f"- {week}")

            # Add a button for enrollment or more details
            if st.button(f"Enroll in {training['title']}"):
                st.success(f"You have enrolled in {training['title']}!")

# Run the app if this file is executed
if __name__ == "__main__":
    st.set_page_config(page_title="Our Trainings", layout="wide")
    render_trainings_ui()
