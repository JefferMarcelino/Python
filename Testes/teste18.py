import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

cursor.execute('''
create table agenda(
nome text,
telefone text)
''')

cursor.execute('''
insert into agenda (nome, telefone)
values(?, ?)
''', ("Nilo", "7788-1432"))

conexao.commit()
cursor.close()
conexao.close()
