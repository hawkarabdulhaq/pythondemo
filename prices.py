import streamlit as st

def show():
    """Display the updated Pricing page with Advanced plan only."""

    # Page Title
    st.title("💰 Pricing Plans")

    # Pricing Cards
    _, col2 = st.columns(2)

    # Advanced Plan
    with col2:
        st.markdown("### 👑 Advanced Plan ($570)")
        st.write("""
        ✅ 9 weeks of training  
        ✅ 9 theoretical + 9 practical sessions  
        ✅ Project-based learning  
        ✅ Certification  
        ✅ Course: Advanced Machine Learning and Real-Time Deployment  
        """)
        st.markdown(
            '<a href="https://calendly.com/hawkar_abdulhaq/ai-for-impact" '
            'target="_blank" style="background-color:#1ABC9C; color:white; padding:10px 20px; '
            'border-radius:5px; text-decoration:none; font-size:1.1em;">Request</a>',
            unsafe_allow_html=True
        )
