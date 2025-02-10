import streamlit as st

def show():
    # Display SVG Animation
    svg_code = """
    <div style="text-align: center;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%">
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

            <g transform="translate(50, 50)" filter="url(#primaryGlow)" opacity="0.3">
                <path d="M0 150 C150 100 250 200 400 150 S700 100 800 150" 
                      stroke="url(#impactWave)" stroke-width="2" fill="none">
                    <animate attributeName="d" 
                             dur="8s" 
                             values="M0 150 C150 100 250 200 400 150 S700 100 800 150;
                                    M0 170 C150 120 250 220 400 170 S700 120 800 170;
                                    M0 150 C150 100 250 200 400 150 S700 100 800 150"
                             repeatCount="indefinite"/>
                </path>
            </g>

            <g transform="translate(400, 80)" filter="url(#primaryGlow)">
                <text text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="32" 
                      fill="#FFFFFF" font-weight="bold">
                    Utilize AI and Machine Learning Faster and Smarter
                    <animate attributeName="opacity" values="0.9;1;0.9" dur="4s" repeatCount="indefinite"/>
                </text>
            </g>

            <g transform="translate(400, 330)" filter="url(#primaryGlow)">
                <text text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="24" fill="#A5B4FC">
                    Building Tomorrow's Solutions Today
                    <animate attributeName="fill" values="#A5B4FC;#818CF8;#A5B4FC" dur="6s" repeatCount="indefinite"/>
                </text>
            </g>
        </svg>
    </div>
    """
    
    st.markdown(svg_code, unsafe_allow_html=True)

