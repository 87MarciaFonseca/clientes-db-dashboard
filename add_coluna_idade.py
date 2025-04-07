import sqlite3

# Conectar ao banco
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Tentar adicionar a coluna "idade"
try:
    cursor.execute("ALTER TABLE clientes ADD COLUMN idade INTEGER")
    print("✅ Coluna 'idade' adicionada com sucesso.")
except sqlite3.OperationalError as e:
    print(f"⚠️ Atenção: {e}")

conn.commit()
conn.close()
