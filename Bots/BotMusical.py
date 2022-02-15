from Bots.Bot import Bot
from Comando import Comando
class BotMusical(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {
            1: Comando(1, 'Bom dia',[ 'Alguma coisa acontece no meu coração... Ah, oi! Bom dia!']),
            2: Comando(2, 'Quem é você?',[ f'EU SOU O SAMBAAA! Brincadeira, eu sou {self.__nome}!']),
            3: Comando(3, 'Como vai ser o futuro?', ['Eu vejo a vida melhor no futuro, eu vejo isso por cima de um muro\nde hipocrisia que insiste em nos rodear...'])
        }

    @property
    def comandos(self):
        return self.__comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f'Deixa eu me apresentar, que eu acabei de chegar! Meu nome é {self.__nome}!'
 
    
    def executa_comando(self,cmd):
        try:
            return self.__comandos[cmd]
        except:
            print("Desafinei...")

   
    def boas_vindas(self):
        return 'Alguma coisa acontece no meu coração... Ah, oi! Bom dia!'

    def despedida(self):
        return 'Deixe-me ir, preciso andar, vou por aí a procurar... Rir pra não chorar! Tchaau!'
