import streamlit as st
from dictionary import translate  # Import the centralized translate function

def show():
    language = st.session_state.language  # Retrieve the selected language

    st.markdown(f'<div class="title">{translate("course_pricing_title", language)}</div>', unsafe_allow_html=True)
    
    # Define columns for the four pricing options
    col1, col2, col3, col4 = st.columns(4)

    # Style adjustments for readability
    feature_style = "font-size: 0.95em; margin-bottom: 8px;"
    button_style = "background-color: #1ABC9C; color: white; padding: 8px 12px; border-radius: 5px; font-size: 0.9em; font-weight: bold; text-decoration: none; display: inline-block; margin-top: 10px;"

    # Student Offer
    with col1:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">{translate("student_offer_title", language)}</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">{translate("student_offer_price", language)}</h4>
            <div style="{feature_style}">{translate("student_feature_1", language)}</div>
            <div style="{feature_style}">{translate("student_feature_2", language)}</div>
            <div style="{feature_style}">{translate("student_feature_3", language)}</div>
            <div style="{feature_style}">{translate("student_feature_4", language)}</div>
            <div style="{feature_style}">{translate("student_feature_5", language)}</div>
            <div style="{feature_style}">{translate("student_feature_6", language)}</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">{translate("enroll_button", language)}</a>
        </div>
        """, unsafe_allow_html=True)

    # Group Offer
    with col2:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">{translate("group_offer_title", language)}</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">{translate("group_offer_price", language)}</h4>
            <div style="{feature_style}">{translate("group_feature_1", language)}</div>
            <div style="{feature_style}">{translate("group_feature_2", language)}</div>
            <div style="{feature_style}">{translate("group_feature_3", language)}</div>
            <div style="{feature_style}">{translate("group_feature_4", language)}</div>
            <div style="{feature_style}">{translate("group_feature_5", language)}</div>
            <div style="{feature_style}">{translate("group_feature_6", language)}</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">{translate("enroll_button", language)}</a>
        </div>
        """, unsafe_allow_html=True)

    # One-on-One Offer
    with col3:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">{translate("one_on_one_offer_title", language)}</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">{translate("one_on_one_offer_price", language)}</h4>
            <div style="{feature_style}">{translate("one_on_one_feature_1", language)}</div>
            <div style="{feature_style}">{translate("one_on_one_feature_2", language)}</div>
            <div style="{feature_style}">{translate("one_on_one_feature_3", language)}</div>
            <div style="{feature_style}">{translate("one_on_one_feature_4", language)}</div>
            <div style="{feature_style}">{translate("one_on_one_feature_5", language)}</div>
            <div style="{feature_style}">{translate("one_on_one_feature_6", language)}</div>
            <div style="{feature_style}">{translate("one_on_one_feature_7", language)}</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">{translate("enroll_button", language)}</a>
        </div>
        """, unsafe_allow_html=True)

    # Enterprise Offer for 3-5 people
    with col4:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">{translate("enterprise_offer_title", language)}</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">{translate("enterprise_offer_price", language)}</h4>
            <div style="{feature_style}">{translate("enterprise_feature_1", language)}</div>
            <div style="{feature_style}">{translate("enterprise_feature_2", language)}</div>
            <div style="{feature_style}">{translate("enterprise_feature_3", language)}</div>
            <div style="{feature_style}">{translate("enterprise_feature_4", language)}</div>
            <div style="{feature_style}">{translate("enterprise_feature_5", language)}</div>
            <div style="{feature_style}">{translate("enterprise_feature_6", language)}</div>
            <div style="{feature_style}">{translate("enterprise_feature_7", language)}</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfolc_O8_QIn25TylAOwTIKOpHpBV3gG_V4bja79B0EopRLVQ/viewform?usp=sf_link" target="_blank" style="{button_style}">{translate("enroll_button", language)}</a>
        </div>
        """, unsafe_allow_html=True)
