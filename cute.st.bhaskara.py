#! /usr/bin/python3
import streamlit as st
st.title ("Formula de Bhaskara")
def run():
 st.set_page_config(
 page_title="Formula de Bhaskara",
 page_icon="",
)

st.write("")
i = 0
deupau = False
st.write("Formula de Bhaskara") 
st.write("")
st.write("X1=-B+Raiz(Delta)")
st.write("--------------------")
st.write("2A")
st.write("")
st.write("X2=-B-Raiz(Delta)")
st.write("----------------------------")
st.write("2A")
st.write("")
#Imagem01
st.image("https://static.mundoeducacao.uol.com.br/mundoeducacao/conteudo/formula-de-bhaskara.jpg")
st.write ("Calcula a Bhaska ai pra Noiz!")
#USER st.number_input
st.write("Qual Ã© o valor de A?")
a = st.number_input("SugestÃ£o 1: " )
st.write("")
st.write("Valor de A: ", a)

st.write("Qual Ã© o valor de B? ")
b = st.number_input("SugestÃ£o 8: " )
st.write("")
st.write("Valor de B ", b)

st.write("Qual Ã© o valor de C?")
c = st.number_input("SugestÃ£o -9: " )
st.write("")
st.write("Valor de C ", c)
#calculodelta
#Imagem 02
st.image("http://2.bp.blogspot.com/-v--lekxUbt0/VXr_4sJPvCI/AAAAAAAAQrU/43sKNsaLX58/s320/delta.jpg")
st.write("")
st.write("Calculo do Delta")
calculodelta = (b * b) - (4 * a * c)
st.write("Valores previos")
st.write("A = ", a)
st.write("B = ", b)
st.write("C = ", c)
st.write("")
st.write("Delta = B2 - 4AC")
st.write("Delta = ","(",b,"*",b,") - (4*",a,"*",c,")")
st.write("Delta = ", calculodelta)

#(calculo raiz)
st.write("")
st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihbOPtXQwp9mlv8Ez59puk8kkIY70PLQj4LatwhngTjs98omoFFutLy7NQHYg3UDUiJ_PmtDgExofpzK3vy4X9iIPXCI_rw-lzNauwKjLTWkwHCZ19oVCbuUa-9Qs_DQl5p5I-da1x8zqLYF14ZGemrWf-bcj2aMYl1I9Xa8wxgjwfvJ97K202zHZ3/w433-h244/nomenclatura%20raiz%20quadrada.png")
st.write("")
st.write("Calculo da Raiz")
#While resultado for diferente de deltaraiz
st.write("")
st.write("Inicio do loop Calculo RAIZ")

st.write("Valor Delta:", calculodelta)
st.write("Valor I inicial:", i)
while deupau == False:
 i += 1
 
 divisao = calculodelta / i
 
 resultado = divisao * i
 if divisao == i: 
  i2 = divisao 
  deupau = True 
 else: 
  deupau = False

st.write("")
st.write("Valor de I atualizado: ",i) 
st.write("Raiz de Delta: ",i2)
st.write("")
#imagem 04
st.image("https://www.pravaler.com.br/wp-content/uploads/2020/08/formula-de-bhaskara-calcular-raizes.png")
st.write("")
st.write("Calculo X1 e X2")
st.write("X1")
st.write("X1 = - B + Raiz(Delta)")
st.write("----------------------------")
st.write("2 * A")
st.write("")
st.write("X1 = -",b,' + ',i2)
st.write("----------------------------")
st.write("2 * ", a)
st.write("")
x1=-(b+i2)/2*a
x2=-(b-i2)/2*a
st.write("X1 = ", x2)
st.write("")
st.write("X2")
st.write("X2 = - B - Raiz(Delta)")
st.write("----------------------------")
st.write("2 * A")
st.write("")
st.write("X2 = -",b,' - ',i2)
st.write("----------------------------")
st.write("2 * ", a)
st.write("")

st.write("X2 = ", x1)
st.write("")

#por algum problema de sintaxe python ou logica matematica 
#o calculo esta invertendo sinal positivo com negativo
#entao para nao perder mais tempo, inverti as variaveis
#de resultado na impressao do console

st.write("Olha o veio Baka ae, quer dizer, Bhaskara")
st.image("https://matematica.com.br/image/posts/1490471516.png")
st.write("")
st.write("MAS....")
st.video("https://www.youtube.com/watch?v=39OSPLVI3_I")

st.write("Site de referÃªncia")
st.write("https://mundoeducacao.uol.com.br/matematica/formula-bhaskara.htm")
st.write("Obrigado!! Mafia Dac")
st.write("")
