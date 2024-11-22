import streamlit as st

def show():
    # Display the title
    st.markdown('<div class="title">About Me</div>', unsafe_allow_html=True)
    
    # Display the profile photo
    st.image("input/me.jpg", width=250, caption="Hawkar Ali Abdulhaq – PhD Candidate, Founder & Entrepreneur", use_column_width="auto")
    
    # Profile Overview
    st.markdown("""
    <div class="content">
        I am a PhD candidate and green entrepreneur committed to pioneering sustainable energy solutions and driving climate resilience. My journey bridges academic research with impactful projects, creating real environmental change through innovative leadership. Follow my journey for insights into sustainability, climate technology, and the future of energy.
    </div>
    """, unsafe_allow_html=True)
    
    # Section: Early Career and Education
    st.markdown("""
    <div class="section-title">Early Career and Education</div>
    <div class="content">
        My professional journey began in 2011 as a geologist in the Kurdistan Region of Iraq. In 2015, I transitioned to Hungary to study Earth Science Engineering at the University of Miskolc, expanding my knowledge and expertise. By 2017, I returned to Kurdistan to collaborate with a research team at the University of Kurdistan, focusing on renewing the geological map of the region.
    </div>
    """, unsafe_allow_html=True)
    
    # Section: Hasar Organization and PhD Studies
    st.markdown("""
    <div class="section-title">Founding Hasar Organization and PhD Studies</div>
    <div class="content">
        In 2019, I founded <a href="https://hasar.org" target="_blank" style="color: #1ABC9C;"><strong>Hasar Organization</strong></a>, Iraq's first climate-focused organization dedicated to carbon removal through nature-based solutions. My work here focuses on advocating for climate adaptation, driving mitigation efforts, and making tangible environmental impacts. I began my PhD at the University of Szeged in 2021, where I am also a research assistant.
    </div>
    """, unsafe_allow_html=True)
    
    # Section: Research and Publications
    st.markdown("""
    <div class="section-title">Research and Publications</div>
    <div class="content">
        My research spans geothermal energy, geology, and climate change, with a significant focus on mineral exploration. My <a href="https://scholar.google.com/" target="_blank" style="color: #1ABC9C;">Google Scholar profile</a> provides a comprehensive list of my work, where I publish as both author and co-author. Notable recent publications include:
        <ul>
            <li><strong>Harnessing Geothermal Energy in Hungary</strong> - Szanyi, J., Kovács, B., and Abdulhaq, H.A., 2025</li>
            <li><strong>Transforming Abandoned Hydrocarbon Fields into Heat Storage Solutions</strong> - Abdulhaq, H.A., Geiger, J., Vass, I., et al., 2024</li>
            <li><strong>Geothermal Energy and Its Potential for Critical Metal Extraction</strong> - Szanyi, J., Rybach, L., and Abdulhaq, H.A., 2023</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Section: A Passion for Coding and Innovation
    st.markdown("""
    <div class="section-title">A Passion for Coding and Innovation</div>
    <div class="content">
        Coding has become integral to my research, allowing for advanced data analysis and supporting sustainable solutions. The Python programming course I developed is part of my vision to foster a skilled network of programmers within my community, supporting digital transformation and climate-tech innovation.
    </div>
    """, unsafe_allow_html=True)
    
    # Section: Entrepreneurial Ventures
    st.markdown("""
    <div class="section-title">Entrepreneurial Ventures</div>
    <div class="content">
        Beyond academia, I co-founded <a href="https://releafs.co" target="_blank" style="color: #1ABC9C;"><strong>Releafs.co</strong></a> and <a href="https://gridx.cc" target="_blank" style="color: #1ABC9C;"><strong>Gridx</strong></a>. Recently, I launched a Python programming and automation course, part of my broader goal to cultivate a network of programmers who can contribute to our community's digital and sustainable transformation.
    </div>
    """, unsafe_allow_html=True)
    
    # Section: Call to Action
    st.markdown("""
    <div class="content" style="margin-top: 40px;">
        <p>Through my work, I aim to bridge research and practical applications, providing insights and inspiring actionable solutions for a resilient future.</p>
    </div>
    """, unsafe_allow_html=True)
