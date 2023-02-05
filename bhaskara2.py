#! /usr/bin/python3
import streamlit as st
st.title ("Formula de Bhaskara")
#upper header
def run():
  st.set_page_config(
  page_title="Formula de Bhaskara",
  page_icon="",
)

st.write("")
#Imagem01
st.image("formula-de-bhaskara.jpg")

st.write ("DISCLAIMER")
st.write ("O código vem com os valores predefinidos:")
st.write("A = 1, B = 8, C = -9")
st.write("Do contrário o programa só iria crashar")
st.write("OUTRAS Sugestões de valores para calcular a Bhaskara com resultados conhecidos:")
st.write("A = 1, B = 12, C = -13")
st.write("Resultado esperado: X1 = 1, X2 = -13")
st.write("A = 3, B = -15, C = 12")
st.write("Resultado esperado: X1 = 4, X2 = 1")
st.write("Esse código não trata se Delta for negativo ou se Raiz for igual à Zero")
st.write("")
st.write ("Calcula a Bhaska ai pra Noiz!")
#USER st.number_input
st.write("Qual eh o valor de A?")
a = st.number_input("Sugestao 1: ", min_value=None, max_value=None, value=1, step=1, key="a")
st.write("")
st.write("Valor de A: ", a)

st.write("Qual eh o valor de B? ")
b = st.number_input("Sugestao 8: ", min_value=None, max_value=None, value=8, step=1, key="b")
st.write("")
st.write("Valor de B ", b)

st.write("Qual eh o valor de C?")
c = st.number_input("Sugestao -9: ", min_value=None, max_value=None, value=-9, step=1, key="c")
st.write("")
st.write("Valor de C ", c)
#calculodelta

#FUNCAO calculoDelta
def calculoDelta(a,b,c):
  resultadoDelta = (b * b) - (4 * a * c)
  return resultadoDelta

#st.write("PONTO CONTROLE - Print calculoDelta", calculoDelta(a,b,c))

resultadoDelta = calculoDelta(a,b,c)

#st.write("Delta01 = ", resultadoDelta)

#Imagem 02
st.image("delta.jpg")
st.write("")
st.write("Calculo do Delta")

st.write("Valores previos")
st.write("A = ", a)
st.write("B = ", b)
st.write("C = ", c)
st.write("")
st.latex(r'''\Delta=b^2-4ac''')
st.write("Delta = ","(",b,"*",b,") - (4*",a,"*",c,")")
st.write("Delta = ", resultadoDelta)

#(calculo raiz)
st.write("Exemplo de Cálculo da Raiz Quadrada")
st.image("raiz-quadrada.png")
st.write("")
st.write("Calculando Raiz")

st.write("")

#FUNCAO calculoRaiz
def calculoRaiz(resultadoDelta):
  deupau = False
  str_depau = "False"
  i = 0
  percent_complete=0
  while deupau == False:
    i += 1
    st.write("<span style='color:red'>CALCULO RAIZ INTERAÇÃO:</span>",i,unsafe_allow_html=True)
    st.progress(percent_complete+i)
   
    divisao = resultadoDelta / i
    
    resultadoRaiz = divisao
    
    if divisao == i: 
      deupau = True
      str_depau = "True"
      
    else:
      bogus = 0

  return resultadoRaiz
st.write("")
#calculoRaiz(resultadoDelta)
resultadoRaiz = calculoRaiz(resultadoDelta)

st.write("")
st.write("Raiz de Delta"); st.latex(r'''\sqrt{\Delta}''')
st.write("Raiz de Delta:",resultadoDelta,": ",resultadoRaiz)
st.write("")
#imagem 04
st.write("Exemplo de Cálculo X1 e X2")
st.image("x1_x2.png")
st.write("")
st.write("Calculo X1 e X2")
st.latex(r'''\Chi=\frac {-b^2±\sqrt{\Delta}} {2.a}''')

#FUNCAO calculoX1_X2
def calculoX1_X2(b,calculoRaiz,a):
    #X1
    st.write("Calculo X1")
    st.latex(r'''\Chi'=\frac {-b^2+\sqrt{\Delta}} {2.a}''')
    divisao = 2*a
       
    st.write("")
    
    st.write("x=-(+",b,")+-RAIZ(",resultadoRaiz*resultadoRaiz,")/2a")
    st.write("x1 = ",-b,"+",resultadoRaiz,"/",divisao)
    passo02=-b+resultadoRaiz
    passo03=passo02/divisao
    X1 = passo03
    st.write("X1 = ",passo02,"/",divisao)
    st.write("X1 = ",passo03)
    
    #X2
    st.write("")
    st.write("Calculo X2")
    st.latex(r'''\Chi''=\frac {-b^2-\sqrt{\Delta}} {2.a}''')

    st.write("x=-(+",b,")+-RAIZ(",resultadoRaiz*resultadoRaiz,")/2a")
    st.write("X2= ",-b,"-",resultadoRaiz,"/",divisao)
    passo02_x2=-b-resultadoRaiz
    passo03_x2=passo02_x2/divisao
    st.write("X2 = ",passo02_x2,"/",divisao)
    st.write("X2 = ",passo03_x2)
    X2 = passo03_x2
    arrayX1_X2 = [X1,X2]

    return arrayX1_X2
resultadoX1 = calculoX1_X2(b,resultadoRaiz,a)

X1 = resultadoX1[0]
X2 = resultadoX1[1]

st.write("")

st.write("Olha o veio Baka ae, quer dizer, Bhaskara")
st.image("bhaskara.png")
st.write("")
st.write("MAS....")
st.video("https://www.youtube.com/watch?v=39OSPLVI3_I")

st.write("Site de referencia")
st.write("https://mundoeducacao.uol.com.br/matematica/formula-bhaskara.htm")
st.write("Full code snippet")
st.write("https://github.com/dacostapiece/bhaskara")
st.write("Obrigado!! Mafia Dac")
st.write("")

#Inserir disclaimer de quando de fato rodou o código
#st.video("https://www.youtube.com/watch?v=39OSPLVI3_I")
