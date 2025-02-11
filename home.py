import streamlit as st
import streamlit.components.v1 as components

def show():
    # Define SVG with explicit width/height attributes and full viewport usage
    svg_code = """
    <div style="width:100%; overflow: hidden; margin: 0; padding: 0;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="450">
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
            </defs>

            <rect width="800" height="450" fill="#000000"/>
            <g transform="translate(50, 50)" filter="url(#primaryGlow)" opacity="0.3">
                <path d="M0 150 C150 100 250 200 400 150 S700 100 800 150" stroke="url(#impactWave)" stroke-width="2" fill="none">
                    <animate attributeName="d" 
                            dur="8s" 
                            values="M0 150 C150 100 250 200 400 150 S700 100 800 150;
                                    M0 170 C150 120 250 220 400 170 S700 120 800 170;
                                    M0 150 C150 100 250 200 400 150 S700 100 800 150"
                            repeatCount="indefinite"/>
                </path>
            </g>

            <!-- Main Title -->
            <text x="50%" y="40%" text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="32" fill="white" font-weight="bold">
                Utilize AI and Machine Learning Faster and Smarter
            </text>

            <!-- Subtitle -->
            <text x="50%" y="55%" text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="18" fill="#A5B4FC">
                Transform your business into a data-driven, more resilient enterprise with us!
            </text>
        </svg>
    </div>
    """

    # Use Streamlit's components.html to render SVG
    components.html(svg_code, height=450)

    # Remove any extra elements interfering with the banner area
