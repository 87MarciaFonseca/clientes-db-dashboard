import sqlite3  # <- ESSA LINHA FALTAVA!
import pandas as pd

# Conexão com o banco de dados
conn = sqlite3.connect("clientes.db")

# a) Listar os 10 primeiros clientes
df_10 = pd.read_sql_query("SELECT * FROM clientes LIMIT 10", conn)
print(df_10)

# b) Filtrar por nome contendo "Carlos"
df_carlos = pd.read_sql_query("SELECT * FROM clientes WHERE nome LIKE '%Carlos%'", conn)
print("\nClientes com nome contendo 'Carlos':")
print(df_carlos)

# c) Contar número total de clientes
df_total = pd.read_sql_query("SELECT COUNT(*) AS total FROM clientes", conn)
print("\nTotal de clientes:")
print(df_total)

# d) Agrupar por cidade
df_cidade = pd.read_sql_query("""
    SELECT cidade, COUNT(*) AS total_clientes
    FROM clientes
    GROUP BY cidade
""", conn)
print("\nClientes por cidade:")
print(df_cidade)

conn.close()
