import streamlit as st

def show():
    st.markdown('<div class="title">Course Pricing Options</div>', unsafe_allow_html=True)
    
    # Define columns for the four pricing options
    col1, col2, col3, col4 = st.columns(4)

    # Student Offer
    with col1:
        st.markdown("""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Student</h3>
            <h4 style="color: #333; font-size: 1.2em;">39,000 IQD</h4>
            <ul style="list-style-type: none; padding-left: 0; color: #333; font-size: 0.9em; line-height: 1.4;">
                <li>Full access to the platform</li>
                <li>Generalized live coding</li>
                <li>5 interactive group sessions</li>
                <li>Pre-defined final project</li>
                <li>Course certificate</li>
                <li>Code for Impact membership</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Group Offer
    with col2:
        st.markdown("""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Group</h3>
            <h4 style="color: #333; font-size: 1.2em;">195,000 IQD per person</h4>
            <ul style="list-style-type: none; padding-left: 0; color: #333; font-size: 0.9em; line-height: 1.4;">
                <li>Full access to the platform</li>
                <li>Generalized live coding</li>
                <li>5 group sessions</li>
                <li>Pre-defined final project</li>
                <li>Course certificate</li>
                <li>Code for Impact membership</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # One-on-One Offer
    with col3:
        st.markdown("""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">One-on-One</h3>
            <h4 style="color: #333; font-size: 1.2em;">395,000 IQD</h4>
            <ul style="list-style-type: none; padding-left: 0; color: #333; font-size: 0.9em; line-height: 1.4;">
                <li>Full access to the platform</li>
                <li>5 one-on-one sessions</li>
                <li>Personalized live coding</li>
                <li>Custom final project</li>
                <li>Course certificate</li>
                <li>LinkedIn reference</li>
                <li>Follow-up support</li>
                <li>Code for Impact membership</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Enterprise Offer
    with col4:
        st.markdown("""
        <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #1ABC9C; font-size: 1.5em;">Enterprise</h3>
            <h4 style="color: #333; font-size: 1.2em;">950,000 IQD</h4>
            <ul style="list-style-type: none; padding-left: 0; color: #333; font-size: 0.9em; line-height: 1.4;">
                <li>Exclusive one-on-one sessions</li>
                <li>Full access to the platform</li>
                <li>5 personalized sessions per participant</li>
                <li>Custom live coding guidance</li>
                <li>Custom final project</li>
                <li>Course certificate</li>
                <li>LinkedIn reference</li>
                <li>Ongoing follow-up support</li>
                <li>Code for Impact membership</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
