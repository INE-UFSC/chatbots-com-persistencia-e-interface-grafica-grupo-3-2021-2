from Bots.Bot import Bot
from model.Comando import Comando


class BotLegal(Bot):
    def __init__(self, nome):
        self.__nome = nome
        super().__comandos = {1: Comando(1, "Você é um otário!", ["Você é muito inteligente e eu te desejo as melhores coisas desse mundo"]),
                              2: Comando(2, "Porque você é tão legal?", ["Porque eu aprendi que na vida a única coisa que vale a pena é o amor"]),
                              3: Comando(3, "O que você acha da legalização das drogas?", ["Acho que se é legal é bom!"])}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return "Olá! Eu sou o Bot Legal, podemos ser amigos?"

    def executa_comando(self, cmd):
        try:
            return self.__comandos[cmd]
        except:
            print("Ah isso eu não sei...")

    def boas_vindas(self):
        return "Oii, que bom que voçê me escolheu, acho que já somos amigos então"

    def despedida(self):
        return "Aff, você já está indo? Até uma próxima então"
