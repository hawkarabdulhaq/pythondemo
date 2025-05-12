import streamlit as st

def show():
    # --- Banner Section using SVG ---
    st.markdown(
        """
        <div style="width: 100%; text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/impact_wave.svg"
                 alt="Impact Wave"
                 style="width: 100%; height: auto; display: block;">
        </div>
        <hr style="margin: 30px 0; border: none; border-top: 2px solid #1ABC9C;">
        """,
        unsafe_allow_html=True
    )

    # --- Subtitle ---
    st.markdown(
        """
        <div style="text-align: center; font-size: 1.5em; font-weight: bold; color: #eeeeee; margin-bottom: 20px;">
            Accelerate your journey from learner to expert with Impact-Driven Coding—proven workflows for maximum results.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Master Class Announcement ---
    st.markdown(
        """
        <div style="border: 2px solid #1ABC9C; border-radius: 12px; padding: 20px; background-color: #111111; margin-bottom: 40px;">
            <h2 style="color: #1ABC9C; text-align: center;">📣 Master Class Announcement</h2>
            <p style="color: #eeeeee; font-size: 1.1em;">
                Join our <strong>in-person</strong> 2-week course in <strong>Erbil</strong>:
                <br><br>
                <strong>🗓 June 29 – July 10, 2025</strong><br>
                <strong>📍 Master Class of Utilizing AI for Advanced Machine Learning and Real-Time Deployment</strong><br><br>
                This exclusive program includes <strong>10 sessions</strong> (2 hours each), with hands-on training in:
                <ul style="color: #eeeeee; padding-left: 25px;">
                    <li>Your Data, Your Future Impact</li>
                    <li>Ice Breaker for Coding</li>
                    <li>Modularity Programming</li>
                    <li>UI and App Building</li>
                    <li>Advanced SQL and Databases</li>
                    <li>Statistics for ML</li>
                    <li>Unsupervised ML</li>
                    <li>Supervised ML</li>
                    <li>Neural Networks</li>
                    <li>Capstone Project</li>
                </ul>
                <p style="color: #eeeeee; font-size: 1.2em; font-weight: bold; text-align: center; margin-top: 10px;">
                    💵 Course Fee: <span style="color: #1ABC9C;">$635 USD</span>
                </p>
                <div style="text-align: center; margin-top: 20px;">
                    <a href="https://docs.google.com/forms/d/e/1FAIpQLSdfISuw6xQvoXI-VFrPQ_HGkQ56ftr4uXr0BKrDCZM4GuKxHw/viewform?usp=header" 
                       target="_blank"
                       style="background-color: #1ABC9C; color: white; padding: 10px 20px; text-decoration: none;
                       border-radius: 8px; font-weight: bold; font-size: 1.1em;">Apply Now</a>
                </div>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- What We Offer Section ---
    st.markdown(
        """
        <div style="text-align: center; font-size: 2em; font-weight: bold; color: #1ABC9C; margin-bottom: 20px;">
            What We Offer
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Service Cards ---
    st.markdown(
        """
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg" alt="Steps-to-Expert" 
                     style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
                <h3 style="color: #eeeeee;">Steps-to-Expert</h3>
                <p style="color: #eeeeee;">
                    Quickly master AI and Machine Learning through expert-crafted Impact-Driven Coding workflows.
                </p>
            </div>
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg" alt="Catalyst Effect" 
                     style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
                <h3 style="color: #eeeeee;">Catalyst Effect</h3>
                <p style="color: #eeeeee;">
                    Accelerate your learning and productivity with scientifically validated Impact-Driven Coding strategies.
                </p>
            </div>
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
                <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg" alt="Explore Beyond" 
                     style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
                <h3 style="color: #eeeeee;">Explore Beyond</h3>
                <p style="color: #eeeeee;">
                    Unlock hidden talents and potentials through customized, proven Impact-Driven Coding techniques.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
