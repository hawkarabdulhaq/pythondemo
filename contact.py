import streamlit as st

def show():
    """Display the embedded Calendly widget."""
    st.markdown("""
    <!-- Calendly inline widget begin -->
    <div class="calendly-inline-widget" data-url="https://calendly.com/hawkar_abdulhaq/ai-for-impact?background_color=010000&text_color=fcf8f8&primary_color=129729" style="min-width:320px;height:700px;"></div>
    <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
    <!-- Calendly inline widget end -->
    """, unsafe_allow_html=True)
