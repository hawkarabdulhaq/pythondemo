import streamlit as st

def show():
    """Display the updated Pricing page with only Basic and Advanced plans."""

    # Page Title
    st.title("💰 Pricing Plans")
    st.markdown("""
    <div style="text-align: center; font-size: 1.3em; color: #1ABC9C; margin-bottom: 20px;">
        Choose the plan that fits your learning goals!
    </div>
    """, unsafe_allow_html=True)

    # Pricing Cards
    col1, col2 = st.columns(2)

    # Basic Plan
    with col1:
        st.markdown("### 🎓 Basic Plan ($250)")
        st.write("""
        ✅ 4 weeks of training  
        ✅ 4 theoretical + 4 practical sessions  
        ✅ Hands-on projects  
        ✅ Certification  
        ✅ Course: Foundations of Python Programming and Applied Coding  
        """)
        st.markdown(
            '<a href="https://checkout.revolut.com/pay/8236b9e9-36c4-4692-911b-735aba86a138" '
            'target="_blank" style="background-color:#1ABC9C; color:white; padding:10px 20px; '
            'border-radius:5px; text-decoration:none; font-size:1.1em;">Request</a>',
            unsafe_allow_html=True
        )

    # Advanced Plan
    with col2:
        st.markdown("### 👑 Advanced Plan ($900)")
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
