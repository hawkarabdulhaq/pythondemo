import streamlit as st

def show():
    """Display the Business Analysis page."""
    
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
        <h1 style="margin: 0; font-size: 2.5em; font-weight: bold;">Transform Your Business with Data</h1>
        <p style="margin-top: 10px; font-size: 1.2em;">Make smarter decisions, reduce costs, and boost efficiency.</p>
    </div>
    <hr style="margin: 30px 0; border: none; border-top: 2px solid #1ABC9C;">
    """, unsafe_allow_html=True)

    # What is a Data-Driven Business?
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-bottom: 10px;">
        What is a Data-Driven Business?
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #34495E; margin-bottom: 30px;">
        A data-driven business makes decisions based on insights, not guesswork. Here's why it matters:
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center;">
        <div style="width: 30%; background-color: #000000; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #34495E;">Higher Efficiency</h3>
            <p>Automate processes and optimize workflows to save time.</p>
        </div>
        <div style="width: 30%; background-color: #000000; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #34495E;">Lower Costs</h3>
            <p>Cut unnecessary expenses by improving resource management.</p>
        </div>
        <div style="width: 30%; background-color: #000000; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #34495E;">Smarter Decisions</h3>
            <p>Leverage real-time data to stay ahead of the competition.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Can Your Business Become Data-Driven?
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-top: 40px;">
        Can Your Business Become Data-Driven?
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #34495E; margin-bottom: 30px;">
        Whether you're a startup or a well-established company, data-driven strategies can revolutionize your business.
    </div>
    """, unsafe_allow_html=True)

    # Quick Business Analysis Button
    if st.button("Quick Business Analysis"):
        st.session_state.page = "Business Analysis"  # Redirect to analysis page
        st.experimental_rerun()

    # Need a Data-Driven System?
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; font-weight: bold; color: #1ABC9C; margin-top: 40px;">
        Do You Need a Data-Driven System?
    </div>
    <div style="text-align: center; font-size: 1.2em; color: #34495E; margin-bottom: 30px;">
        We can develop a data-driven strategy and implement it for you.
    </div>
    """, unsafe_allow_html=True)
