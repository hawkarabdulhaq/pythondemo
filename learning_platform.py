import streamlit as st
import pstudent  # Import the new Student Projects module

def show():
    # Define four tabs for Canvas, Course Content, Testimonials, and Student Projects
    tab1, tab2, tab3, tab4 = st.tabs([
        "Canvas",
        "Course Content",
        "Testimonials",
        "Student Projects",
    ])

    # Canvas Tab Content
    with tab1:
        st.markdown('<div class="title">Learning Platform</div>', unsafe_allow_html=True)
        
        # Display the image for the learning platform
        st.image(
            "https://i.imgur.com/sLdcUzF.jpg", 
            caption="Explore our advanced learning platform tailored for modern learners.", 
            use_column_width=True
        )

        # Platform description
        st.markdown("""
        <div class="content">
            Our learning platform is designed to provide a seamless and engaging educational experience, 
            offering tools and resources for interactive and effective learning.
        </div>
        """, unsafe_allow_html=True)

    # Course Content Tab Content
    with tab2:
        st.markdown('<div class="title">Course Content</div>', unsafe_allow_html=True)

        # Weekly content with expanders for each week
        for week in range(1, 6):
            with st.expander(f"Week {week}: Topics Overview"):
                st.write(f"**Learning Objectives**: Learn key concepts and skills for Week {week}.")
                st.write("**Content:** Detailed lessons and examples covering the week's topics.")
                st.write("**Assignments:** Hands-on assignments to reinforce learning.")
                additional_resources = f"Additional resources for Week {week}."
                if additional_resources:
                    st.write("**Additional Resources:**")
                    st.write(additional_resources)

    # Testimonials Tab Content
    with tab3:
        st.markdown('<div class="title">Testimonials</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="content">
            Here's what our students have to say about their experience with us:
        </div>
        """, unsafe_allow_html=True)

        # Placeholder for testimonials
        st.markdown("""
        - "This course was life-changing!" - A. Student  
        - "I gained so much confidence in coding." - B. Learner  
        - "The hands-on projects were the best part!" - C. Developer
        """)

    # Student Projects Tab Content
    with tab4:
        st.markdown('<div class="title">Student Projects</div>', unsafe_allow_html=True)
        pstudent.show()  # Display content from the pstudent.py file
