import streamlit as st

def show():
    """Display the streamlined Pricing page in the Streamlit app."""

    # Page Title
    st.title("💰 Pricing Plans")
    st.markdown("""
    <div style="text-align: center; font-size: 1.3em; color: #1ABC9C; margin-bottom: 20px;">
        Find the best plan for your AI learning journey. Choose based on your needs!
    </div>
    """, unsafe_allow_html=True)

    # Pricing Cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🎓 Basic Plan ($250)")
        st.write("""
        ✅ 4 weeks of training  
        ✅ 4 theoretical + 4 practical sessions  
        ✅ Hands-on projects  
        ✅ Certification  
        ✅ **Covers Course 1 only**  
        """)
        st.markdown('<a href="https://checkout.revolut.com/pay/8236b9e9-36c4-4692-911b-735aba86a138" target="_blank" style="background-color:#1ABC9C; color:white; padding:10px 20px; border-radius:5px; text-decoration:none; font-size:1.1em;">Buy</a>', unsafe_allow_html=True)

    with col2:
        st.markdown("### 🚀 Pro Plan ($350)")
        st.write("""
        ✅ 6 weeks of training  
        ✅ 6 theoretical + 6 practical sessions  
        ✅ 3 private mentorship sessions  
        ✅ Hands-on AI project support  
        ✅ Certification  
        ✅ **Covers Course 1 & Course 2**  
        """)
        st.markdown('<a href="https://checkout.revolut.com/pay/2080f594-3b59-4e55-808c-1d1c954186a4" target="_blank" style="background-color:#1ABC9C; color:white; padding:10px 20px; border-radius:5px; text-decoration:none; font-size:1.1em;">Buy</a>', unsafe_allow_html=True)

    with col3:
        st.markdown("### 👑 VIP Plan ($900 - $1200)")
        st.write("""
        ✅ 12 months of private coaching  
        ✅ Monthly 1-on-1 mentorship  
        ✅ Career guidance & networking  
        ✅ Personalized AI learning roadmap  
        ✅ Certification  
        ✅ **Covers Course 1 & Course 2**  
        """)
        st.markdown('<a href="https://calendly.com/hawkar_abdulhaq/ai-for-impact" target="_blank" style="background-color:#1ABC9C; color:white; padding:10px 20px; border-radius:5px; text-decoration:none; font-size:1.1em;">Request</a>', unsafe_allow_html=True)

    # Streamlined Feature Comparison Table
    st.markdown("### 📊 Compare Plans")
    st.markdown("""
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 1.1em;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: center;
            padding: 10px;
        }
        th {
            background-color: #1ABC9C;
            color: white;
        }
    </style>
    <table>
        <tr>
            <th>Feature</th>
            <th>Basic ($250)</th>
            <th>Pro ($350)</th>
            <th>VIP ($900 - $1200)</th>
        </tr>
        <tr>
            <td><strong>Duration</strong></td>
            <td>4 Weeks</td>
            <td>6 Weeks</td>
            <td>12 Months</td>
        </tr>
        <tr>
            <td><strong>Live Theoretical Sessions</strong></td>
            <td>✅ 4</td>
            <td>✅ 6</td>
            <td>✅ 6</td>
        </tr>
        <tr>
            <td><strong>Project-Based Learning</strong></td>
            <td>✅ Yes</td>
            <td>✅ Yes</td>
            <td>✅ Yes</td>
        </tr>
        <tr>
            <td><strong>Live Practical Sessions</strong></td>
            <td>✅ 4</td>
            <td>✅ 6</td>
            <td>✅ 6</td>
        </tr>
        <tr>
            <td><strong>Certificate</strong></td>
            <td>✅ Yes</td>
            <td>✅ Yes</td>
            <td>✅ Yes</td>
        </tr>
        <tr>
            <td><strong>Career Guidance</strong></td>
            <td>❌</td>
            <td>❌</td>
            <td>✅ Personalized</td>
        </tr>
        <tr>
            <td><strong>Certifications</strong></td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td><strong>Best For</strong></td>
            <td>Beginners who want structured learning</td>
            <td>Learners who need mentorship</td>
            <td>Professionals seeking career coaching</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
