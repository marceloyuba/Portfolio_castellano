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
def main():
    st.title('Dashboard de Power BI en Streamlit')
    
    # Inserta el iframe con la URL de tu dashboard de Power BI
    st.markdown('<iframe width="1000" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiM2NjNDA0YmItMmRhZC00ZDhlLWFmOWYtZTZiMWMxYWY3ODAzIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
    
def Developer(desarrollador):
    resultadodeveloper = Functions.Developer(desarrollador)
    return resultadodeveloper

st.markdown(""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: #ffff00;">INSTRUCCIONES</h1>
            <h3 style="color: #ffff00; font-family: 'Trebuchet MS';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.<br>
                4. Sugerencia de usuarios: Valve, Ubisoft, Capcom, Epic Games, Rockstar Games, Sega.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Enter nuevamente.
            </h3>         
        </body>
    </html>
    """, unsafe_allow_html=True)

desarrollador = st.text_input("Ingrese el nombre del desarrollador", "Valve")
if st.button("Consultar"):
    developer_result = Developer(desarrollador)
    st.write(developer_result)