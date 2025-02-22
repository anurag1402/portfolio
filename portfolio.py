import streamlit as st
import pandas as pd
from PIL import Image
import base64
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Anurag Anand - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with enhanced styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Enhanced Dark Mode with Gradient */
    .main {
        background: linear-gradient(135deg, #000000, #1a1a1a);
        color: #FFFFFF;
    }
    
    .stApp {
        background: linear-gradient(135deg, #000000, #1a1a1a);
    }
    
    /* Improved Typography */
    .stTitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 4.5rem !important;
        font-weight: 700 !important;
        color: #FFFFFF !important;
        letter-spacing: -0.02em;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.3);
        animation: fadeIn 1s ease-in;
    }
    
    .stSubheader {
        font-size: 2rem !important;
        font-weight: 500 !important;
        color: #FFFFFF !important;
        opacity: 0.9;
        animation: fadeIn 1.2s ease-in;
    }
    
    .section-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 2rem;
        color: #FFFFFF;
        text-shadow: 0 0 15px rgba(0, 255, 255, 0.2);
        position: relative;
        padding-left: 1rem;
        animation: fadeIn 1s ease-in;
    }
    
    .section-title::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 70%;
        background: linear-gradient(to bottom, #00ffff, #ff00ff);
        border-radius: 2px;
    }
    
    /* Enhanced Metric Cards */
    .metric-card {
        background: linear-gradient(145deg, #111111, #1a1a1a);
        padding: 2rem;
        border-radius: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        animation: fadeIn 1.5s ease-in;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #00ffff, #ff00ff);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 30px rgba(0, 255, 255, 0.1);
    }
    
    .metric-card:hover::before {
        transform: scaleX(1);
    }
    
    .metric-card h3 {
        color: #00ffff !important;
        font-size: 3rem;
        margin: 0;
        animation: countUp 2s forwards;
    }
    
    .metric-card i {
        font-size: 2rem;
        color: #00ffff;
        margin-bottom: 1rem;
    }
    
    /* Project Cards with 3D Effect */
    .project-card {
        perspective: 1000px;
        height: 400px;
        margin-bottom: 2rem;
        animation: fadeIn 1.5s ease-in;
    }
    
    .project-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
    }
    
    .project-card:hover .project-card-inner {
        transform: rotateY(180deg);
    }
    
    .project-card-front, .project-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        border-radius: 1rem;
        padding: 2rem;
    }
    
    .project-card-front {
        background: linear-gradient(145deg, #111111, #1a1a1a);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .project-card-back {
        background: linear-gradient(145deg, #1a1a1a, #111111);
        transform: rotateY(180deg);
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    /* Enhanced Sidebar */
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #111111, #1a1a1a);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .nav-link {
        display: flex;
        align-items: center;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0.5rem;
        transition: all 0.3s ease;
        background: rgba(255, 255, 255, 0.05);
        text-decoration: none;
        color: #FFFFFF;
    }
    
    .nav-link:hover {
        background: rgba(0, 255, 255, 0.1);
        transform: translateX(10px);
    }
    
    .nav-link i {
        margin-right: 1rem;
        color: #00ffff;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes countUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Enhanced Form Styling */
    .stTextInput > div > div {
        background-color: #111111;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 0.5rem;
    }
    
    .stTextInput > div > div:focus-within {
        border-color: #00ffff;
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #00ffff, #ff00ff);
        color: #FFFFFF;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 0.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 255, 255, 0.2);
    }
    
    /* Skill Badges */
    .skill-badge {
        display: inline-block;
        padding: 0.75rem 1.5rem;
        margin: 0.5rem;
        border-radius: 2rem;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 255, 255, 0.2);
        color: #FFFFFF;
        font-weight: 500;
        transition: all 0.3s ease;
        animation: fadeIn 1.5s ease-in;
    }
    
    .skill-badge:hover {
        border-color: #00ffff;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
        transform: translateY(-5px);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("Navigation")
    nav = st.radio("", ["Home", "Experience", "Projects", "Skills", "Contact"], 
                   label_visibility="collapsed")
    
    st.markdown("### Download Resume")
    def create_download_link(filename):
        with open(filename, "rb") as file:
            contents = file.read()
            encoded = base64.b64encode(contents).decode()
            href = f'<a href="data:application/pdf;base64,{encoded}" download="{filename}" class="nav-link"><i class="fas fa-download"></i>Download Resume (PDF)</a>'
            return href
    
    st.markdown(create_download_link("/Users/msdan/Downloads/Portfolio/Resume_Anurag_Anand_DS2.pdf"), unsafe_allow_html=True)
    
    st.markdown("### Connect With Me")
    st.markdown('<a href="https://linkedin.com/in/anuraganand1402" class="nav-link"><i class="fab fa-linkedin"></i>LinkedIn</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://github.com/ANURAGANAND14" class="nav-link"><i class="fab fa-github"></i>GitHub</a>', unsafe_allow_html=True)

# Main Content
if nav == "Home":
    # Header Section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Anurag Anand")
        st.subheader("Data Scientist")
        st.write("📍 Mumbai | 📧 anuanand1402@gmail.com | 📱 +918529706039")
    
    with col2:
        profile_image = Image.open("/Users/msdan/Downloads/Portfolio/Passport Size Pic.jpg")
        st.image(profile_image, width=200)
    
    # About Me with Tabs
    st.markdown("## About Me")
    tab1, tab2 = st.tabs(["Professional Summary", "Interests"])
    
    with tab1:
        st.markdown("""
        Results-driven Data Scientist with demonstrated success in implementing and deploying Generative AI and data solutions
        for enterprise applications. Proven track record in delivering production-ready systems that drive operational efficiency
        and data-informed decision-making.
        """)
    
    with tab2:
        st.markdown("""
        - 🏏 **Sports Enthusiast**: Cricket team leadership experience
        - 📚 **Avid Reader**: Focus on technology and management literature
        - 🤖 **AI Research**: Keeping up with latest developments in AI/ML
        - 🎯 **Problem Solving**: Passionate about solving complex technical challenges
        """)

    # Key Metrics with Icons
    st.markdown("## Impact Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="metric-card">
                <i class="fas fa-rocket"></i>
                <h3>13%</h3>
                <p>Onboarding Efficiency Boost</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="metric-card">
                <i class="fas fa-chart-line"></i>
                <h3>21%</h3>
                <p>Ticket Resolution Improvement</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="metric-card">
                <i class="fas fa-users"></i>
                <h3>12%</h3>
                <p>Client Operations Enhancement</p>
            </div>
        """, unsafe_allow_html=True)

elif nav == "Experience":
    st.markdown("## Professional Experience")
    
    st.markdown("""
    <div class="timeline-item">
        <h3>Associate Data Scientist</h3>
        <h4>Blenheim Chalcot (UK's Leading Digital Venture Builder) | 06/2024 - 01/2025</h4>
        <ul>
            <li>Boosted onboarding efficiency by 13% and improved ticket resolution by 21%</li>
            <li>Implemented and deployed 3+ AI-powered automation solutions</li>
            <li>Collaborated with Technical Architect and CXOs to develop 4 multi-Agent & RAG based solutions</li>
            <li>Implemented production-ready solutions using open-source LLMs, Anthropic, Gemini, and OpenAI APIs</li>
        </ul>
    </div>
    
    <div class="timeline-item">
        <h3>System Design Intern</h3>
        <h4>Continental Device India | 07/2023 - 12/2023</h4>
        <ul>
            <li>Reduced component failure rate from 15% to <11%</li>
            <li>Developed and deployed data-driven test automation systems</li>
            <li>Improved testing efficiency by 17%</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif nav == "Projects":
    st.markdown("## Featured Projects")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="project-card">
            <div class="project-card-inner">
                <div class="project-card-front">
                    <h3>Campaign Crafter</h3>
                    <img src="/Users/msdan/Downloads/Portfolio/Screenshot 2025-02-22 at 11.56.26 AM.png" alt="Campaign Crafter Preview" style="max-width: 100%; margin-top: 1rem;">
                </div>
                <div class="project-card-back">
                    <h3>Campaign Crafter</h3>
                    <p>End-to-end automated system for social media campaign generation</p>
                    <ul>
                        <li>Multi-agent AI architecture</li>
                        <li>GPT-4/DALL-E 3 integration</li>
                        <li>Automated content creation</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <div class="project-card-inner">
                <div class="project-card-front">
                    <h3>Chat Analyzer</h3>
                    <img src="/Users/msdan/Downloads/Portfolio/chat_analyzer.gif" alt="Chat Analyzer Preview" style="max-width: 100%; margin-top: 1rem;">
                </div>
                <div class="project-card-back">
                    <h3>Chat Analyzer</h3>
                    <p>Automated chatbot evaluation system</p>
                    <ul>
                        <li>UpTrain LLMops framework</li>
                        <li>Real-time analytics</li>
                        <li>PostgreSQL optimization</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif nav == "Skills":
    st.markdown("## Technical Skills")
    
    # Skills categories with animated badges
    st.markdown("### Programming & Tools")
    st.markdown("""
    <div class="skills-container">
        <span class="skill-badge"><i class="fab fa-python"></i> Python</span>
        <span class="skill-badge"><i class="fas fa-code"></i> C++</span>
        <span class="skill-badge"><i class="fas fa-database"></i> SQL</span>
        <span class="skill-badge"><i class="fas fa-brain"></i> Machine Learning</span>
        <span class="skill-badge"><i class="fas fa-robot"></i> AI</span>
        <span class="skill-badge"><i class="fas fa-project-diagram"></i> DSA</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Frameworks")
    st.markdown("""
    <div class="skills-container">
        <span class="skill-badge"><i class="fas fa-bolt"></i> FastAPI</span>
        <span class="skill-badge"><i class="fas fa-stream"></i> Streamlit</span>
        <span class="skill-badge"><i class="fas fa-comments"></i> Chainlit</span>
        <span class="skill-badge"><i class="fas fa-book"></i> Jupyter</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Tools & Platforms")
    st.markdown("""
    <div class="skills-container">
        <span class="skill-badge"><i class="fas fa-file-excel"></i> Microsoft Excel</span>
        <span class="skill-badge"><i class="fas fa-chart-bar"></i> Power BI</span>
        <span class="skill-badge"><i class="fas fa-database"></i> PostgreSQL</span>
        <span class="skill-badge"><i class="fas fa-keyboard"></i> Prompt Engineering</span>
    </div>
    """, unsafe_allow_html=True)

else:  # Contact
    st.markdown("## Contact Me")
    
    # Enhanced contact form
    with st.form("contact_form"):
        st.markdown("""
        <div class="contact-form">
            <div class="form-group">
                <i class="fas fa-user"></i>
        """, unsafe_allow_html=True)
        name = st.text_input("Name")
        st.markdown("""
            </div>
            <div class="form-group">
                <i class="fas fa-envelope"></i>
        """, unsafe_allow_html=True)
        email = st.text_input("Email")
        st.markdown("""
            </div>
            <div class="form-group">
                <i class="fas fa-comment"></i>
        """, unsafe_allow_html=True)
        message = st.text_area("Message")
        st.markdown("</div>", unsafe_allow_html=True)
        
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            st.success("Thanks for reaching out! I'll get back to you soon.")

# Footer with animated social links
st.markdown("---")
st.markdown("""
<footer style="margin-top: 2rem; padding: 1rem 0; text-align: center;">
    <div style="margin-bottom: 1rem;">
        <a href="https://linkedin.com/in/anuraganand1402" class="social-link" target="_blank">
            <i class="fab fa-linkedin"></i>
        </a>
        <a href="https://github.com/anuraganand14" class="social-link" target="_blank">
            <i class="fab fa-github"></i>
        </a>
    </div>
    <p style="margin: 0;">© 2025 Anurag Anand. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)