from Bots.Bot import Bot
from model.Comando import Comando


class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        super().__comandos = {
            1: Comando(1, "Olá, tudo bem? ", [f"E o que tem de bom?!"]),
            2: Comando(2, "Como você está ?", ["Não interessa!"]),
            3: Comando(3, "Quero um conselho", ["Não tenho filho deste tamanho!"]),
            4: Comando(4, "Adeus", [""])
        }

    def mostra_comandos(self):
        return self.__comandos

    def apresentacao(self):
        return f'GRRRRRR Meu nome é {self.nome} e não me incomode!'

    def executa_comando(self, cmd):
        try:
            return self.__comandos[cmd]
        except:
            print("NÃO SEI!")

    def boas_vindas(self):
        return 'Não acredito que você me escolheu!'

    def despedida(self):
        return 'Finalmente, até nunca mais! '
