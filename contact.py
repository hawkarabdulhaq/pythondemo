import streamlit as st

def show():
    """Alternative solution using Calendly's script with fixed height"""
    st.markdown("""
    <div class="calendly-inline-widget" 
         data-url="https://calendly.com/hawkar_abdulhaq/ai-for-impact?background_color=373737&text_color=fcf8f8&primary_color=129729" 
         style="min-width:320px;height:100vh;overflow:auto">
    </div>
    <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
    <style>
        .calendly-inline-widget {
            min-height: 700px !important;
        }
    </style>
    """, unsafe_allow_html=True)
