from random import randint


class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, ID, mensagem, respostas=[]):
        self.__id = ID
        self.__mensagem = mensagem
        self.__respostas = respostas

    @property
    def id(self):
        return self.__id

    @property
    def mensagem(self):
        return self.__mensagem

    # retorna uma resposta aleatória
    def getRandomResposta(self):
        return self.__respostas[randint(0, len(self.__respostas))]

    # adiciona resposta
    def addResposta(self, resposta: str):
        self.__respostas.append(resposta)

    # remove resposta (opcional)
    def delResposta(self, resposta):
        pass
