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
    st.write("🌐 [Your Website](https://yourwebsite.com)")
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
    st.image("selfimage.jpg", use_column_width=True)
    st.write("A system that recommends movies based on user preferences.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush)")

with col2:
    st.subheader("Ai Chatbot")
    st.image("selfimage.jpg", use_column_width=True)
    st.write("An interactive Q&A chatbot built using Streamlit and integrated with open-source large language models (LLMs). Designed to provide intelligent, witty, and human-like responses while maintaining conversational context through message history.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush)")

with col3:
    st.subheader("Portfolio Website")
    st.image("selfimage.jpg", use_column_width=True)
    st.write("A personal portfolio website showcasing my projects and skills.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush)")

col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("IoT-Based Car Parking System")
    st.image("selfimage.jpg", use_column_width=True)
    st.write("A smart car parking system using IoT and sensors.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush)")

with col5:
    st.subheader("Android App - Birthday Wish")
    st.image("selfimage.jpg", use_column_width=True)
    st.write("An Android app that sends automated birthday wishes.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush)")

with col6:
    st.subheader("RC Ornithopter")
    st.image("selfimage.jpg", use_column_width=True)
    st.write("A remote-controlled ornithopter designed for flight testing.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush)")

# Skills
st.header("Skills")
skills = ["Python", "Machine Learning", "Web Development", "IoT", "Android Development"]
st.write(", ".join(skills))

# Contact
st.header("Contact Me")
st.write("Feel free to reach out via email or LinkedIn!")
