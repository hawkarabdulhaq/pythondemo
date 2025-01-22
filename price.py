import streamlit as st

def show():
    # Set styles for consistent layout
    feature_style = "font-size: 0.95em; margin-bottom: 8px;"
    button_style = "background-color: #1ABC9C; color: white; padding: 8px 12px; border-radius: 5px; font-size: 0.9em; font-weight: bold; text-decoration: none; display: inline-block; margin-top: 10px;"

    # Page title
    st.markdown('<div class="title">Course Pricing</div>', unsafe_allow_html=True)

    # Free Week Demo section
    free_demo_col = st.columns(1)
    with free_demo_col[0]:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 30px;">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Free Week Demo</h3>
            <div style="{feature_style}">Full Access to Week 1</div>
            <div style="{feature_style}">1 Online Session</div>
            <div style="{feature_style}">Available for one week</div>
            <a href="https://calendly.com/hawkar_abdulhaq/introduction-to-coding-training-with-hawkar" target="_blank" style="{button_style}">Enroll Now</a>
        </div>
        """, unsafe_allow_html=True)

    # Define pricing options in columns
    col1, col2, col3, col4 = st.columns(4)

    # Student Offer
    with col1:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Student Offer</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">$100</h4>
            <div style="{feature_style}">Interactive Classes</div>
            <div style="{feature_style}">Hands-On Projects</div>
            <div style="{feature_style}">24/7 Support</div>
            <div style="{feature_style}">Flexible Schedule</div>
            <div style="{feature_style}">Certification</div>
            <div style="{feature_style}">Exclusive Resources</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">Enroll Now</a>
        </div>
        """, unsafe_allow_html=True)

    # Group Offer
    with col2:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Group Offer</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">$80 per person</h4>
            <div style="{feature_style}">For Groups of 5+</div>
            <div style="{feature_style}">Custom Schedules</div>
            <div style="{feature_style}">Group Discounts</div>
            <div style="{feature_style}">Certification for All</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">Enroll Now</a>
        </div>
        """, unsafe_allow_html=True)

    # One-on-One Offer
    with col3:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">One-on-One Offer</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">$200</h4>
            <div style="{feature_style}">Personalized Classes</div>
            <div style="{feature_style}">Mentorship</div>
            <div style="{feature_style}">Flexible Schedule</div>
            <div style="{feature_style}">Premium Support</div>
            <div style="{feature_style}">Certification</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">Enroll Now</a>
        </div>
        """, unsafe_allow_html=True)

    # Enterprise Offer
    with col4:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Enterprise Offer</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">Custom Pricing</h4>
            <div style="{feature_style}">Tailored Training</div>
            <div style="{feature_style}">Team Access</div>
            <div style="{feature_style}">Exclusive Resources</div>
            <div style="{feature_style}">Flexible Timelines</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">Contact Us</a>
        </div>
        """, unsafe_allow_html=True)
