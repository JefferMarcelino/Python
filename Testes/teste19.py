import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchone()

print("Nome: %s\nTelefone: %s" % resultado)
cursor.close()
conexao.close()
