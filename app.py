import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt 
from GRAFO_CICLOS import malla_curricular
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

                malla_curricular("CursosInformatica.csv")

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
        st.header('Malla Curricular')
        st.dataframe(df)

        df = df.iloc[:-2, :]

        df = df.rename(columns={"Nombre_original": "Cursos"})


        #Grafo dirigido en NetworkX: Para saber cuál es la línea que generará un curso base
        cursos = df[~df['Nombre'].str.contains("Asignaturas", case=False)]['Cursos'].tolist()
        curso_selec = st.selectbox('- Seleccione el curso a visualizar', cursos)
        st.write('Curso seleccionado:', curso_selec.capitalize())

        codigo = df.loc[df["Cursos"] == curso_selec, "Código"].values[0]
        G = nx.DiGraph()
        G.add_node(codigo)
        flag = False

        while flag == False:
            if not df.loc[df["Codigo_del_Requisito"] == codigo, "Código"].empty:
                descendiente = df.loc[df["Codigo_del_Requisito"] == codigo, "Código"].values[0]
                G.add_node(descendiente)
                G.add_edge(codigo, descendiente)
                codigo = descendiente

            else:
                pos = nx.spring_layout(G)  
                fig, ax = plt.subplots(figsize=(10, 6))  
                nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, ax=ax)  # Dibujar el grafo
                ax.set_title(f"Grafo del curso de {curso_selec}")  
                ax.axis('off')  
                plt.tight_layout()  
                st.pyplot(fig) 
                flag = True

if __name__ == "__main__":
    main()
