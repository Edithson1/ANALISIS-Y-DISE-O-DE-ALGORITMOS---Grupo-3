import streamlit as st
import os

def main():
    logged_in = False  # Variable para verificar si el usuario ha iniciado sesión
    menu = ["Login", "Registro"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Login":
        st.markdown("<h1 style='text-align: center;'>Login</h1>", unsafe_allow_html=True)
        logged_in = show_login()
    elif choice == "Registro":
        st.markdown("<h1 style='text-align: center;'>Registrarse</h1>", unsafe_allow_html=True)
        show_registration()

    if logged_in:
        show_user_account()

def show_registration():
    # Campos de entrada para el nombre de usuario y la contraseña
    username = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")

    # Botón para realizar el registro
    if st.button("Registrarse"):
        if username and password:
            register_user(username, password)
            st.success("¡Registro exitoso! Por favor, inicia sesión.")
        else:
            st.error("Por favor, completa todos los campos.")

def register_user(username, password):
    # Obtener la ruta al directorio actual del script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta al archivo de usuarios dentro del directorio del proyecto
    users_file_path = os.path.join(current_dir, "users.txt")

    # Escribir los datos de registro en el archivo de usuarios
    with open(users_file_path, "a") as file:
        file.write(f"{username}:{password}\n")

def show_login():
    # Campos de entrada para el nombre de usuario y la contraseña
    username = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")

    # Botón para iniciar sesión
    if st.button("Iniciar sesión"):
        if verify_user(username, password):
            st.success(f"Bienvenido, {username}!")
            return True  # Marcar como iniciado sesión si la verificación es exitosa
        else:
            st.error("Nombre de usuario o contraseña incorrectos.")

def verify_user(username, password):
    # Obtener la ruta al directorio actual del script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta al archivo de usuarios dentro del directorio del proyecto
    users_file_path = os.path.join(current_dir, "users.txt")

    with open(users_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                return True
    return False

def show_user_account():
    # Mostrar el nombre de usuario y las opciones dentro de la sección de inicio de sesión
    st.write("")
    st.write("")
    st.write("### Opciones de sesión")
    st.write("")
    # Opción para ver los datos del perfil del usuario
    st.write("[Ver perfil](#)")
    # Opción para cerrar sesión
    if st.button("Cerrar sesión", key="logout_btn"):
        st.success("¡Sesión cerrada correctamente!")
        st.experimental_rerun()

if __name__ == "__main__":
    main()
