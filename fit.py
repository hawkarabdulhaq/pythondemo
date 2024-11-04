# fit.py
import streamlit as st

def show():
    st.markdown('<div class="title">Fit Assessment: Discover Your Path with Personalized Python Training</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
        Unlock your potential with a tailored training experience. The Fit Assessment helps you find the best match between your goals and the <strong>Personalized Python Programming and Automation Training</strong> by Hawkar Ali Abdulhaq. By answering a few questions, you’ll discover which training class is best suited to support your growth—whether you’re advancing your career, optimizing operations, enhancing research, or developing new skills for personal projects.
    </div>
    """, unsafe_allow_html=True)

    # Objectives Section
    st.markdown("<h3>Objectives of the Fit Assessment</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><strong>Understand Your Goals:</strong> Align your personal or professional objectives with Python programming.</li>
        <li><strong>Identify Your Class:</strong> Get placed into one of four classes tailored to specific learning needs.</li>
        <li><strong>Highlight Long-Term Impact:</strong> Discover the potential value of Python programming in your journey, from saving time to advancing research and career goals.</li>
        <li><strong>Support Informed Decisions:</strong> Gain insights to make a confident decision about enrolling in the course.</li>
    </ul>
    """, unsafe_allow_html=True)

    # Class Overview Table
    st.markdown("<h3>Class Overview</h3>", unsafe_allow_html=True)
    st.markdown("""
    <table style="width:100%; border-collapse: collapse; margin-bottom: 20px;">
        <tr style="border-bottom: 1px solid var(--border-color);">
            <th style="text-align: left; padding: 10px;"><strong>Class</strong></th>
            <th style="text-align: left; padding: 10px;"><strong>Title</strong></th>
            <th style="text-align: left; padding: 10px;"><strong>Description</strong></th>
        </tr>
        <tr>
            <td style="padding: 10px;">A</td>
            <td style="padding: 10px;">Financial & Operational Optimizers</td>
            <td style="padding: 10px;">For professionals aiming to streamline workflows, save time, and reduce costs with automation.</td>
        </tr>
        <tr>
            <td style="padding: 10px;">B</td>
            <td style="padding: 10px;">Academic & Research Innovators</td>
            <td style="padding: 10px;">Ideal for academics enhancing research efficiency, data analysis, and impact.</td>
        </tr>
        <tr>
            <td style="padding: 10px;">C</td>
            <td style="padding: 10px;">Career Advancers & Skill Builders</td>
            <td style="padding: 10px;">For those strengthening their CV, building technical skills, and advancing their careers.</td>
        </tr>
        <tr>
            <td style="padding: 10px;">D</td>
            <td style="padding: 10px;">Personal Development & Lifelong Learners</td>
            <td style="padding: 10px;">Perfect for lifelong learners applying programming to personal projects and daily tasks.</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    # How It Works Section
    st.markdown("<h3>How It Works: Fit Assessment Workflow</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="content">
        <ol>
            <li><strong>Complete the Survey:</strong> Share your goals and interests.</li>
            <li><strong>Receive Your Results by Email:</strong> Get your tailored class placement and insights for the course.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    # Highlighted Button to Survey
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://docs.google.com/forms/d/e/1FAIpQLScHcfqWZ_-mkfuNpq7hBQQNzqmIX3oHlsE0UAAlIAe7FGaRdw/viewform?usp=sf_link" target="_blank" style="display: inline-block; padding: 12px 24px; font-size: 1.2em; font-weight: bold; color: white; background-color: #1ABC9C; border-radius: 5px; text-decoration: none;">
            Take the Fit Assessment
        </a>
    </div>
    """, unsafe_allow_html=True)
