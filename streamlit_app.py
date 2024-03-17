import streamlit as st

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