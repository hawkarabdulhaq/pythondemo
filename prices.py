import streamlit as st

def show():
    """Display the Pricing page in the Streamlit app."""

    # Page Title
    st.title("💰 Pricing Plans")
    st.markdown("""
    <div style="text-align: center; font-size: 1.3em; color: #1ABC9C; margin-bottom: 20px;">
        Find the best plan for your AI learning journey. Choose based on your needs!
    </div>
    """, unsafe_allow_html=True)

    # Pricing Table with Visuals
    col1, col2, col3 = st.columns(3)

    # Basic Plan
    with col1:
        st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/basic.jpg", use_container_width=True)
        st.markdown("### 🎓 Basic Plan ($250)")
        st.write("""
        ✅ 4 weeks of training  
        ✅ 4 theoretical + 4 practical sessions  
        ✅ Hands-on projects  
        ✅ Certification  
        """)
        st.markdown('<a href="https://calendly.com/hawkar_abdulhaq/ai-for-impact" target="_blank" style="background-color:#1ABC9C; color:white; padding:10px 20px; border-radius:5px; text-decoration:none; font-size:1.1em;">Request</a>', unsafe_allow_html=True)

    # Pro Plan
    with col2:
        st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/pro.jpg", use_container_width=True)
        st.markdown("### 🚀 Pro Plan ($350)")
        st.write("""
        ✅ 6 weeks of training  
        ✅ 6 theoretical + 6 practical sessions  
        ✅ 3 private mentorship sessions  
        ✅ Hands-on AI project support  
        ✅ Certification  
        """)
        st.markdown('<a href="https://calendly.com/hawkar_abdulhaq/ai-for-impact" target="_blank" style="background-color:#1ABC9C; color:white; padding:10px 20px; border-radius:5px; text-decoration:none; font-size:1.1em;">Request</a>', unsafe_allow_html=True)

    # VIP Plan
    with col3:
        st.image("https://raw.githubusercontent.com/hawkarabdulhaq/pythondemo/main/input/vip.jpg", use_container_width=True)
        st.markdown("### 👑 VIP Plan ($900 - $1200)")
        st.write("""
        ✅ 12 months of private coaching  
        ✅ Monthly 1-on-1 mentorship  
        ✅ Career guidance & networking  
        ✅ Personalized AI learning roadmap  
        ✅ Certification  
        """)
        st.markdown('<a href="https://calendly.com/hawkar_abdulhaq/ai-for-impact" target="_blank" style="background-color:#1ABC9C; color:white; padding:10px 20px; border-radius:5px; text-decoration:none; font-size:1.1em;">Request</a>', unsafe_allow_html=True)

    # Detailed Feature Comparison Table
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
            <td><strong>Live Practical Sessions</strong></td>
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
            <td><strong>Mentorship Sessions</strong></td>
            <td>❌ No</td>
            <td>✅ 3</td>
            <td>✅ Ongoing</td>
        </tr>
        <tr>
            <td><strong>Private Coaching</strong></td>
            <td>❌ No</td>
            <td>❌ No</td>
            <td>✅ Monthly 1-on-1</td>
        </tr>
        <tr>
            <td><strong>Career Guidance</strong></td>
            <td>❌ No</td>
            <td>❌ No</td>
            <td>✅ Personalized</td>
        </tr>
        <tr>
            <td><strong>Certification</strong></td>
            <td>✅ Yes</td>
            <td>✅ Yes</td>
            <td>✅ Yes</td>
        </tr>
        <tr>
            <td><strong>Best For</strong></td>
            <td>Beginners who want structured learning</td>
            <td>Learners who need mentorship</td>
            <td>Professionals seeking career coaching</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; font-size: 0.9em; color: #7F8C8D;">
        releafs.co © 2024
    </div>
    """, unsafe_allow_html=True)
