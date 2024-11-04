import streamlit as st

def show():
    st.markdown('<div class="title">Fit Assessment: Discover Your Path with Personalized Python Training</div>', unsafe_allow_html=True)
    
    # Introduction text
    st.markdown("""
    Unlock your potential with a tailored training experience. The Fit Assessment helps you find the best match between your goals and the Personalized Python Programming and Automation Training by Hawkar Ali Abdulhaq. By answering a few questions, you’ll discover which training class best supports your growth—whether you’re advancing your career, optimizing operations, enhancing research, or developing new skills for personal projects.
    """, unsafe_allow_html=True)

    # Objectives section
    st.subheader("Objectives of the Fit Assessment")
    st.markdown("""
    - **Understand Your Goals**: Align your personal or professional objectives with Python programming.
    - **Identify Your Class**: Get placed into one of four classes tailored to specific learning needs.
    - **Highlight Long-Term Impact**: See the potential value of Python programming for your journey, from saving time to advancing research and career goals.
    - **Support Informed Decisions**: Gain insights to make a confident decision about enrolling in the course.
    """)

    # Class Overview table
    st.subheader("Class Overview")
    st.markdown("""
    | Class | Title                             | Description                                                                        |
    |-------|-----------------------------------|------------------------------------------------------------------------------------|
    | A     | Financial & Operational Optimizers | For professionals aiming to streamline workflows, save time, and reduce costs.       |
    | B     | Academic & Research Innovators     | Ideal for academics enhancing research efficiency, data analysis, and impact.        |
    | C     | Career Advancers & Skill Builders  | For those strengthening their CV, building technical skills, and advancing careers.  |
    | D     | Personal Development & Lifelong Learners | Perfect for lifelong learners applying programming to personal projects and daily tasks. |
    """)

    # Workflow steps
    st.subheader("How It Works: Fit Assessment Workflow")
    st.markdown("""
    1. **Data Entry**: Answer questions about your role, goals, and interests in programming.
    2. **Data Analysis**: Our system scores your responses to match your goals with a class.
    3. **Class Assignment**: You’re placed into one of four classes that best aligns with your needs.
    4. **Personalized Feedback**: Receive an email with your assigned class, explaining what it means for you.
    5. **Enroll with Confidence**: Use the insights to make an informed decision about joining the course, with support from our team every step of the way.
    """)

    # Fit Assessment Form Link
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://docs.google.com/forms/d/e/1FAIpQLScHcfqWZ_-mkfuNpq7hBQQNzqmIX3oHlsE0UAAlIAe7FGaRdw/viewform?usp=sf_link" target="_blank">
            <button style="padding: 10px 20px; font-size: 1.2em; background-color: #1ABC9C; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Take the Fit Assessment
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
