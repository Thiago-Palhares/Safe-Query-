import streamlit as st
from ai import analisar_sql

st.title("Safe Query")

entrada = st.text_area("Digite sua query SQL ou pergunta:")

if st.button("Analisar"):
    resposta = analisar_sql(entrada)
    st.write(resposta)