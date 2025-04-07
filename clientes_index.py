import sqlite3
import time

# Conecta ao banco ou cria um novo
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Criação da tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        cidade TEXT
    );
""")

# Insere muitos dados se a tabela estiver vazia
cursor.execute("SELECT COUNT(*) FROM clientes")
total = cursor.fetchone()[0]
if total == 0:
    print("Inserindo dados...")
    for i in range(100000):
        cursor.execute("INSERT INTO clientes (nome, email, cidade) VALUES (?, ?, ?)", 
                       (f"Cliente {i}", f"cliente{i}@email.com", "Rio de Janeiro"))
    conn.commit()

# TESTE DE CONSULTA SEM ÍNDICE
print("\n🔍 Buscando sem índice...")
inicio = time.time()
cursor.execute("SELECT * FROM clientes WHERE nome = 'Cliente 99999'")
print(cursor.fetchone())
print(f"⏱ Tempo sem índice: {time.time() - inicio:.4f} segundos")

# CRIA O ÍNDICE
cursor.execute("CREATE INDEX IF NOT EXISTS idx_nome ON clientes(nome)")
conn.commit()

# TESTE DE CONSULTA COM ÍNDICE
print("\n🔍 Buscando com índice...")
inicio = time.time()
cursor.execute("SELECT * FROM clientes WHERE nome = 'Cliente 99999'")
print(cursor.fetchone())
print(f"⏱ Tempo com índice: {time.time() - inicio:.4f} segundos")

conn.close()
