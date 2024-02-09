import streamlit as st
import time

st.set_page_config(page_title="TUMCHANGIE KIJANA", page_icon=":wave:")
st.title("""TUMCHANGIE KIJANA - FUNDRAISER """)

st.subheader("A young man's future on hold due to exam fees. Help him reach his potential by contributing towards his tuition. Every bit counts, let's unlock his dreams together! Donate now. ")
col1, col2 = st.columns([3,3])
with col1.expander("click to read more"):
     st.markdown("Use the control number below to make your contribution, tumia control number kutoka kwenye picha chini kumchangia kijana thank you")
     st.image("124.PNG")
with col2.expander("Picha"):
     st.image("john.jpeg")
    

st.file_uploader("Upload receipt")

with st.spinner(text="Uploading"):
    time.sleep(5)
    st.success("Asante kwa mchango wako")     




