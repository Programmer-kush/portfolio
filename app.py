import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon="🎭", layout="wide")

# Sidebar
with st.sidebar:
    st.image("selfimage.jpg", width=200)
    st.title("Kush Bohare")
    st.write("College Student ")
    st.write("📍 Kurukshetra, Haryana")
    st.write("📧 Kushbohare@gmail.com")
    st.write("🌐 [website](https://kushportfolio.streamlit.app/)")
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

# Creating rows for project display
def create_project(title, image_path, description, link):
    """Helper function to create a project layout inside a container."""
    with st.container():
        st.subheader(title)
        st.image(image_path, use_container_width=True)
        st.write(description)
        st.write(f"[🔗 View Project]({link})")

# First row
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        create_project(
            "Movie Recommendation System",
            "Movie Recommendation.png",
            "A movie recommendation system that suggests movies based on user preferences using collaborative filtering.",
            "https://github.com/Programmer-kush/Movie-recomdation-system"
        )
    with col2:
        create_project(
            "AI Chatbot",
            "ChatBot.png",
            "An interactive Q&A chatbot built using Streamlit and integrated with open-source large language models (LLMs).",
            "https://github.com/Programmer-kush/ChatBot"
        )
    with col3:
        create_project(
            "AI Resume Screening",
            "Resume Screening.png",
            "An AI-powered resume screening tool that evaluates resumes based on job descriptions and keywords.",
            "https://github.com/Programmer-kush/AI-Resume_Screening"
        )

# Second row
with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        create_project(
            "IoT-Based Car Parking System",
            "IOT Project.jpg",
            "A smart car parking system using IoT, sensors, and a Machine Learning model.",
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
    skills = ["Python", "Data Structure & Algorithm", "Machine Learning", "Web Development", "IoT", "Android Development"]
    st.markdown("\n".join(f"- {skill}" for skill in skills))

# Contact
st.header("Contact Me")
with st.container():
    st.markdown("[Email Me](mailto:kushbohare@gmail.com)")
    st.write("Feel free to reach out via email or LinkedIn!")
