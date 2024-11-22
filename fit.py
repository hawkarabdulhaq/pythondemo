import streamlit as st
from dictionary import translate  # Import the centralized translate function

def show():
    language = st.session_state.language  # Retrieve the selected language

    # Title Section
    st.markdown(f'<div class="title">{translate("fit_title", language)}</div>', unsafe_allow_html=True)

    # Create tabs for Individuals and Enterprises
    tab1, tab2 = st.tabs([translate("individuals_tab", language), translate("enterprises_tab", language)])

    # Individual Tab Content
    with tab1:
        st.markdown(f"""
        <div class="content">
            {translate("individuals_intro", language)}
        </div>
        """, unsafe_allow_html=True)

        # Objectives Section
        st.markdown(f"<h3>{translate('objectives_title', language)}</h3>", unsafe_allow_html=True)
        st.markdown(f"""
        <ul>
            <li><strong>{translate("objective_1", language)}</strong></li>
            <li><strong>{translate("objective_2", language)}</strong></li>
            <li><strong>{translate("objective_3", language)}</strong></li>
            <li><strong>{translate("objective_4", language)}</strong></li>
        </ul>
        """, unsafe_allow_html=True)

        # Class Overview Table for Individuals
        st.markdown(f"<h3>{translate('class_overview_title', language)}</h3>", unsafe_allow_html=True)
        st.markdown(f"""
        <table style="width:100%; border-collapse: collapse; margin-bottom: 20px;">
            <tr style="border-bottom: 1px solid var(--border-color);">
                <th style="text-align: left; padding: 10px;"><strong>{translate("class_column", language)}</strong></th>
                <th style="text-align: left; padding: 10px;"><strong>{translate("title_column", language)}</strong></th>
                <th style="text-align: left; padding: 10px;"><strong>{translate("description_column", language)}</strong></th>
            </tr>
            <tr>
                <td style="padding: 10px;">A</td>
                <td style="padding: 10px;">{translate("class_a_title", language)}</td>
                <td style="padding: 10px;">{translate("class_a_description", language)}</td>
            </tr>
            <tr>
                <td style="padding: 10px;">B</td>
                <td style="padding: 10px;">{translate("class_b_title", language)}</td>
                <td style="padding: 10px;">{translate("class_b_description", language)}</td>
            </tr>
            <tr>
                <td style="padding: 10px;">C</td>
                <td style="padding: 10px;">{translate("class_c_title", language)}</td>
                <td style="padding: 10px;">{translate("class_c_description", language)}</td>
            </tr>
            <tr>
                <td style="padding: 10px;">D</td>
                <td style="padding: 10px;">{translate("class_d_title", language)}</td>
                <td style="padding: 10px;">{translate("class_d_description", language)}</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)

        # How It Works Section
        st.markdown(f"<h3>{translate('workflow_title', language)}</h3>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="content">
            <ol>
                <li><strong>{translate("workflow_step_1", language)}</strong></li>
                <li><strong>{translate("workflow_step_2", language)}</strong></li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

        # Highlighted Button to Survey for Individuals
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://docs.google.com/forms/d/e/1FAIpQLScHcfqWZ_-mkfuNpq7hBQQNzqmIX3oHlsE0UAAlIAe7FGaRdw/viewform?usp=sf_link" target="_blank" style="display: inline-block; padding: 12px 24px; font-size: 1.2em; font-weight: bold; color: white; background-color: #1ABC9C; border-radius: 5px; text-decoration: none;">
                {translate("individual_button", language)}
            </a>
        </div>
        """, unsafe_allow_html=True)

    # Enterprises Tab Content
    with tab2:
        st.markdown(f"""
        <div class="content">
            {translate("enterprises_intro", language)}
        </div>
        """, unsafe_allow_html=True)

        # Highlighted Button to Survey for Enterprises
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSekdOWoJsM1KCzz6lnhDNjiDHmN7jAvp3yp-cJyie1zeT0-Eg/viewform?usp=sf_link" target="_blank" style="display: inline-block; padding: 12px 24px; font-size: 1.2em; font-weight: bold; color: white; background-color: #1ABC9C; border-radius: 5px; text-decoration: none;">
                {translate("enterprise_button", language)}
            </a>
        </div>
        """, unsafe_allow_html=True)
