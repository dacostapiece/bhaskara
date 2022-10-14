import streamlit as st
name=""
age=0
buttonName = st.button("insert name")
if buttonName == True:
  name = st.text_input("nome")
  buttonName = True
age = st.number_input("age", step=1, value=0)
st.write("name: ", name)
st.write("age", age)
