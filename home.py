import streamlit as st

def show():
    # SVG Banner Section - Properly encoded as a string
    svg_html = '''
    <div style="text-align: center; background-color: #000000; padding: 20px; border-radius: 10px; margin-bottom: 30px;">
        <svg width="100%" height="450" viewBox="0 0 800 450" style="max-width: 800px;" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="impactWave" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" style="stop-color:#d3d3d3"/>
                    <stop offset="50%" style="stop-color:#d3d3d3"/>
                    <stop offset="100%" style="stop-color:#d3d3d3"/>
                </linearGradient>
                <filter id="primaryGlow" x="-50%" y="-50%" width="200%" height="200%">
                    <feGaussianBlur stdDeviation="4" result="blur"/>
                    <feFlood flood-color="#d3d3d3" flood-opacity="0.3" result="color"/>
                    <feComposite in="color" in2="blur" operator="in" result="glow"/>
                    <feMerge>
                        <feMergeNode in="glow"/>
                        <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                </filter>
                <pattern id="techGrid" x="0" y="0" width="50" height="50" patternUnits="userSpaceOnUse">
                    <path d="M25 0 v50 M0 25 h50" stroke="#4B5563" stroke-width="0.5" opacity="0.15"/>
                    <circle cx="25" cy="25" r="1" fill="#4B5563" opacity="0.2"/>
                </pattern>
            </defs>
            <rect width="800" height="450" fill="#000000"/>
            <rect width="800" height="450" fill="url(#techGrid)"/>
            <g transform="translate(400, 80)" filter="url(#primaryGlow)">
                <text text-anchor="middle" font-family="Arial, sans-serif" font-size="32" fill="#FFFFFF" font-weight="bold">
                    Utilize AI and Machine Learning Faster and Smarter
                </text>
            </g>
            <g transform="translate(400, 330)" filter="url(#primaryGlow)">
                <text text-anchor="middle" font-family="Arial, sans-serif" font-size="24" fill="#A5B4FC">
                    Building Tomorrow&#39;s Solutions Today
                </text>
            </g>
            <g transform="translate(400, 360)" filter="url(#primaryGlow)">
                <text text-anchor="middle" font-family="Arial, sans-serif" font-size="16" fill="#6366F1">
                    Python • Web Apps • Machine Learning • Data Analysis • Google Colab
                </text>
            </g>
            <g transform="translate(400, 420)" filter="url(#primaryGlow)">
                <text text-anchor="middle" font-family="Arial, sans-serif" font-size="18" fill="#FFFFFF">
                    Transform your business into a data-driven, more resilient enterprise with us!
                </text>
            </g>
        </svg>
    </div>
    '''
    
    st.markdown(svg_html, unsafe_allow_html=True)

    # Subtitle
    st.markdown("""
    <div style="text-align: center; font-size: 1.5em; font-weight: bold; color: #eeeeee; margin-bottom: 20px;">
        Optimizing businesses for resilience and sustainable growth with AI!
    </div>
    """, unsafe_allow_html=True)

    # What We Offer Section
    st.markdown("""
    <div style="text-align: center; font-size: 2em; font-weight: bold; color: #1ABC9C; margin-bottom: 20px;">
        What We Offer
    </div>
    """, unsafe_allow_html=True)

    # Offer Details
    st.markdown("""
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
        <div style="background-color: ##000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg" alt="Training" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #eeeeee;">Training</h3>
            <p>Learn AI, Machine Learning, and Automation quickly and effectively.</p>
        </div>
        <div style="background-color: ##000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg" alt="Analysis" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #eeeeee;">Analysis</h3>
            <p>We analyze your business and provide a custom data-driven improvement plan.</p>
        </div>
        <div style="background-color: ##000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg" alt="Solutions" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #eeeeee;">Solutions</h3>
            <p>Custom-built tools to solve problems and streamline your operations.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
