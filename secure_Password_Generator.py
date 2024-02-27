import streamlit as st
import random
from werkzeug.security import generate_password_hash


minusculas = "abcdefghijklmnñopqrstuvwxyz"
mayusculas = minusculas.upper()
numeros = "0123456789"
simbolos = "@()[]{}*,;/-_¿?.¡!$<#>&+%="

# Definir la función para generar contraseñas
def generar_contrasena(longitud):
    secuencia_Base = minusculas + mayusculas + numeros + simbolos
    generador = random.sample(secuencia_Base, longitud)
    password = "".join(generador)
    password_Encriptada = generate_password_hash(password)
    return password, password_Encriptada

# Configurar la interfaz de Streamlit
st.title("Generador de Contraseñas")
st.image("img/BG.jpg", width=600)
longitud = st.slider("Selecciona la longitud deseada para la contraseña:", 6, 20, 10)

if st.button("Generar Contraseña"):
    password, password_Encriptada = generar_contrasena(longitud)
    st.write(f"Contraseña generada: {password}")
    st.write(f"Contraseña encriptada: {password_Encriptada}")