import streamlit as st

st.set_page_config(page_title="Prueba", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hola, soy Marcelo Yuba :wave:")
    st.title("Un Data Analyst de Buenos Aires, Argentina")
    st.write(
        "Soy apasionado en el analisis de datos usando, Power BI y Python, tratando de forma mas eficiente,  obtener resultados para negocios."
    )
    st.write("[Mas sobre mi >](https://github.com/marceloyuba)")
