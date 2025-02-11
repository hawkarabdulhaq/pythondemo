import streamlit as st
import streamlit.components.v1 as components

def show():
    # Full-page HTML with SVG and styling for proper rendering
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <style>
          /* Fullscreen adjustments */
          html, body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
            background-color: black; /* Matches SVG background */
          }

          /* Container to center the SVG */
          .container {
            width: 100vw;
            height: 90vh; /* Adjusted height to fit the full SVG */
            display: flex;
            justify-content: center;
            align-items: center;
          }

          /* SVG fully visible */
          svg {
            max-width: 100%;
            max-height: 100%;
            display: block;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
            <!-- Your Full SVG Content -->
            <defs>
              <linearGradient id="impactWave" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#d3d3d3"/>
                <stop offset="50%" style="stop-color:#d3d3d3"/>
                <stop offset="100%" style="stop-color:#d3d3d3"/>
              </linearGradient>
            </defs>
            <rect width="1200" height="900" fill="#000000"/>
            <text x="50%" y="20%" font-family="Arial" font-size="48" fill="white" text-anchor="middle">
              Utilize AI and Machine Learning Faster and Smarter
            </text>
            <text x="50%" y="80%" font-family="Arial" font-size="24" fill="#A5B4FC" text-anchor="middle">
              Building Tomorrow's Solutions Today
            </text>
          </svg>
        </div>
      </body>
    </html>
    """

    # Increase iframe size to show full SVG
    components.html(html_code, height=900, width=1200, scrolling=False)

    # Add extra space to push the following content lower
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    # Move "Optimizing businesses..." section down
    st.markdown("""
        <div style="margin-top: 80px; text-align: center; font-size: 1.5em; font-weight: bold; color: #eeeeee;">
            Optimizing businesses for resilience and sustainable growth with AI!
        </div>
    """, unsafe_allow_html=True)

    # Move "What We Offer" section down
    st.markdown("""
        <div style="margin-top: 50px; text-align: center; font-size: 2em; font-weight: bold; color: #1ABC9C;">
            What We Offer
        </div>
    """, unsafe_allow_html=True)

    # Offer details section
    st.markdown("""
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
          <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/training.jpg" 
                 alt="Training" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #eeeeee;">Training</h3>
            <p style="color: #ffffff;">Learn AI, Machine Learning, and Automation quickly and effectively.</p>
          </div>
          <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/analyze.jpg" 
                 alt="Analysis" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #eeeeee;">Analysis</h3>
            <p style="color: #ffffff;">We analyze your business and provide a custom data-driven improvement plan.</p>
          </div>
          <div style="background-color: #000000; padding: 20px; border-radius: 10px; width: 30%; margin-bottom: 20px; 
                      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); text-align: center;">
            <img src="https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/solution.jpg" 
                 alt="Solutions" style="border-radius: 10px; margin-bottom: 15px; width: 100%; height: auto;">
            <h3 style="color: #eeeeee;">Solutions</h3>
            <p style="color: #ffffff;">Custom-built tools to solve problems and streamline your operations.</p>
          </div>
        </div>
    """, unsafe_allow_html=True)
