# ================================= Conexao com Postgres
# import psycopg2

# try:
#     con = psycopg2.connect("host=localhost dbname=projeto \
#                             user=admin  \
#                             password=4linux")

#     cur = con.cursor()

#     cur.execute("insert into scripts(nome, conteudo) values ('testcon.py','teste \
#         de conexao ao banco');")

# except Exception as e:
#     print('Erro: {}'.format(e))
#     print('Fazendo Rollback')
#     con.rollback()

# finally:
#     print('Finalizando a conexao com o banco')
#     cur.close()
#     con.close()

# ================================= Conexao com Mongo DB
from pymongo import MongoClient

client = MongoClient('127.0.0.1')
db = client['dexterops']


def inserir_dados():
    try:
        db.fila.insert({"_id": 2, "empresa": "4linux", "cursos": [{"nome": "python fundamentals",
                                                                   "carga horaria": 40},
                                                                  {"nome": "linux fundamentals",
                                                                   "carga horaria": 40}
                                                                  ]})

    except Exception as e:
        print('Erro: {}'.format(e))

inserir_dados()