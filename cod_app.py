import sqlite3
import streamlit as st
import pandas as pd

# Título da página
st.title("Visualização de Dados - Banco de Clientes")

# Conectar ao banco de dados SQLite
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Obter os dados da tabela "clientes"
try:
    cursor.execute("SELECT * FROM clientes")
    dados = cursor.fetchall()
    colunas = [descricao[0] for descricao in cursor.description]
    
    # Criar DataFrame com os dados
    df = pd.DataFrame(dados, columns=colunas)
    
    # Exibir tabela no Streamlit
    st.subheader("Tabela de Clientes")
    st.dataframe(df)

except sqlite3.Error as e:
    st.error(f"Erro ao consultar o banco: {e}")

# Fechar a conexão
conn.close()
