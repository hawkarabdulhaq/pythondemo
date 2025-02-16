import streamlit as st

def show():
    """Display the Steps-to-Impact page."""
    
    # Banner Section with Background Image
    st.markdown(f"""
    <div style="
        position: relative;
        text-align: center;
        color: white;
        height: 300px;
        background-image: url('https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/waves.jpg');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    ">
        <h1 style="margin: 0; font-size: 2.5em; font-weight: bold;">Steps-to-Impact: Transform Your Business with Data</h1>
        <p style="margin-top: 10px; font-size: 1.2em;">Empower your decisions, reduce costs, and drive sustainable growth.</p>
    </div>
    <hr style="margin: 30px 0; border: none; border-top: 2px solid #1ABC9C;">
    """, unsafe_allow_html=True)

    # What is a Data-Driven Business?
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-bottom: 10px;">
        Introducing Steps-to-Impact
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #eeeeee; margin-bottom: 30px;">
        Our structured approach for guiding your business from guesswork to data-driven excellence.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center;">
        <div style="width: 30%; background-color: #000000; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #eeeeee;">Higher Efficiency</h3>
            <p>Optimize workflows, reduce manual tasks, and increase team productivity.</p>
        </div>
        <div style="width: 30%; background-color: #000000; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #eeeeee;">Smarter Decisions</h3>
            <p>Base every choice on real-time insights, not gut feelings.</p>
        </div>
        <div style="width: 30%; background-color: #000000; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #eeeeee;">Lasting Impact</h3>
            <p>Implement data strategies that deliver measurable, long-term results.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Can Your Business Become Data-Driven?
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-top: 40px;">
        Ready to Take the First Step?
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #eeeeee; margin-bottom: 30px;">
        From startups to established enterprises, our Steps-to-Impact framework can transform your organization's potential.
    </div>
    """, unsafe_allow_html=True)

    # Quick Steps-to-Impact Analysis Button
    if st.button("Quick Steps-to-Impact Analysis"):
        st.session_state.page = "Business Analysis"  # Or any relevant page ID you want to navigate to
        st.experimental_rerun()

    # Need a Data-Driven System?
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-top: 40px;">
        Want a Data-Driven System You Can Count On?
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #eeeeee; margin-bottom: 30px;">
        Let us design and implement your personalized Steps-to-Impact plan.
    </div>
    """, unsafe_allow_html=True)
