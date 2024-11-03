import streamlit as st

def show():
    st.markdown('<div class="title">Participant Testimonials</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content">
        These testimonials were gathered from participants who have completed the course. Each story reflects their unique journey, goals, and achievements in mastering Python and applying it to their personal or professional projects.
    </div>
    """, unsafe_allow_html=True)

    # Testimonial from Hakari Jalal Mohammed
    st.markdown("""
    <div class="section-title">Hakari Jalal Mohammed, Bibani</div>
    <blockquote>
        "I joined this course to deepen my understanding and practical skills in developing web applications, especially to create tools that enhance learning and make quality educational resources more accessible. The hands-on projects were the most impactful, allowing me to apply my learning in real-time and engage with Dr. Hawkar, who fostered a supportive learning environment. A memorable experience was integrating AI into coding, sparking my interest in using AI for data analysis. I even developed a web application to assist students with chemistry calculations, which received positive feedback from users! This course has expanded my skill set and motivated me to pursue more projects in technology and education."
    </blockquote>
    <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/hakary-bibani-796779334" target="_blank">Hakari-Bibani</a> &nbsp;&nbsp;<strong>GitHub:</strong> <a href="https://github.com/Hakari-Bibani" target="_blank">Hakari-Bibani</a></p>
    """, unsafe_allow_html=True)

    # Testimonial from Akam Namq Abdulkareem
    st.markdown("""
    <div class="section-title">Akam Namq Abdulkareem</div>
    <blockquote>
        "Taking this course was initially a personal hobby, but I have dreams of using these skills in finance and academics. Writing my first script was an exciting milestone. I faced challenges, like connecting Google Drive with Colab, but I overcame them by practicing. I plan to use these skills to build financial applications in the future. I would recommend this course to others, especially if they already have a solid background in computer knowledge."
    </blockquote>
    <p><strong>GitHub:</strong> <a href="https://github.com/akampython" target="_blank">akampython (to be updated soon)</a></p>
    """, unsafe_allow_html=True)

    # Testimonial from Haval Hassan Ali
    st.markdown("""
    <div class="section-title">Haval Hassan Ali</div>
    <blockquote>
        "I wanted to acquire a valuable skill, and this course certainly delivered. Completing assignments was especially impactful, providing practical, hands-on experience. I faced challenges in deploying scripts due to setup and troubleshooting issues, but Dr. Hawkar’s guidance was invaluable. He suggested alternative tools that made the process much smoother, helping me complete deployment successfully. I’m now working on a project I hope to finish soon and plan to use these skills in a pharmacy-related project. I highly recommend this course for its practical approach and encourage future participants to stay engaged and seek support when needed."
    </blockquote>
    <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/haval-ali-72308a19b/" target="_blank">Haval Ali</a></p>
    """, unsafe_allow_html=True)
