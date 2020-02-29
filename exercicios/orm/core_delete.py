from sqlalchemy import delete
from core import user_table, engine

con = engine.connect()


def delete_dado(dado):
    d = delete(user_table).where(user_table.c.nome == dado)
    result = con.execute(d)
    print(result.rowcount)


delete_dado('Pedro')
