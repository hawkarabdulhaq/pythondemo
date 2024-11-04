# discounts.py
import streamlit as st

def show():
    st.markdown('<div class="title">Discount Opportunities</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content">
        Take advantage of our discount options to make learning more affordable and rewarding!
        
        <ul>
            <li><strong>Earn Discounts with Friend Referrals</strong>: Invite a friend, and they receive a <strong>15% discount</strong> on the course fee. You also receive a <strong>15% discount</strong> as a thank-you!</li>
            <li><strong>Refer Three, Get Your Course Free</strong>: Successfully refer three friends who enroll in the course, and your entire course fee will be <strong>completely waived</strong>.</li>
            <li><strong>Student Discount for 3rd and 4th Graders</strong>: If you're a 3rd or 4th-grade student, you’re eligible for an <strong>80% discount</strong> on the total course price.</li>
        </ul>
        
        <p>For more information, reach out to us at <a href="mailto:connect@habdulhaq.com" style="color: #1ABC9C;">connect@habdulhaq.com</a>.</p>
    </div>
    """, unsafe_allow_html=True)
