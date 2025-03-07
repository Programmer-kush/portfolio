import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon="🎭", layout="wide")

# Sidebar
with st.sidebar:
    st.image("selfimage.jpg", width=200)
    st.title("Kush Bohare")
    st.write("College Student")
    st.write("📍 Kurukshetra, Haryana")
    st.write("📧 Kushbohare@gmail.com")
    st.write("🌐 [Website](https://kushportfolio.streamlit.app/)")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/kush-bohare-bohare-774775351/) | [GitHub](https://github.com/Programmer-kush)")

# Main Content
st.title("Welcome to My Portfolio")

# About Me
st.header("About Me")
with st.container():
    st.write(
        """
        I am a college student who is passionate about software development and machine learning.
        I am currently pursuing my B.Tech in Information Technology and Engineering from NIT Kurukshetra.
        I have experience working with Python, C++, and Java.
        I am always eager to learn new technologies and build projects that solve real-world problems.
        I am also an active member of the AeroModelling club of our college.
        """
    )

# Projects
st.header("Projects")

# Function to create a project card with a fixed 16:9 image aspect ratio
def create_project(title, image_path, description, link):
    with st.container():
        st.subheader(title)
        
        # Load and resize image to 16:9 aspect ratio
        img = Image.open(image_path)
        img = img.resize((960, 540))  # Standard 16:9 resolution
        st.image(img, use_column_width=True)
        
        st.write(description)
        st.markdown(f"[🔗 View Project]({link})")

# Row 1
col1, col2, col3 = st.columns(3)
with col1:
    create_project(
        "Movie Recommendation System",
        "Movie Recommendation.png",
        "A system that suggests movies based on user preferences using collaborative filtering.",
        "https://github.com/Programmer-kush/Movie-recomdation-system"
    )
with col2:
    create_project(
        "AI Chatbot",
        "ChatBot.png",
        "An interactive chatbot using open-source large language models (LLMs).",
        "https://github.com/Programmer-kush/ChatBot"
    )
with col3:
    create_project(
        "AI Resume Screening",
        "Resume Screening.png",
        "An AI-powered resume screening tool that evaluates resumes based on job descriptions.",
        "https://github.com/Programmer-kush/AI-Resume_Screening"
    )

# Row 2
col4, col5, col6 = st.columns(3)
with col4:
    create_project(
        "IoT-Based Car Parking System",
        "IOT Project.jpg",
        "A smart car parking system using IoT, sensors, and a machine learning model.",
        "https://github.com/Programmer-kush/Automated-Car-parking-system"
    )
with col5:
    create_project(
        "Android App - UnitConverter",
        "UnitConverterApp.png",
        "A simple unit converter app for Android made using Jetpack Compose.",
        "https://github.com/Programmer-kush/UnitConverterApp"
    )
with col6:
    create_project(
        "Fake News Detection using ML",
        "Fake news detect.png",
        "A machine learning model that detects fake news.",
        "https://github.com/Programmer-kush/ML-powered-Fake-news-detector"
    )

# Skills
st.header("Skills")
with st.container():
    skills = ["Python", "Data Structures & Algorithms", "Machine Learning", "Web Development", "IoT", "Android Development"]
    st.markdown("\n".join(f"- {skill}" for skill in skills))

# Contact
st.header("Contact Me")
with st.container():
    st.markdown("[Email Me](mailto:kushbohare@gmail.com)")
    st.write("Feel free to reach out via email or LinkedIn!")
