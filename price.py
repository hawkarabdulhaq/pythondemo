# price.py
import streamlit as st

def show():
    st.markdown('<div class="title">Course Pricing Options</div>', unsafe_allow_html=True)
    
    # Define columns for the four pricing options
    col1, col2, col3, col4 = st.columns(4)

    # Style adjustments for readability
    feature_style = "font-size: 0.95em; margin-bottom: 8px;"
    button_style = "background-color: #1ABC9C; color: white; padding: 10px 15px; border-radius: 5px; font-size: 0.9em; font-weight: bold; text-decoration: none; display: inline-block;"

    # Student Offer
    with col1:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Student</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">39,000 IQD</h4>
            <div style="{feature_style}">Full access to the platform</div>
            <div style="{feature_style}">Generalized live coding</div>
            <div style="{feature_style}">5 interactive group sessions</div>
            <div style="{feature_style}">Pre-defined final project</div>
            <div style="{feature_style}">Course certificate</div>
            <div style="{feature_style}">Code for Impact membership</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">Enroll Now</a>
        </div>
        """, unsafe_allow_html=True)

    # Group Offer
    with col2:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Group</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">195,000 IQD per person</h4>
            <div style="{feature_style}">Full access to the platform</div>
            <div style="{feature_style}">Generalized live coding</div>
            <div style="{feature_style}">5 group sessions</div>
            <div style="{feature_style}">Pre-defined final project</div>
            <div style="{feature_style}">Course certificate</div>
            <div style="{feature_style}">Code for Impact membership</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">Enroll Now</a>
        </div>
        """, unsafe_allow_html=True)

    # One-on-One Offer
    with col3:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">One-on-One</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">395,000 IQD</h4>
            <div style="{feature_style}">Full access to the platform</div>
            <div style="{feature_style}">5 one-on-one sessions</div>
            <div style="{feature_style}">Personalized live coding</div>
            <div style="{feature_style}">Custom final project</div>
            <div style="{feature_style}">Course certificate</div>
            <div style="{feature_style}">LinkedIn reference</div>
            <div style="{feature_style}">Follow-up support</div>
            <div style="{feature_style}">Code for Impact membership</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">Enroll Now</a>
        </div>
        """, unsafe_allow_html=True)

    # Enterprise Offer for 3-5 people
    with col4:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Enterprise</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">950,000 IQD <br> <span style="font-size: 0.9em;">(3-5 participants)</span></h4>
            <div style="{feature_style}">Exclusive one-on-one sessions</div>
            <div style="{feature_style}">Full access to the platform</div>
            <div style="{feature_style}">5 personalized sessions per participant</div>
            <div style="{feature_style}">Custom live coding guidance</div>
            <div style="{feature_style}">Custom final project</div>
            <div style="{feature_style}">Course certificate</div>
            <div style="{feature_style}">LinkedIn reference</div>
            <div style="{feature_style}">Ongoing follow-up support</div>
            <div style="{feature_style}">Code for Impact membership</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">Enroll Now</a>
        </div>
        """, unsafe_allow_html=True)
