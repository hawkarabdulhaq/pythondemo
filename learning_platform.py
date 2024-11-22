import streamlit as st
from dictionary import translate  # Import the centralized translate function
import pstudent  # Import the new Student Projects module

def show():
    language = st.session_state.language  # Retrieve the selected language

    # Define four tabs for Canvas, Course Content, Testimonials, and Student Projects
    tab1, tab2, tab3, tab4 = st.tabs([
        translate("canvas_tab", language),
        translate("course_content_tab", language),
        translate("testimonials_tab", language),
        translate("student_projects_tab", language),
    ])

    # Canvas Tab Content
    with tab1:
        st.markdown(f'<div class="title">{translate("learning_platform_title", language)}</div>', unsafe_allow_html=True)
        
        # Display the image for the learning platform
        st.image(
            "https://i.imgur.com/sLdcUzF.jpg", 
            caption=translate("canvas_image_caption", language), 
            use_column_width=True
        )

        # Platform description
        st.markdown(f"""
        <div class="content">
            {translate("learning_platform_description", language)}
        </div>
        """, unsafe_allow_html=True)

    # Course Content Tab Content
    with tab2:
        st.markdown(f'<div class="title">{translate("course_content_title", language)}</div>', unsafe_allow_html=True)

        # Weekly content with expanders for each week
        for week in range(1, 6):
            with st.expander(translate(f"week_{week}_title", language)):
                st.write(f"**{translate('learning_objectives', language)}**: {translate(f'week_{week}_objectives', language)}")
                st.write(f"**{translate('content', language)}:**")
                st.write(translate(f"week_{week}_content", language))
                st.write(f"**{translate('assignments', language)}:**")
                st.write(translate(f"week_{week}_assignments", language))
                additional_resources = translate(f"week_{week}_resources", language)
                if additional_resources:
                    st.write(f"**{translate('additional_resources', language)}:**")
                    st.write(additional_resources)

    # Testimonials Tab Content
    with tab3:
        st.markdown(f'<div class="title">{translate("testimonials_title", language)}</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="content">
            {translate("testimonials_description", language)}
        </div>
        """, unsafe_allow_html=True)

        # Testimonials are included here.

    # Student Projects Tab Content
    with tab4:
        st.markdown(f'<div class="title">{translate("student_projects_title", language)}</div>', unsafe_allow_html=True)
        pstudent.show()  # Display content from the pstudent.py file
