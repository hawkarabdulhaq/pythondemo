import streamlit as st

def show():
    """Display the About Us page."""

    # ---------- Banner ----------
    st.markdown(
        """
        <style>
            /* Re-useable card style */
            .section-card {
                background-color: #111111;
                padding: 35px 25px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.25);
                margin-bottom: 35px;
            }
            /* Nice divider line */
            .divider {
                margin: 40px auto;
                height: 2px;
                width: 60px;
                background: #1ABC9C;
                border: none;
            }
        </style>

        <!-- Banner with dark gradient overlay for legibility -->
        <div style="
            position: relative;
            height: 340px;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 6px 12px rgba(0,0,0,0.35);
        ">
            <div style="
                position: absolute;
                inset: 0;
                background: linear-gradient(
                    rgba(0,0,0,0.65),
                    rgba(0,0,0,0.55)
                ), url('https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/about.jpg') center / cover;
            "></div>

            <div style="
                position: relative;
                z-index: 1;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                color: #ffffff;
            ">
                <h1 style="font-size: 2.7em; font-weight: 800; margin: 0;">
                    About&nbsp;Us
                </h1>
                <p style="font-size: 1.25em; max-width: 800px; margin-top: 10px;">
                    Empowering <b>Climate, Energy &amp; Sustainability</b> sectors with
                    <span style="color:#1ABC9C;">Impact-Driven Coding</span>.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------- Who We Are ----------
    st.markdown(
        """
        <hr class="divider">

        <div class="section-card">
            <h2 style="text-align:center; color:#1ABC9C; margin-top:0;">Who&nbsp;We&nbsp;Are</h2>
            <p style="text-align:center; color:#eeeeee; font-size:1.1em; max-width:850px; margin:0 auto;">
                We’re an <b>AI &amp; Sustainability startup</b> on a mission to fuse advanced machine learning with real-world climate action.
                From optimising renewable-energy portfolios to cutting supply-chain emissions, our focus is simple:
                <em>code that creates measurable impact</em>.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------- Our Mission ----------
    st.markdown(
        """
        <div class="section-card">
            <h2 style="text-align:center; color:#1ABC9C; margin-top:0;">Our&nbsp;Mission</h2>
            <p style="text-align:center; color:#eeeeee; font-size:1.1em; max-width:850px; margin:0 auto;">
                Help organisations in <b>climate tech, energy, and sustainable commerce</b>
                harness AI responsibly—boosting resilience, accelerating decarbonisation,
                and unlocking fresh value from data.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------- Our Approach ----------
    st.markdown(
        """
        <div class="section-card">
            <h2 style="text-align:center; color:#1ABC9C; margin-top:0;">Our&nbsp;Approach&nbsp;—&nbsp;Impact-Driven Coding</h2>
            <ul style="color:#eeeeee; font-size:1.05em; max-width:850px; margin:15px auto; line-height:1.55;">
                <li><b>Proven workflows&nbsp;&rarr;</b> Each pipeline is lab-tested on real datasets before it ever ships.</li>
                <li><b>Domain alignment&nbsp;&rarr;</b> We co-design with climate scientists, energy analysts and ESG leaders.</li>
                <li><b>Rapid iteration&nbsp;&rarr;</b> Agile sprints deliver tangible improvements within weeks, not quarters.</li>
                <li><b>Transparent metrics&nbsp;&rarr;</b> Every project includes carbon-/impact-dashboards so progress is visible to all.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------- Why Sustainability ----------
    st.markdown(
        """
        <div class="section-card">
            <h2 style="text-align:center; color:#1ABC9C; margin-top:0;">Why&nbsp;Sustainability&nbsp;Matters</h2>
            <p style="text-align:center; color:#eeeeee; font-size:1.1em; max-width:850px; margin:0 auto;">
                AI has incredible power—<em>but only when it serves the planet and its people</em>.
                By embedding sustainability principles into every line of code,
                we ensure technology remains a force for good.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------- Call To Action ----------
    st.markdown(
        """
        <hr class="divider">

        <div style="text-align:center;">
            <h2 style="color:#1ABC9C; margin-bottom:10px;">Ready to Build Impact Together?</h2>
            <p style="color:#eeeeee; font-size:1.15em; margin-bottom:25px;">
                Let’s accelerate your AI-for-Good journey—drop us a line and see how
                <b>Impact-Driven Coding</b> can move the needle for your organisation.
            </p>
            <a href="#contact" style="
                background:#1ABC9C; color:#000; padding:12px 28px;
                border-radius:6px; font-weight:bold; text-decoration:none;
                box-shadow:0 3px 6px rgba(0,0,0,0.3);
            ">Get&nbsp;in&nbsp;Touch</a>
        </div>
        """,
        unsafe_allow_html=True
    )
