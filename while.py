#! /usr/bin/python3
import streamlit as st
deupau = False
i = 0
calculodelta = st.number_input(label="etiqueta")
while deupau == False:
  i += 1
  divisao = calculodelta / i
  resultado = divisao * i
  if divisao == i: 
    i2 = divisao 
    deupau = True 
  else: 
    deupau = False
st.write(i2)
st.image("bhaskara.png")
