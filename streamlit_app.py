import streamlit as st
import Functions
import base64

st.set_page_config(page_title="Porfolio Marcelo Yuba", page_icon="scr/fondo.jpg", layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("scr/fondo.jpg")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("data:image/jpg;base64,{img}");
    backgrund-size: cover
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

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
