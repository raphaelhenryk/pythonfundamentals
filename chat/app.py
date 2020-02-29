import modules.banco as banco
import threading

if __name__ == "__main__":
    # instancia do objeto BancoMongo

    db = banco.BancoMongo()
    user = input("Nickname: ")
    
    try:
        f = threading.Thread(target=db.visualisar)
        f.start()
    except Exception as e:
        print('Falha ao criar a thread: {}'.format(e))
    while f.is_alive:
        mens = input()
        db.cadastrar(user, mens)
