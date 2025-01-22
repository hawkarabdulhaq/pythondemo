import streamlit as st

def show():
    # Display the title
    st.markdown('<div class="title">About Us</div>', unsafe_allow_html=True)

    # Display the profile photo
    st.image(
        "input/me.jpg",
        width=250,
        caption="Our story and journey to excellence.",
        use_column_width="auto",
    )

    # Profile Overview
    st.markdown("""
    <div class="content">
        Learn about our team, mission, and dedication to empowering learners worldwide with the best resources and mentorship.
    </div>
    """, unsafe_allow_html=True)

    # Section: Early Career and Education
    st.markdown("""
    <div class="section-title">Early Career and Education</div>
    <div class="content">
        Our journey began with a strong foundation in technology and education, driven by a passion for innovation.
    </div>
    """, unsafe_allow_html=True)

    # Section: Hasar Organization and PhD Studies
    st.markdown("""
    <div class="section-title">Hasar Organization and PhD Studies</div>
    <div class="content">
        We partnered with leading organizations to advance research and technology for real-world impact.
    </div>
    """, unsafe_allow_html=True)

    # Section: Research and Publications
    st.markdown("""
    <div class="section-title">Research and Publications</div>
    <div class="content">
        Our team has contributed to groundbreaking research in technology and education:
        <ul>
            <li><strong>Publication 1: Exploring AI in Education</strong></li>
            <li><strong>Publication 2: Advancing Learning Platforms</strong></li>
            <li><strong>Publication 3: Innovations in Digital Transformation</strong></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Section: A Passion for Coding and Innovation
    st.markdown("""
    <div class="section-title">A Passion for Coding and Innovation</div>
    <div class="content">
        Our commitment to coding excellence and creative problem-solving drives every aspect of our work.
    </div>
    """, unsafe_allow_html=True)

    # Section: Entrepreneurial Ventures
    st.markdown("""
    <div class="section-title">Entrepreneurial Ventures</div>
    <div class="content">
        From startups to large-scale projects, we bring innovative ideas to life through technology and collaboration.
    </div>
    """, unsafe_allow_html=True)

    # Section: Call to Action
    st.markdown("""
    <div class="content" style="margin-top: 40px;">
        <p>Join us on this journey and become part of a community passionate about learning and innovation.</p>
    </div>
    """, unsafe_allow_html=True)
