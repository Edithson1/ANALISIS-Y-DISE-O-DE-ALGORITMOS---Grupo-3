import streamlit as st

# Título de la aplicación
st.title('Login App')

# Entrada de texto para el nombre de usuario
username = st.text_input('Nombre de usuario')

# Entrada de texto para la contraseña
password = st.text_input('Contraseña', type='password')

# Botón de inicio de sesión
if st.button('Iniciar sesión'):
    if username == 'usuario' and password == 'contraseña':
        st.success('¡Inicio de sesión exitoso!')
    else:
        st.error('Nombre de usuario o contraseña incorrectos')
