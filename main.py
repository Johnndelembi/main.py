import streamlit as st
import time

st.set_page_config(page_title="TUMCHANGIE KIJANA", page_icon=":wave:")
st.title("""TUMCHANGIE KIJANA - FUNDRAISER """)

col1, col2 = st.columns([3,3])

camera_photo = col1.camera_input("Take a photo")

progress_bar = col1.progress(0)

for perc_completed in range(100):
    time.sleep(0.025)
    progress_bar.progress(perc_completed+1)

with col2:     
    st.image("meme.jpeg")
    st.caption("Kidogo ulichonacho kinatosha tumchangie kijana aende akafanye mtihani")
    

col1.success("Photo was uploaded succesfull")

st.subheader("A young man's future on hold due to exam fees. Help him reach his potential by contributing towards his tuition. Every bit counts, let's unlock his dreams together! Donate now. ")

with st.expander("click to read more"):
     st.markdown("Use the control number below to make your contribution, thank you")
     st.image("124.PNG")

st.file_uploader("Upload receipt")

with st.spinner(text="Uploading"):
    time.sleep(5)
    st.success("Asante kwa mchango wako")     




