# price.py
import streamlit as st

def show():
    st.markdown('<div class="title">Course Pricing Options</div>', unsafe_allow_html=True)
    
    # Define columns for the four pricing options
    col1, col2, col3, col4 = st.columns(4)

    # Style adjustments for readability
    feature_style = "font-size: 0.95em; margin-bottom: 8px;"

    # Student Offer
    with col1:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Student</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">39,000 IQD</h4>
            <ul style="list-style-type: disc; padding-left: 1.2em; color: #333;">
                <li style="{feature_style}">Full access to the platform</li>
                <li style="{feature_style}">Generalized live coding</li>
                <li style="{feature_style}">5 interactive group sessions</li>
                <li style="{feature_style}">Pre-defined final project</li>
                <li style="{feature_style}">Course certificate</li>
                <li style="{feature_style}">Code for Impact membership</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Group Offer
    with col2:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Group</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">195,000 IQD per person</h4>
            <ul style="list-style-type: disc; padding-left: 1.2em; color: #333;">
                <li style="{feature_style}">Full access to the platform</li>
                <li style="{feature_style}">Generalized live coding</li>
                <li style="{feature_style}">5 group sessions</li>
                <li style="{feature_style}">Pre-defined final project</li>
                <li style="{feature_style}">Course certificate</li>
                <li style="{feature_style}">Code for Impact membership</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # One-on-One Offer
    with col3:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">One-on-One</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">395,000 IQD</h4>
            <ul style="list-style-type: disc; padding-left: 1.2em; color: #333;">
                <li style="{feature_style}">Full access to the platform</li>
                <li style="{feature_style}">5 one-on-one sessions</li>
                <li style="{feature_style}">Personalized live coding</li>
                <li style="{feature_style}">Custom final project</li>
                <li style="{feature_style}">Course certificate</li>
                <li style="{feature_style}">LinkedIn reference</li>
                <li style="{feature_style}">Follow-up support</li>
                <li style="{feature_style}">Code for Impact membership</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Enterprise Offer
    with col4:
        st.markdown(f"""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Enterprise</h3>
            <h4 style="color: #333; font-size: 1.1em; margin-top: 5px;">950,000 IQD</h4>
            <ul style="list-style-type: disc; padding-left: 1.2em; color: #333;">
                <li style="{feature_style}">Exclusive one-on-one sessions</li>
                <li style="{feature_style}">Full access to the platform</li>
                <li style="{feature_style}">5 personalized sessions per participant</li>
                <li style="{feature_style}">Custom live coding guidance</li>
                <li style="{feature_style}">Custom final project</li>
                <li style="{feature_style}">Course certificate</li>
                <li style="{feature_style}">LinkedIn reference</li>
                <li style="{feature_style}">Ongoing follow-up support</li>
                <li style="{feature_style}">Code for Impact membership</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
