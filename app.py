import streamlit as st
import home
import stepstoexpert  # Keep this if you're still using it for other pages or logic
import business
import solutions
import about
import contact
import style

# Apply custom styles from style.py
style.apply_custom_styles()

# Initialize session state for page tracking
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

def set_page(page):
    """Update the session state's page value."""
    st.session_state["page"] = page

# ---------------------
# Define your training data & show_trainings function
# ---------------------

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

def show_trainings():
    """
    Displays the training courses in a card-style layout with a 'Request' button.
    When a user clicks 'Request', a form appears for collecting invoicing details.
    """
    st.title("Steps to Expert – Our Courses")
    st.markdown("---")

    # Make sure we have a place to store which course was clicked
    if "selected_course" not in st.session_state:
        st.session_state["selected_course"] = None

    # Custom CSS or style
    # (If you want to keep your existing style from style.py, you can skip adding more here.)
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

    courses = get_trainings()["courses"]
    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    # Display each course as a "card"
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

        # A Streamlit button to set the selected course
        button_label = f"Request {course['name']}"
        if st.button(button_label, key=f"request_{course['name']}"):
            st.session_state.selected_course = course["name"]

    st.markdown('</div>', unsafe_allow_html=True)

    # If a course has been selected, show the request form
    if st.session_state.selected_course:
        st.markdown("---")
        st.subheader(f"Request Form for: {st.session_state.selected_course}")

        with st.form("request_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            notes = st.text_area("Additional Info (optional)")

            submitted = st.form_submit_button("Submit Request")
            if submitted:
                # Here you'd handle sending an invoice, storing info, or emailing yourself
                st.success(
                    f"Thank you, {name}! "
                    f"Your request for {st.session_state.selected_course} has been received. "
                    "We'll send you an invoice shortly."
                )
                # Optionally, reset the selected course
                # st.session_state.selected_course = None


# ---------------------
# SIDEBAR NAVIGATION
# ---------------------

with st.sidebar:
    # Display logo
    st.image("input/logo.jpg", width=200)

    # Navigation buttons
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Steps-to-Expert", on_click=set_page, args=("Steps-to-Expert",))
    st.button("Steps-to-Impact", on_click=set_page, args=("Steps-to-Impact",))
    st.button("Steps-to-Solutions", on_click=set_page, args=("Steps-to-Solutions",))
    st.button("About", on_click=set_page, args=("About",))
    st.button("Contact", on_click=set_page, args=("Contact",))

    # Contact Information
    st.markdown(
        """
        <div style="margin-top: 30px; font-size: 1.1em; color: #eeeeee;">
            <p><strong>Contact:</strong></p>
            <p>Email: <a href="mailto:connect@aiforimpact.net" target="_blank" style="color: #1ABC9C;">connect@aiforimpact.net</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------
# MAIN PAGE CONTENT
# ---------------------

page = st.session_state.get("page", "Home")

if page == "Home":
    try:
        home.show()
    except AttributeError:
        st.error("Error: The Home page is not defined properly.")

elif page == "Steps-to-Expert":
    # CALL OUR NEW TRAININGS DISPLAY FUNCTION
    show_trainings()

elif page == "Steps-to-Impact":
    try:
        business.show()
    except AttributeError:
        st.error("Error: The Business (Steps-to-Impact) page is not defined properly.")

elif page == "Steps-to-Solutions":
    try:
        solutions.show()
    except AttributeError:
        st.error("Error: The Solutions page is not defined properly.")

elif page == "About":
    try:
        about.show()
    except AttributeError:
        st.error("Error: The About page is not defined properly.")

elif page == "Contact":
    try:
        contact.show()
    except AttributeError:
        st.error("Error: The Contact page is not defined properly.")

# ---------------------
# FOOTER
# ---------------------

st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        aiforimpact © 2024<br>
        Powered by Climate Resilience Fundraising Platform B.V.
    </div>
    """,
    unsafe_allow_html=True,
)
