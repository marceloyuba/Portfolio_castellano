import streamlit as st
from IPython.display import IFrame
st.set_page_config(page_title="Prueba", page_icon=":tada:", layout="wide")
dashboard = IFrame(src="https://app.powerbi.com/view?r=eyJrIjoiM2NjNDA0YmItMmRhZC00ZDhlLWFmOWYtZTZiMWMxYWY3ODAzIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9", width=1000, height=600)
# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hola, soy Marcelo Yuba :wave:")
    st.title("Un Data Analyst de Buenos Aires, Argentina")
    st.write(
        "Soy apasionado en el analisis de datos usando, Power BI y Python, tratando de forma mas eficiente,  obtener resultados para negocios."
    )
    st.write("[Mas sobre mi >](https://github.com/marceloyuba)")
with st.container(): dashboard