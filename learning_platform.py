import streamlit as st

def show():
    st.markdown('<div class="title">Learning Platform</div>', unsafe_allow_html=True)
    
    # Display the image
    st.image("https://i.imgur.com/sLdcUzF.jpg", caption="Canvas: Your Interactive Learning Platform", use_column_width=True)

    # Platform description with detailed weekly module structure
    st.markdown("""
    <div class="content">
        Our dedicated learning platform is hosted on <strong>Canvas</strong>, designed to guide you through a structured and interactive 5-week program. Each week includes:
        <ul>
            <li><strong>One-on-One Online Session</strong> to kickstart the week, allowing you to discuss your goals and clear any doubts in a personalized setting.</li>
            <li><strong>Pre-recorded Lectures</strong> covering the core concepts and topics in detail.</li>
            <li><strong>Explanatory Modules</strong> breaking down complex ideas with clear, digestible explanations.</li>
            <li><strong>Interactive Discussions</strong> on key topics to deepen your understanding.</li>
            <li><strong>Assignments</strong> to apply what you’ve learned and receive feedback.</li>
        </ul>
        This interactive platform encourages engagement and ensures you have the support needed to achieve your learning objectives. Stay tuned for access details and further updates!
    </div>
    """, unsafe_allow_html=True)
