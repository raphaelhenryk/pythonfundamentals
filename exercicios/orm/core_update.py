from sqlalchemy import update
from core import user_table, engine

con = engine.connect()


def atualizar_nome(nome_antigo, nome_novo):
    atualizar = update(user_table).where(user_table.c.nome == nome_antigo)
    atualizar = atualizar.values(nome=nome_novo)
    con.execute(atualizar)
    print(result.rowcount)

atualizar_nome('Raphael','Pedro')