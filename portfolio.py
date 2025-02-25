import streamlit as st
from PIL import Image
import base64
import random
import urllib.parse
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Anurag Anand | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        /* Global styles */
        [data-testid="stAppViewContainer"] {
            background-color: #0a192f;
            color: #e6f1ff;
        }

        .main-title {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            color: #64ffda;
        }

        .sub-title {
            font-size: 1.5rem;
            font-weight: 400;
            color: #8892b0;
            margin-bottom: 2rem;
        }

        .section-title {
            font-size: 1.75rem;
            font-weight: 700;
            color: #ccd6f6;
            margin-bottom: 1rem;
            border-bottom: 2px solid #64ffda;
            padding-bottom: 0.5rem;
        }

        .highlight {
            color: #64ffda;
            font-weight: 600;
        }

        .card {
            background-color: #112240;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border-left: 3px solid #64ffda;
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px -15px rgba(2, 12, 27, 0.7);
        }

        .card-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #e6f1ff;
            margin-bottom: 0.5rem;
        }

        .card-subtitle {
            font-size: 0.9rem;
            color: #64ffda;
            margin-bottom: 1rem;
        }

        .bullet-point {
            margin-bottom: 0.5rem;
            position: relative;
            padding-left: 1.5rem;
        }

        .bullet-point:before {
            content: "▹";
            position: absolute;
            left: 0;
            color: #64ffda;
        }

        .contact-link {
            color: #64ffda;
            text-decoration: none;
            transition: color 0.3s;
            font-weight: 500;
        }

        .contact-link:hover {
            color: #ffffff;
        }

        /* Custom sidebar */
        [data-testid="stSidebar"] {
            background-color: #112240;
            padding-top: 2rem;
        }

        .sidebar-info {
            padding: 1rem;
            text-align: center;
        }

        .sidebar-name {
            font-size: 1.5rem;
            font-weight: 700;
            margin: 1rem 0;
            color: #ccd6f6;
        }

        .sidebar-role {
            font-size: 1rem;
            color: #64ffda;
            margin-bottom: 1rem;
        }

        .skill-tag {
            background-color: #233554;
            color: #64ffda;
            padding: 0.3rem 0.6rem;
            border-radius: 5px;
            display: inline-block;
            margin: 0.25rem;
            font-size: 0.8rem;
        }

        /* Skills animation */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }

        .animated-skill {
            animation: float 3s ease-in-out infinite;
        }

        /* Timeline styling */
        .timeline-container {
            position: relative;
            padding-left: 40px;
            margin-top: 30px;
        }

        .timeline-container:before {
            content: '';
            position: absolute;
            left: 10px;
            top: 0;
            bottom: 0;
            width: 4px;
            background-color: #64ffda;
        }

        .timeline-item {
            margin-bottom: 40px;
            position: relative;
        }

        .timeline-dot {
            position: absolute;
            left: -40px;
            top: 5px;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background-color: #64ffda;
            z-index: 1;
        }

        .timeline-content {
            background-color: #112240;
            border-radius: 8px;
            padding: 20px;
            border-left: 3px solid #64ffda;
        }

        .timeline-date {
            font-weight: 700;
            font-size: 1.2rem;
            color: #ccd6f6;
            margin: 0 0 10px 0;
        }

        .timeline-title {
            font-weight: 600;
            color: #64ffda;
            margin: 0 0 10px 0;
        }

        /* Navigation styling */
        .stRadio > div {
            display: flex;
            flex-direction: column;
        }

        .stRadio > div > label {
            background-color: #112240;
            margin: 5px 0;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
            border-left: 3px solid transparent;
        }

        .stRadio > div > label:hover {
            background-color: #1a365d;
            border-left: 3px solid #64ffda;
        }

        .stRadio > div > label[data-baseweb="radio"] > div {
            background-color: #64ffda !important;
        }

        /* Project link button */
        .project-link {
            display: inline-block;
            background-color: #233554;
            color: #64ffda;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            text-decoration: none;
            margin-top: 1rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .project-link:hover {
            background-color: rgba(100, 255, 218, 0.1);
            transform: translateY(-2px);
        }

        /* Resume download button */
        .resume-button {
            display: inline-block;
            background-color: #64ffda;
            color: #112240;
            padding: 0.75rem 1.5rem;
            border-radius: 5px;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
            margin-top: 1rem;
        }

        .resume-button:hover {
            background-color: #4dd5bf;
        }

        /* Mobile responsiveness */
        @media screen and (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            .sub-title {
                font-size: 1.2rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar content
def sidebar():
    with st.sidebar:
        st.markdown('<div class="sidebar-info">', unsafe_allow_html=True)

        # Static profile image
        st.image("profile.jpg", width=150)

        st.markdown('<div class="sidebar-name">Anurag Anand</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-role">Data Scientist</div>', unsafe_allow_html=True)

        st.markdown("**Location:** Mumbai, India")
        st.markdown("**Email:** anuanand1402@gmail.com")
        st.markdown("**Phone:** +918529706039")

        st.markdown("### Connect")
        st.markdown("[LinkedIn](https://linkedin.com/in/anuraganand1402)")

        st.markdown("### Skills")
        skills = [
            "Python", "C++", "SQL", "Machine Learning", "AI",
            "FastAPI", "Streamlit", "Chainlit", "Jupyter",
            "Data Structures", "Algorithms", "PostgreSQL",
            "Prompt Engineering", "Statistical Analysis"
        ]

        skill_html = ""
        for skill in skills:
            delay = random.uniform(0, 5)
            skill_html += f'<span class="skill-tag animated-skill" style="animation-delay: {delay}s">{skill}</span>'

        st.markdown(f'<div style="line-height: 2.5;">{skill_html}</div>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Navigation menu with better styling
        st.markdown("### Navigation")
        nav_options = ["About", "Experience", "Projects", "Education", "Journey", "Contact"]

        nav = st.radio("", nav_options, label_visibility="collapsed")
        return nav

# Header section
def header():
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="main-title">Hello, I\'m Anurag Anand.</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">Building intelligent solutions with data science & AI.</div>', unsafe_allow_html=True)
    
        st.markdown("""
        Results-driven **Data Scientist** with demonstrated success in implementing and deploying
        Generative AI and data solutions for enterprise applications. Proven track record in delivering
        production-ready systems that drive operational efficiency and data-informed decision-making.
        """)
    
        # Additional professional summary
        st.markdown("""
        <div style="margin-top: 1.5rem;">
            <p>I specialize in building <span class="highlight">end-to-end AI solutions</span> that transform business
            operations through intelligent automation. My expertise includes:</p>
    
        <ul style="list-style-type: none; padding-left: 0;">
                <li class="bullet-point">Building and automating data pipelines using Python (Pandas, SQL) and cloud tools like Azure</li>
                <li class="bullet-point">Training and fine-tuning machine learning models using Scikit-learn, PyTorch</li>
                <li class="bullet-point">Implementing Retrieval-Augmented Generation (RAG) systems using LangChain and vector databases</li>
                <li class="bullet-point">Developing dashboards and visualizations with Tableau, Power BI, or Matplotlib to present insights</li>
                <li class="bullet-point">Optimizing Large Language Models (LLMs) with prompt engineering and parameter tuning</li>
            </ul>
    
        <p style="margin-top: 1rem; font-size: 1.2rem; font-weight: 600; color: #64ffda;">Currently exploring new opportunities to leverage AI for business transformation and process optimization.</p>
        </div>
        """, unsafe_allow_html=True)

        

    with col2:
        # Animated stats
        st.markdown("""
        <div class="card" style="text-align: center;">
            <div style="font-size: 2.5rem; font-weight: 800; color: #64ffda;">3+</div>
            <div>AI-powered solutions deployed</div>
        </div>
        <div class="card" style="text-align: center;">
            <div style="font-size: 2.5rem; font-weight: 800; color: #64ffda;">21%</div>
            <div>Improvement in ticket resolution for Fintech Portfoio</div>
        </div>
        <div class="card" style="text-align: center;">
            <div style="font-size: 2.5rem; font-weight: 800; color: #64ffda;">12%</div>
            <div>Boost in client operations for UK based Consumer Finance startup</div>
        </div>
        """, unsafe_allow_html=True)
# Experience section
def experience():
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <div class="card">
            <div class="card-title">Associate Data Scientist</div>
            <div class="card-subtitle">Blenheim Chalcot (UK's Leading Digital Venture Builder) | 06/2024 - 01/2025</div>
            <div class="bullet-point">Boosted onboarding efficiency by 13% and improved ticket resolution by 21% by deploying AI-driven tools for customer onboarding and support, directly benefiting fintech and edtech ventures.</div>
            <div class="bullet-point">Successfully implemented and deployed 3+ AI-powered automation solutions for document validation and customer workflow optimization, driving a measured improvement of 12% in client operations and user engagement.</div>
            <div class="bullet-point">Collaborated with Technical Architect and CXOs to develop and deploy 4 multi-Agent & RAG based solutions at enterprise scale, streamlining core business processes in screening, verification, and content generation.</div>
            <div class="bullet-point">Demonstrated proficiency in implementing production-ready solutions using open-source LLMs, Anthropic, Gemini, and OpenAI APIs for various business applications.</div>
        </div>

        <div class="card">
            <div class="card-title">System Design Intern</div>
            <div class="card-subtitle">Continental Device India (Semiconductor Components Manufacturer) | 07/2023 - 12/2023</div>
            <div class="bullet-point">Implemented data analytics solution that reduced component failure rate from 15% to <11% through collaboration with engineering and QA teams and deployment of real-time monitoring dashboard.</div>
            <div class="bullet-point">Developed and deployed data-driven test automation systems, adhering to AECQ standards, resulting in 17% improvement in testing efficiency.</div>
        </div>
        """, unsafe_allow_html=True)

# Projects section
def projects():
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">Campaign Crafter</div>
            <div class="bullet-point">Architected and deployed an end-to-end automated system using multi-agent AI for social media campaign generation.</div>
            <div class="bullet-point">Implemented production-ready integration of company goals, values, and audience targeting for automated content creation.</div>
            <div class="bullet-point">Built and deployed scalable solution using Python, AutoGen framework, and OpenAI's GPT-4/DALL-E 3.</div>
            <div class="bullet-point">Implemented prompt engineering techniques for enhanced AI responses.</div>
            <a href="https://campaigncrafter-g0fre4bzc4cbb7b8.uksouth-01.azurewebsites.net/" target="_blank" class="project-link">View Live Project</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Chat Analyzer</div>
            <div class="bullet-point">Deployed automated evaluation system for production chatbot monitoring using UpTrain LLMops framework and OpenAI.</div>
            <div class="bullet-point">Implemented comprehensive analytics including sentiment scoring, resolution tracking, and compliance monitoring.</div>
            <div class="bullet-point">Deployed secure system features including urgency detection and robust security protocols.</div>
            <div class="bullet-point">Designed and optimized PostgreSQL database schema for efficient chat data storage and statistical analysis on performance metrics.</div>
        </div>
        """, unsafe_allow_html=True)

# Education section
def education():
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">B.E. (Hons.) Electrical and Electronics Engineering</div>
        <div class="card-subtitle">BITS Pilani | 08/2020 - 05/2024</div>
        <div class="bullet-point">Completed comprehensive curriculum in Electrical and Electronics Engineering (EEE), with specialized focus on Data Science, Humanities, and Computer Science.</div>
        <div class="bullet-point">Led technical initiatives as active member of TEDx Club, managing event execution and speaker coordination.</div>
        <div class="bullet-point">Contributed to professional development programs through Placement & Training Unit, facilitating technical training workshops.</div>
    </div>
    """, unsafe_allow_html=True)



# Timeline visualization
def timeline():
    st.markdown('<div class="section-title">My Journey</div>', unsafe_allow_html=True)

    # Fixed timeline with proper HTML structure
    st.markdown("""
    <div class="timeline-container">
    <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <h3 class="timeline-date">2025</h3>
                <h4 class="timeline-title">Associate Data Scientist at Blenheim Chalcot</h4>
                <p>Implemented AI-powered automation solutions and collaborated on multi-Agent & RAG based solutions.</p>
            </div>
        </div>

    <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <h3 class="timeline-date">2023 - 2024</h3>
                <h4 class="timeline-title">System Design Intern at Continental Device India</h4>
                <p>Implemented data analytics solution that reduced component failure rate and developed data-driven test automation systems.</p>
            </div>
        </div>

    <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <h3 class="timeline-date">2020 - 2024</h3>
                <h4 class="timeline-title">B.E. (Hons.) at BITS Pilani</h4>
                <p>Studied Electrical and Electronics Engineering with focus on Data Science and Computer Science.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Contact section


def create_gmail_link(to, subject, body):
    """Create a Gmail link with pre-filled subject and body."""
    base_url = "https://mail.google.com/mail/?view=cm&fs=1&tf=1"
    subject_param = urllib.parse.quote(subject)
    body_param = urllib.parse.quote(body)
    gmail_url = f"{base_url}&su={subject_param}&body={body_param}&to={to}"
    return gmail_url

def contact():
    st.markdown('<div class="section-title">Get In Touch</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">Contact Information</div>
            <p><span class="highlight">📧 Email:</span> <a href="mailto:anuanand1402@gmail.com" class="contact-link">anuanand1402@gmail.com</a></p>
            <p><span class="highlight">📱 Phone:</span> +918529706039</p>
            <p><span class="highlight">💼 LinkedIn:</span> <a href="https://linkedin.com/in/anuraganand1402" target="_blank" class="contact-link">linkedin.com/in/anuraganand1402</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        with st.form("contact_form"):
            st.markdown('<p style="color: #64ffda; font-weight: 600;">Send a Message</p>', unsafe_allow_html=True)
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submitted = st.form_submit_button("Send Message")
            if submitted:
                # Create Gmail link
                recipient_email = "anuanand1402@gmail.com"
                subject = f"Message from {name}"
                email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                gmail_url = create_gmail_link(recipient_email, subject, email_body)

                # JavaScript to open the Gmail compose window
                open_mail_js = f"""
                <script type="text/javascript">
                    window.open("{gmail_url}", "_blank");
                </script>
                """
                components.html(open_mail_js)
                st.success("Thanks for reaching out! Your Gmail should open shortly with the pre-filled message.")



                st.markdown('<a href="resume.pdf" download class="resume-button">Download Resume</a>', unsafe_allow_html=True)
        st.markdown('<a href="resume.pdf" download class="resume-button">Download Resume</a>', unsafe_allow_html=True)

# Main function to run the app
def main():
    local_css()
    nav = sidebar()

    if nav == "About":
        header()
    elif nav == "Experience":
        experience()
    elif nav == "Projects":
        projects()
    elif nav == "Education":
        education()
    elif nav == "Journey":
        timeline()
    elif nav == "Contact":
        contact()

if __name__ == "__main__":
    main()
