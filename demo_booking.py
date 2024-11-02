import streamlit as st

def show():
    st.markdown('<div class="title">Book a Free Demo Session</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Book a free demo session to learn more about the course and get personalized insights.</div>', unsafe_allow_html=True)

    # Calendly Inline Widget for Demo Session Booking
    st.markdown("""
    <div class="calendly-inline-widget" data-url="https://calendly.com/hawkar_abdulhaq/introduction-to-coding-training-with-hawkar" style="min-width:320px;height:700px;"></div>
    <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
    """, unsafe_allow_html=True)
  
