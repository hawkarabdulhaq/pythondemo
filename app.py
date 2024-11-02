import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    /* Set the default font to Courier */
    * {
        font-family: "Courier", monospace;
    }
    
    /* Styling the title */
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #2C3E50;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    /* Styling for section titles */
    .section-title {
        font-size: 1.7em;
        font-weight: bold;
        color: #34495E;
        margin-top: 30px;
        margin-bottom: 10px;
        border-bottom: 2px solid #34495E;
        padding-bottom: 5px;
    }
    
    /* General content styling */
    .content {
        font-size: 1.1em;
        color: #2C3E50;
        line-height: 1.6;
        text-align: justify;
        margin-bottom: 20px;
    }

    /* Highlighting important sections */
    .highlight {
        font-weight: bold;
        color: #1ABC9C;
    }
    
    /* Style for video container */
    .video-container {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title">Welcome to Personalized Python Training</div>', unsafe_allow_html=True)
st.markdown('<div class="content">Perfect for beginners looking to learn coding in just one month and deploy their prototype projects.</div>', unsafe_allow_html=True)

# Embed YouTube video
st.markdown("""
<div class="video-container">
    ### Watch the demo video and get to know about the course
    <iframe width="853" height="480" src="https://www.youtube.com/embed/Y_dxPZu1J6M" 
    title="Demo: Coding with Hawkar" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
    encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" 
    allowfullscreen></iframe>
</div>
""", unsafe_allow_html=True)

# Course Overview
st.markdown('<div class="section-title">Course Overview</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content">
Here’s a quick summary of what we’ll cover:

- **Setting Up Python**: We’ll start by preparing your Python environment, ensuring you’re ready to begin your learning journey with a strong foundation.
- **Hawkar's Workflow**: I’ll introduce my structured approach to learning Python, focusing on breaking down complex concepts into manageable steps for an efficient learning process.
- **Applying GitHub**: We’ll explore how to leverage GitHub for version control, project management, and efficient collaboration, especially relevant if you’re aiming to build real-world projects.
- **Your Personalized Project**: As we progress, we’ll work on projects specifically tailored to your field, helping you apply coding skills in practical scenarios.
- **Building a Future-Proof Skill Set**: Beyond your personalized project, we’ll explore how Python skills can extend into various industries, helping you see how programming can streamline tasks, automate processes, and scale your impact.
</div>
""", unsafe_allow_html=True)

# Pricing Information
st.markdown('<div class="section-title">Pricing Options</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content">
- <span class="highlight">Standard Course Fee</span>: **375,000 IQD (discounted)**
- <span class="highlight">One-on-One Session</span>: **$290** for a personalized experience
- <span class="highlight">Group Session (3+ people)</span>: **$195 per person**

Choose the option that best fits your needs and learning preferences.
</div>
""", unsafe_allow_html=True)

# Enrollment information
st.markdown('<div class="section-title">Enrollment</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content">
To confirm your enrollment, please make the course payment to **FIB account 07504792181**. Once the payment is received, you’ll receive a personalized survey to tailor the training according to your unique needs.

For further details:
- **Email**: [connect@habdulhaq.com](mailto:connect@habdulhaq.com)
- **Website**: [www.habdulhaq.com](https://www.habdulhaq.com/trainings)
</div>
""", unsafe_allow_html=True)
