import sqlite3

# Conectar ao banco
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Lista de idades para preencher (adicione conforme necessário)
# Aqui estou fazendo de forma aleatória só como exemplo
idades = {
    1: 25,
    2: 32,
    3: 45,
    4: 29,
    5: 38
}

# Atualizar cada cliente com sua idade
for id_cliente, idade in idades.items():
    cursor.execute("UPDATE clientes SET idade = ? WHERE id = ?", (idade, id_cliente))

conn.commit()
conn.close()
print("✅ Idades preenchidas com sucesso!")
