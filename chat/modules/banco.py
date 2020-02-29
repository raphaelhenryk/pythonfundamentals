from pymongo import MongoClient, DESCENDING
import time


class BancoMongo():

    def __init__(self):
        try:
            cliente = MongoClient('192.168.200.111')
            self.db = cliente['chat']
        except Exception as e:
            print(e)
            exit()

    def cadastrar(self, nome, mensagem):
        date = {'nome': nome,
                'mensagem': mensagem,
                'hora': time.strftime('%d-%m-%Y %H:%M:%S')
                }

        self.db.chat.insert(date)

    def visualisar(self):
        ultimoRegistro = [
            rg for rg in self.db.chat.find().sort("_id", DESCENDING)]
        while True:
            date = [rg for rg in self.db.chat.find().sort("_id", DESCENDING)]
            if date != ultimoRegistro:
                ultimoRegistro = date
                dado = ultimoRegistro[0]
                print("[{}] {} : {} \n".format(dado['hora'], dado['nome'], dado['mensagem']))
            time.sleep(2)
