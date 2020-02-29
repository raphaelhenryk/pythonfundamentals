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
        db.fila.insert({"_id": 1, "empresa": "4linux", "cursos": [{"nome": "python fundamentals",
                                                                   "carga horaria": 40},
                                                                  {"nome": "linux fundamentals",
                                                                   "carga horaria": 40}
                                                                  ]})

    except Exception as e:
        print('Erro: {}'.format(e))


def buscar_dados():
    for r in db.fila.find():
        print('Empresa: {}'.format(r['empresa']))
        for c in r['cursos']:
            print(20*'=')
            print('Nome: {} \n Carga Horaria: {}'.format(
                c['nome'], c['carga horaria']))


def adicionar_sub():
        db.fila.update({"_id": 1}, {"$addToSet":
                                    {"instrutores": {'nome': 'Mariana',
                                                     'email': 'mariana.albano@4linux.com.br'}}})


def update_instrutor():
        db.fila.update({"_id": 1, "instrutores.nome": "Mariana"},
                       {"$set": {"instrutores.$.nome": "Marcela"}})


def update_email():
        db.fila.update({"_id": 1, "instrutores.email": "mariana@hotail.com"},
                       {"$set": {"instrutores.$.email": "xurupita@gmail.com"}})


inserir_dados()
buscar_dados()
adicionar_sub()
update_instrutor()
update_email()
buscar_dados()

