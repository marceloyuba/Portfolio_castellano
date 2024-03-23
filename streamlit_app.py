import streamlit as st
from PIL import Image

st.set_page_config(page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

img_contact_form = Image.open("images/yt_contact_form.png")
img_tec = Image.open("scr/taxis.png")

# ---- HEADER SECTION ----
with st.container():        
    st.header("Hola, soy Marcelo Yuba :wave:")
    st.title("Un Data Analyst  y Data Scientist de Buenos Aires, Argentina")
    st.write(
        "Apasionado en el analisis de datos usando, Power BI y Python, tratando de forma mas eficiente,  obtener resultados para tu negocio."
    )
    st.write("[Mi Github >](https://github.com/marceloyuba)")
    st.write("[Mi LinkedIn >](https://www.linkedin.com/in/marcelo-yuba-b9a39827b/)")



# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    text_column, image_column = st.columns((1, 2))
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
    with image_column:
       st.image(img_tec)







page_bg_img = """
<style>

[data-testid="stAppViewContainer"] > .main {
background-image: url("https://github.com/marceloyuba/PorfolioIngles/blob/main/scr/fondoTaxi.png?raw=true");
background-position: top left;
background-repeat: repeat;
background-attachment: fixed;
background-size: cover;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)