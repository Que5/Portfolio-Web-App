import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Phumlani Dlamini | Python Developer")
    content = """Enthusiastic Python developer with a strong focus on blockchain (Web3) development. I bring versatility to the table, skilled in both web development and machine learning.  2x Web3 Hackathon winner, eager to leverage my skills to build secure and innovative smart contracts.

A year of experience as a web developer, proficient in utilizing technologies like AWS and Jira. Let's connect and discuss your Python development needs!
"""
    st.info(content)
content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")


with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

