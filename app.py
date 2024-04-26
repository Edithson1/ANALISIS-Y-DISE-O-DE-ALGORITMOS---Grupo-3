import streamlit as st

def main():
    st.title("Registro y Login App")

    menu = ["Login", "Registro"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Login":
        show_login()
    elif choice == "Registro":
        show_registration()

def show_registration():
    st.subheader("Registro")

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
    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")

def show_login():
    st.subheader("Login")

    # Campos de entrada para el nombre de usuario y la contraseña
    username = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")

    # Botón para iniciar sesión
    if st.button("Iniciar sesión"):
        if verify_user(username, password):
            st.success(f"Bienvenido, {username}!")
        else:
            st.error("Nombre de usuario o contraseña incorrectos.")

def verify_user(username, password):
    with open("users.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                return True
    return False

if __name__ == "__main__":
    main()
