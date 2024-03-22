import streamlit as st
import Functions

st.set_page_config(page_title="Porfolio Marcelo Yuba", page_icon="scr/fondo.jpg", layout="wide")

page_bg_img ="""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hola, soy Marcelo Yuba :wave:")
    st.title("Un Data Analyst  y Data Scientist de Buenos Aires, Argentina")
    st.write(
        "Soy un apasionado en el analisis de datos usando, Power BI y Python, tratando de forma mas eficiente,  obtener resultados para tu negocio."
    )
    st.write("[Mi Github >](https://github.com/marceloyuba)")
    st.write("[Mi LinkedIn >](https://www.linkedin.com/in/marcelo-yuba-b9a39827b/)")

def main():
    st.markdown(
    """
    <style>
    
    </style>
    """,
    unsafe_allow_html=True
)
    st.title('Dashboard de Power BI en Streamlit')
    
    # Inserta el iframe con la URL de tu dashboard de Power BI
    st.markdown('<iframe width="1000" height="800" align = "center" src="https://app.powerbi.com/view?r=eyJrIjoiM2NjNDA0YmItMmRhZC00ZDhlLWFmOWYtZTZiMWMxYWY3ODAzIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
        
if __name__ == '__main__':
    main()
