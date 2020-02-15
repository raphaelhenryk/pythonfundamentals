class Servidor():

    # Toda variǘel qe estiver no método def _init_ deve sr passado na chamada do metodo (self)
    def __init__(self, servico, disco, processador, memoria):
        self.servico = servico
        self.disco = disco
        self.processador = processador
        self.memoria = memoria

    def addMemoria(self, incremento_memoria):
        val_memoria = self.memoria
        self.memoria = val_memoria + incremento_memoria

    def addArmazenamento(self, incremento_armazenamento):
        val_disco = self.disco
        self.disco = val_disco + incremento_armazenamento

    def alteraServico(self, novo_servico):
        self.servico = novo_servico

servidorWeb = Servidor('Nginx', 250, 'I7 9 geracao', 16)

print(servidorWeb.servico) 
print(servidorWeb.disco)
print(servidorWeb.processador)
print(servidorWeb.memoria)

servidorWeb.addMemoria(16)
servidorWeb.addArmazenamento(250)
servidorWeb.alteraServico('Firefox')


print(servidorWeb.servico)
print(servidorWeb.disco)
print(servidorWeb.processador)
print(servidorWeb.memoria)