import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    /* Keep default font as Courier for general elements */
    * {
        font-family: "Courier", monospace;
    }
    
    /* Light theme styles */
    :root {
        --bg-color: #FFFFFF;
        --text-color: #2C3E50;
        --section-title-color: #34495E;
        --highlight-color: #1ABC9C;
        --border-color: #34495E;
    }

    /* Dark theme styles */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-color: #1E1E1E;
            --text-color: #F0F0F0;
            --section-title-color: #F0F0F0;
            --highlight-color: #4DC9B2;
            --border-color: #4DC9B2;
        }
    }

    /* Responsive styling */
    @media only screen and (max-width: 768px) {
        .title { font-size: 2em; }
        .section-title { font-size: 1.5em; }
        .content { font-size: 1em; }
        .video-container { padding: 5px; }
        iframe { width: 100%; height: auto; }
    }

    /* General body styling */
    body {
        background-color: var(--bg-color);
        color: var(--text-color);
    }

    /* Title Styling */
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: var(--text-color);
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    /* Section Titles */
    .section-title {
        font-size: 1.7em;
        font-weight: bold;
        color: var(--section-title-color);
        margin-top: 30px;
        margin-bottom: 10px;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 5px;
        text-align: left;
    }
    
    /* Content Styling */
    .content {
        font-size: 1.1em;
        color: var(--text-color);
        line-height: 1.6;
        text-align: justify;
        margin-bottom: 20px;
    }

    /* Highlight Section */
    .highlight {
        font-weight: bold;
        color: var(--highlight-color);
    }
    
    /* Video Container Styling */
    .video-container {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
        background-color: var(--bg-color);
        padding: 10px;
        border-radius: 8px;
    }

    /* Responsive iframe for video */
    iframe {
        max-width: 100%;
        width: 100%;
        height: auto;
        border: 2px solid var(--border-color);
        border-radius: 8px;
    }

    /* Pricing Container Specifics */
    .pricing-box {
        font-size: 0.9em; /* Adjusted for tighter fit in pricing boxes */
        padding: 20px;
        border-radius: 10px;
        background-color: #f4f8fb;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    /* Specific styling for list items in pricing boxes */
    .pricing-feature {
        margin: 5px 0;
        white-space: nowrap; /* Prevents text wrapping within list items */
        font-size: 0.9em; /* Slightly smaller for tight containers */
    }
    </style>
    """, unsafe_allow_html=True)
