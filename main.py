import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Jacek Majewski")
    content = """
    Hi, I am Jacek! I'm learning programming mainly using free resources, 
    I'm interested in programming and IT in a broad sense, 
    and I would like to develop as a Python Developer.
    """
    st.info(content)