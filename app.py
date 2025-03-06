import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon="🎭", layout="wide")

# Sidebar
with st.sidebar:
    st.image("selfimage.jpg", width=200)
    st.title("kush Bohare")
    st.write("College Student ")
    st.write("📍Kurukshetra,Haryana")
    st.write("📧 Kushbohare@gmail.com")
    st.write("🌐 [Your Website](https://yourwebsite.com)")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/kush-bohare-bohare-774775351/) | [GitHub](https://github.com/Programmer-kush)")

# Main Content
st.title("Welcome to My Portfolio")

# About Me
st.header("About Me")
st.write(
    """
 I   I am a college student who is passionate about software development and machine learning.
   I am currently pursuing my B.Tech in Information Technology and Engineering from NIT Kurukshetra.
     I have experience working with Python, C++, and Java. 
     I am always eager to learn new technologies and build projects that solve real-world problems.
    I am also a active member of AeroModelling club of our college
    """
)

# Projects
st.header("Projects")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Movie-recomdation-system")
    st.image("selfimage.jpg", use_column_width=True)
    st.write("Short description of the project.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush)")

with col2:
    st.subheader("Project 2")
    st.image("selfimage.jpg", use_column_width=True)
    st.write("Short description of the project.")
    st.write("[🔗 View Project](https://github.com/Programmer-kush)")

# Skills
st.header("Skills")
skills = ["Python", "Machine Learning", "Web Development", "IoT", "Android Development"]
st.write(", ".join(skills))

# Contact
st.header("Contact Me")
st.write("Feel free to reach out via email or LinkedIn!")
