import sqlite3
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Clientes DB", layout="wide")
st.title("📊 Visualização de Dados - Banco de Clientes")

# Conectar ao banco SQLite
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Obter os dados da tabela "clientes"
try:
    cursor.execute("SELECT * FROM clientes")
    dados = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(dados, columns=colunas)

    st.success(f"{len(df)} registros carregados com sucesso!")

    # 🎯 Filtros
    with st.expander("🔍 Filtrar dados"):
        nome = st.text_input("Filtrar por Nome")
        idade = st.slider("Filtrar por Idade", 0, 100, (0, 100))

        # Aplicar filtros
        df_filtrado = df[
            df["nome"].str.contains(nome, case=False, na=False) &
            df["idade"].between(idade[0], idade[1])
        ]

    # Mostrar dados filtrados
    st.subheader("📋 Resultado")
    st.dataframe(df_filtrado, use_container_width=True)

    # 📤 Exportar CSV
    st.download_button(
        label="⬇️ Baixar dados como CSV",
        data=df_filtrado.to_csv(index=False).encode('utf-8'),
        file_name='clientes_filtrados.csv',
        mime='text/csv'
    )

except sqlite3.Error as e:
    st.error(f"Erro ao consultar o banco: {e}")

finally:
    conn.close()
