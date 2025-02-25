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
                "price": "250$",
            },
        ]
    }
    return trainings

def show_app():
    """
    Demonstration of a two-tab approach:
      Tab 1 (Courses): Show course cards & request buttons.
      Tab 2 (Request): Show a request form after user picks a course.
    """

    # Initialize session state
    if "selected_course" not in st.session_state:
        st.session_state["selected_course"] = None
    if "active_tab" not in st.session_state:
        st.session_state["active_tab"] = "Courses"  # default tab

    st.title("Courses & Requests")

    # Create two tabs: "Courses" and "Request"
    tab_courses, tab_request = st.tabs(["Courses", "Request"])

    # --- TAB 1: COURSES ---
    with tab_courses:
        if st.session_state["active_tab"] == "Courses":
            st.markdown("### Explore Our Courses")
            st.markdown("---")

            # CSS for layout
            st.markdown("""
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
            """, unsafe_allow_html=True)

            training_data = get_trainings()
            courses = training_data["courses"]

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
                </div>
                """
                st.markdown(course_html, unsafe_allow_html=True)

                # Add a button that sets the selected course and flips tab
                if st.button(f"Request {course['name']}", key=f"btn_{course['name']}"):
                    st.session_state["selected_course"] = course["name"]
                    st.session_state["active_tab"] = "Request"
                    st.experimental_rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # --- TAB 2: REQUEST FORM ---
    with tab_request:
        if st.session_state["active_tab"] == "Request":
            # If no course selected yet, show a message
            if not st.session_state["selected_course"]:
                st.info("No course selected yet. Please go to 'Courses' tab and choose a course.")
            else:
                st.subheader(f"Request Form for: {st.session_state['selected_course']}")
                with st.form("request_form"):
                    name = st.text_input("Your Name")
                    email = st.text_input("Your Email")
                    notes = st.text_area("Additional Info (optional)")

                    submitted = st.form_submit_button("Submit Request")
                    if submitted:
                        # Here, handle sending invoice or saving data to DB, emailing yourself, etc.
                        st.success(
                            f"Thank you, {name}! Your request for {st.session_state['selected_course']} has been received. "
                            "We'll send you an invoice shortly."
                        )
                        # Optional: Reset selected course if you want to prevent multiple submissions
                        # st.session_state["selected_course"] = None


# Run the app in a single file context:
if __name__ == "__main__":
    show_app()
