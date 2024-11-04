# fit.py
import streamlit as st

def show():
    st.markdown('<div class="title">Fit Assessment: Discover Your Path with Personalized Python Training</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content">
        <p>Unlock your potential with a tailored training experience. The Fit Assessment helps you find the best match between your goals and the <strong>Personalized Python Programming and Automation Training</strong> by Hawkar Ali Abdulhaq. By answering a few questions, you’ll discover which training class best supports your growth—whether you’re advancing your career, optimizing operations, enhancing research, or developing new skills for personal projects.</p>
        
        <h3>Objectives of the Fit Assessment</h3>
        <ul>
            <li><strong>Understand Your Goals:</strong> Align your personal or professional objectives with Python programming.</li>
            <li><strong>Identify Your Class:</strong> Get placed into one of four classes tailored to specific learning needs.</li>
            <li><strong>Highlight Long-Term Impact:</strong> See the potential value of Python programming for your journey, from saving time to advancing research and career goals.</li>
            <li><strong>Support Informed Decisions:</strong> Gain insights to make a confident decision about enrolling in the course.</li>
        </ul>
        
        <h3>Class Overview</h3>
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
                <td style="padding: 10px;">Perfect for lifelong learners looking to apply programming to personal projects and daily tasks.</td>
            </tr>
        </table>

        <h3>How It Works: Fit Assessment Workflow</h3>
        <ol>
            <li><strong>Data Entry:</strong> Answer questions about your role, goals, and interests in programming.</li>
            <li><strong>Data Analysis:</strong> Our system scores your responses to match your goals with a class.</li>
            <li><strong>Class Assignment:</strong> You’re placed into one of four classes that best aligns with your needs.</li>
            <li><strong>Personalized Feedback:</strong> Receive an email with your assigned class, explaining what it means for you.</li>
            <li><strong>Enroll with Confidence:</strong> Use the insights to make an informed decision about joining the course, with support from our team every step of the way.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    # Add a big highlighted button for the Google Form link
    st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 20px;">
        <a href="https://docs.google.com/forms/d/e/1FAIpQLScHcfqWZ_-mkfuNpq7hBQQNzqmIX3oHlsE0UAAlIAe7FGaRdw/viewform?usp=sf_link" 
           target="_blank" style="background-color: #1ABC9C; color: white; font-size: 1.2em; padding: 15px 30px; border-radius: 10px; text-decoration: none;">
            Take the Fit Assessment
        </a>
    </div>
    """, unsafe_allow_html=True)
