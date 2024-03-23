import streamlit as st

st.set_page_config(page_title="Portfolio Marcelo Yuba", page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

img_tec = "https://github.com/marceloyuba/Portfolio_castellano/blob/main/scr/taxis.png?raw=true"

# ---- HEADER SECTION ----
with st.container():        
    st.header("Hola, soy Marcelo Yuba :wave:")
    st.title("Un Data Analyst  y Data Scientist de Buenos Aires, Argentina")
    st.write(
        "Apasionado en el analisis de datos usando, Power BI y Python, tratando de forma mas eficiente,  obtener resultados para tu negocio o empresa."
    )
    st.write("[Mi Github >](https://github.com/marceloyuba)")
    st.write("[Mi LinkedIn >](https://www.linkedin.com/in/marcelo-yuba-b9a39827b/)")


column_widths = [2, 1] 

with st.container():
    st.write("---")
    st.title("Que es lo que hago")
    st.write("##")
    col1, col2 = st.columns(column_widths)

    # En la primera columna, puedes agregar texto u otros elementos si lo deseas
    with col1:
        st.subheader("Utilizando diferentes tecnologias, me permiten hacer analisis de datos, Dashboards interactivos")
        

    # En la segunda columna, puedes mostrar la imagen
    with col2:
        imagen = "scr/tec.png"  # Reemplaza esto con la ruta de tu imagen
        st.image(imagen)






page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/Portfolio_castellano/blob/main/scr/taxis.png?raw=true");
background-position: top left;
background-repeat: repeat;
background-attachment: fixed;
background-size: cover;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)