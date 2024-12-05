import streamlit as st

def show():
    st.title("Freelance Opportunities")
    st.write("""
        Explore freelance projects and opportunities with Hawkar Abdulhaq. 
        Get in touch to discuss how we can collaborate on projects and create value together.
    """)
    st.markdown("""
        - **Flexible Works**: $35/hour.
        - **Fast Projects**: Higher rates apply.
        - **Weekend Work**: Premium rates available.
    """)
    st.markdown("""
        <div style="margin-top: 30px;">
            <p><strong>Contact us:</strong></p>
            <p>Email: <a href="mailto:connect@habdulhaq.com" target="_blank" style="color: #1ABC9C;">connect@habdulhaq.com</a></p>
        </div>
    """, unsafe_allow_html=True)
