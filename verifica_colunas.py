import sqlite3

# Conectar ao banco
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Verificar estrutura da tabela
cursor.execute("PRAGMA table_info(clientes)")
colunas = cursor.fetchall()

for coluna in colunas:
    print(coluna)

conn.close()
