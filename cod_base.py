import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Verificar se conectou
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tabelas no banco:", cursor.fetchall())

conn.close()
