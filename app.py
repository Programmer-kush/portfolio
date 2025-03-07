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
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Movie Recommendation System")
    st.image("Movie Recommendation.png", use_container_width=True)
    st.write("A movie recommendation system that suggests movies based on user preferences. The system uses collaborative filtering to recommend movies similar to the user's preferences.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush/Movie-recomdation-system)")

with col2:
    st.subheader("Ai Chatbot")
    st.image("ChatBot.png", use_container_width=True)
    st.write("An interactive Q&A chatbot built using Streamlit and integrated with open-source large language models (LLMs). Designed to provide intelligent, witty, and human-like responses while maintaining conversational context through message history.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush/ChatBot)")

with col3:
    st.subheader("AI Resume Screening")
    st.image("Resume Screening.png", use_container_width=True)
    st.write("The AI-Powered Resume Screening Tool is designed to assist recruiters by automatically evaluating resumes based on a provided job description and keywords. This tool leverages the Groq API for NLP to analyze resumes and determine candidate suitability.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush/AI-Resume_Screening)")

col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("IoT-Based Car Parking System")
    st.image("IOT Project.jpg", use_container_width=True)
    st.write("A smart car parking system using IoT and sensors and Machine Leaning Model")
    st.write("[🔗 View Project](https://github.com/Programmer-kush/Automated-Car-parking-system)")

with col5:
    st.subheader("Android App - UnitConverter")
    st.image("UnitConverterApp.png", use_container_width=True)
    st.write("A simple unit converter app for Android made bu using Jetpack compose.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush/UnitConverterApp)")

with col6:
    st.subheader("Fake News Detection using ML")
    st.image("Fake news detect.png", use_container_width=True)
    st.write("A machine learning model that detects fake news.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush/ML-powered-Fake-news-detector)")

# Skills
st.header("Skills")
skills = ["Python","Data structure & Algorithm","Machine Learning", "Web Development", "IoT", "Android Development"]
st.write(", ".join(skills))

# Contact
st.header("Contact Me")
st.markdown("[Email Me](mailto:kushbohare@gmail.com)")

st.write("Feel free to reach out via email or LinkedIn!")
