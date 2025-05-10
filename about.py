import streamlit as st

def show():
    """Display the About Us page – cleaned-up and button-free."""

    # 1️⃣  Global CSS
    st.markdown(
        """
        <style>
            .banner{
                position:relative;height:340px;border-radius:12px;
                overflow:hidden;box-shadow:0 6px 12px rgba(0,0,0,.35);
            }
            .banner::before{
                content:"";position:absolute;inset:0;
                background:linear-gradient(rgba(0,0,0,.65),rgba(0,0,0,.55)),
                           url('https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/about.jpg')
                           center/cover;
            }
            .banner-content{
                position:relative;z-index:1;height:100%;
                display:flex;flex-direction:column;justify-content:center;
                align-items:center;text-align:center;color:#fff;
            }
            .card{
                background:#111;padding:35px 25px;border-radius:10px;
                box-shadow:0 4px 10px rgba(0,0,0,.25);margin-bottom:35px;
            }
            .divider{
                margin:40px auto;height:2px;width:60px;background:#1ABC9C;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 2️⃣  Banner
    st.markdown(
        """
        <div class="banner">
            <div class="banner-content">
                <h1 style="font-size:2.7em;font-weight:800;margin:0;">About&nbsp;Us</h1>
                <p style="font-size:1.25em;max-width:800px;margin-top:10px;">
                    Empowering <b>Climate, Energy &amp; Sustainability</b> sectors with
                    <span style="color:#1ABC9C;">Impact-Driven Coding</span>.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # 3️⃣  Content cards
    st.markdown(
        """
        <div class="card">
            <h2 style="text-align:center;color:#1ABC9C;margin-top:0;">Who&nbsp;We&nbsp;Are</h2>
            <p style="text-align:center;color:#eeeeee;font-size:1.1em;max-width:850px;margin:0 auto;">
                We’re an <b>AI &amp; Sustainability startup</b> on a mission to blend advanced
                machine learning with tangible climate action. Our focus is simple:
                <i>code that creates measurable impact</i>.
            </p>
        </div>

        <div class="card">
            <h2 style="text-align:center;color:#1ABC9C;margin-top:0;">Our&nbsp;Mission</h2>
            <p style="text-align:center;color:#eeeeee;font-size:1.1em;max-width:850px;margin:0 auto;">
                Help organisations in <b>climate tech, energy, and sustainable commerce</b>
                harness AI responsibly—boosting resilience, accelerating decarbonisation,
                and unlocking fresh value from data.
            </p>
        </div>

        <div class="card">
            <h2 style="text-align:center;color:#1ABC9C;margin-top:0;">Our&nbsp;Approach — Impact-Driven&nbsp;Coding</h2>
            <ul style="color:#eeeeee;font-size:1.05em;max-width:850px;margin:15px auto;line-height:1.55;">
                <li><b>Proven workflows:</b> lab-tested on real datasets before they ship</li>
                <li><b>Domain alignment:</b> co-designed with scientists &amp; ESG leaders</li>
                <li><b>Rapid iteration:</b> tangible improvements in weeks, not quarters</li>
                <li><b>Transparent metrics:</b> every project ships with impact dashboards</li>
            </ul>
        </div>

        <div class="card">
            <h2 style="text-align:center;color:#1ABC9C;margin-top:0;">Why&nbsp;Sustainability&nbsp;Matters</h2>
            <p style="text-align:center;color:#eeeeee;font-size:1.1em;max-width:850px;margin:0 auto;">
                AI is powerful—<i>but only when it serves the planet and its people</i>.
                By embedding sustainability principles into every line of code,
                we ensure technology remains a force for good.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 4️⃣  CTA (heading + text only—button removed)
    st.markdown(
        """
        <hr class="divider">
        <div style="text-align:center;">
            <h2 style="color:#1ABC9C;margin-bottom:10px;">Ready to Build Impact Together?</h2>
            <p style="color:#eeeeee;font-size:1.15em;margin-bottom:0;">
                Let’s accelerate your AI-for-Good journey—reach out and discover how
                <b>Impact-Driven Coding</b> can move the needle for your organisation.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
