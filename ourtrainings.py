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

def show_trainings():
    st.title("Our Courses")
    st.markdown("---")

    # --------------------------------------------------------
    # 1) Handle session state for selected_course and scrolling
    # --------------------------------------------------------
    if "selected_course" not in st.session_state:
        st.session_state.selected_course = None
    if "scroll_to_form" not in st.session_state:
        st.session_state.scroll_to_form = False

    # --------------------------------------------------------
    # 2) If we need to scroll, insert a small JS snippet at top
    # --------------------------------------------------------
    if st.session_state.scroll_to_form:
        scroll_script = """
        <script>
            // Scroll to the form anchor
            var element = document.getElementById("form_anchor");
            if (element) {
                element.scrollIntoView({behavior: 'smooth'});
            }
        </script>
        """
        st.markdown(scroll_script, unsafe_allow_html=True)
        # Reset the flag
        st.session_state.scroll_to_form = False

    # --------------------------------------------------------
    # 3) Display each course as a card
    #    We'll put a placeholder for the form above the button
    # --------------------------------------------------------

    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    training_data = get_trainings()
    courses = training_data["courses"]

    for course in courses:
        # Container for the entire course card
        with st.container():
            st.markdown(
                f"""
                <div class="card">
                    <h3>{course['name']}</h3>
                    <img src="{course['image']}" alt="{course['name']}"/>
                    <p><strong>Impact:</strong> {course['impact']}</p>
                    <p><strong>Course Chapters:</strong></p>
                    <ul>
                """,
                unsafe_allow_html=True,
            )

            for chapter in course["chapters"]:
                st.markdown(f"<li>{chapter}</li>", unsafe_allow_html=True)

            st.markdown(
                f"""
                    </ul>
                    <p><strong>Availability:</strong> {course['availability']}</p>
                    <p><strong>Price:</strong> {course['price']}</p>
                """,
                unsafe_allow_html=True,
            )

            # 4) The placeholder for the form is created above the button
            form_placeholder = st.empty()

            # If this is the selected course, fill the placeholder with the form
            if st.session_state.selected_course == course["name"]:
                # Insert an anchor to scroll to
                st.markdown("<a id='form_anchor'></a>", unsafe_allow_html=True)

                with form_placeholder.container():
                    st.info(f"**Request for: {course['name']}**")
                    with st.form(f"request_form_{course['name']}"):
                        name = st.text_input("Your Name")
                        email = st.text_input("Your Email")
                        notes = st.text_area("Additional Info (optional)")
                        submitted = st.form_submit_button("Submit Request")

                        if submitted:
                            st.success(
                                f"Thank you, {name}! Your request for **{course['name']}** has been received. "
                                "We'll send you an invoice shortly."
                            )
                            # Optionally reset the selected course
                            # st.session_state.selected_course = None

            # 5) Button to request the course
            request_btn = st.button(
                f"Request {course['name']}",
                key=f"btn_{course['name']}"
            )

            if request_btn:
                # Set the selected course in session state
                st.session_state.selected_course = course["name"]
                # Trigger the scroll script
                st.session_state.scroll_to_form = True
                # Rerun so that the form is created, and then we scroll to it
                st.experimental_rerun()

            # Close the HTML card
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # --------------------------------------------------------
    # End of main function
    # --------------------------------------------------------

# ========== END OF SCRIPT ==========

