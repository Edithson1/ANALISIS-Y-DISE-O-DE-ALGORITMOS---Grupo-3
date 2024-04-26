import streamlit as st
import pandas as pd

usuarios = {
    72439569: "hulk@bb",
    42326885: "loki%=#",
}

def main():
    if not st.session_state.get("logged_in", False):
        st.markdown("<h2 style='text-align: center;'>INICIAR SESIÓN</h2>", unsafe_allow_html=True)
        
        username = st.text_input("Nombre de usuario")
        password = st.text_input("Contraseña", type="password")

        if st.button("Iniciar sesión"):
            if verify_user(username, password):
                st.session_state.logged_in = True
            else:
                st.error("Nombre de usuario o contraseña incorrectos.")
    else:
        show_authenticated_content()

def verify_user(username, password):
    try:
        username = int(username)
    except ValueError:
        return False
    
    if username in usuarios:
        if usuarios[username] == password:
            st.session_state.username = username
            return True
    return False

def show_authenticated_content():
    st.title(f"Bienvenido, {st.session_state.username}!")
    
    def download(archivo):
        df = pd.read_excel(archivo)
        return df
    
    archivo = st.file_uploader("Cargar malla curricular", type=["xlsx", "xls"])

    if archivo is not None:
        df = download(archivo)
        st.write(df.head(100))

if __name__ == "__main__":
    main()
