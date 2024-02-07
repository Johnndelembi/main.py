import streamlit as st
import time

st.title("""OPERESHEN OKOA ELIMU - FUNDRAISER """)

col1, col2 = st.columns([3,3])

camera_photo = col1.camera_input("Take a photo")

progress_bar = col1.progress(0)

for perc_completed in range(100):
    time.sleep(0.025)
    progress_bar.progress(perc_completed+1)

with col2:     
    st.image("meme.jpeg")
    

col1.success("Photo was uploaded succesfull")

st.markdown("hello, welcome to this fundraiser, this guy is looking for extra money for his tuition fee so he can sit for his final exams ")

with st.expander("click to read more"):
     st.markdown("Use the control number below to make your contribution, thank you")
     st.image("124.PNG")

st.file_uploader("Upload receipt")

with st.spinner(text="Uploading"):
    time.sleep(5)
    st.success("Asante kwa mchango wako")     




