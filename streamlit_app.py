import streamlit as st
import Functions

st.set_page_config(page_title="Prueba", page_icon="scr/fondo.jpg", layout="wide")
def css():
    # Aplicar estilo CSS para el fondo
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("scr/fondo.jpg") no-repeat center center fixed;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True)
if __name__ == '__css__':
    css()
# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hola, soy Marcelo Yuba :wave:")
    st.title("Un Data Analyst de Buenos Aires, Argentina")
    st.write(
        "Soy apasionado en el analisis de datos usando, Power BI y Python, tratando de forma mas eficiente,  obtener resultados para negocios."
    )
    st.write("[Mas sobre mi >](https://github.com/marceloyuba)")
def pagina_inicio():
    st.title("Página de Inicio")
    st.write("Bienvenido a la página de inicio. Esta es la primera página.")

def pagina_opcion1():
    st.title("Página Opción 1")
    st.write("Esta es la página de la Opción 1.")

def pagina_opcion2():
    st.title("Página Opción 2")
    st.write("Esta es la página de la Opción 2.")
def main():
    st.title('Dashboard de Power BI en Streamlit')
    
    # Inserta el iframe con la URL de tu dashboard de Power BI
    st.markdown('<iframe width="1000" height="800" align = "center" src="https://app.powerbi.com/view?r=eyJrIjoiM2NjNDA0YmItMmRhZC00ZDhlLWFmOWYtZTZiMWMxYWY3ODAzIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
    
    st.sidebar.title("Menú de Navegación")
    seleccion_pagina = st.sidebar.radio("Ir a", ("Inicio", "Opción 1", "Opción 2"))

    if seleccion_pagina == "Inicio":
        pagina_inicio()
    elif seleccion_pagina == "Opción 1":
        pagina_opcion1()
    elif seleccion_pagina == "Opción 2":
        pagina_opcion2()
if __name__ == '__main__':
    main()
    
def Developer(desarrollador):
    resultadodeveloper = Functions.Developer(desarrollador)
    return resultadodeveloper

st.markdown(""" 
    <html>
        <body>
            <h2>INSTRUCCIONES</h2>
            <p>            
                1. Ingrese el desarrollador en el cuadro de abajo.<br>
                2. Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.<br>
                3. Sugerencia de usuarios: Valve, Ubisoft, Capcom, Epic Games, Rockstar Games, Sega.<br>
                4. Para cambiar de usuario, copie y pegue de las sugerencias y presione consultar nuevamente.
            </p>      
        </body>
    </html>
    """, unsafe_allow_html=True)

desarrollador = st.text_input("Ingrese el nombre del desarrollador", "Valve")
if st.button("Consultar"):
    developer_result = Developer(desarrollador)
    st.write(developer_result)
    
    
def recomendacion_usuario(Id_Usuario):
    resultadotop_game = Functions.recomendacion_usuario(Id_Usuario)
    return resultadotop_game

st.markdown(""" 
    <html>
        <body>
            <h2>INSTRUCCIONES</h2>
            <p>
                1. Ingrese el usuario en el cuadro de abajo.<br>
                2. Se consulta por usuario y devuelve una lista de recomendaciones para el mismo en base de otros productos similares a los que tiene.<br>
                3. Sugerencia de usuarios: fui312, mailiam123, ScoutCounterAttack, halofan360, tarjla.<br>
                4. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </p>       
        </body>
    </html>
    """, unsafe_allow_html=True)

Id_Usuario = st.text_input("Ingrese el nombre del usuario", "fui312")
if st.button("Consultar Modelo"):
    recomendacion_result = recomendacion_usuario(Id_Usuario)
    st.write(recomendacion_result)
    


