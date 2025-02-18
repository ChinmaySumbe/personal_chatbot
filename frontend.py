import streamlit as st
import backend as bk

st.title("Personalize chatbot")
Input = st.text_input("Ask Me")
st.text("Click on Submit")
go_button = st.button("Submit")


if go_button:
    output = bk.get_text_stream_output(Input)
    st.write(output)