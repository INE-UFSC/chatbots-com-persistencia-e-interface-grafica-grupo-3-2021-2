from Bots.Bot import Bot
from model.Comando import Comando


class BotMinerin(Bot):
    def __init__(self, nome):
        self.__nome = nome
        super().__comandos = {
            1: Comando(1, "Você queria ter praia?", ["Sô, não é Minas que não tem mar, é o mar que não têm Minas!"]),
            2: Comando(2, "Pão de Queijo ou Queijo Canastra?", ["Pão de Queijo com Queijo Canastra"]),
            3: Comando(3, "O que significa a sigla GO?", ["GOnorante! Mas nós aqui de Minas somo Mai Gonorante ainda!"]),
            4: Comando(4, "Onde você mora?", ["Eu moro logo ali, na rua de cima do açouque do Valtin, debaixo da rua da Vânia mãe do Zé"]),
            5: Comando(5, "Qual o verdadeiro truco?", ["O truco de verdade é o trucão com manilha fixa! Esses paulistas que inventam esse trem de manilha alta"]),
            6: Comando(6, "Você é atleticano ou cruzeirense?", ["GALOOOOOO!"])
        }

    @property
    def nome(self):
        return self.__nome

    @property
    def comandos(self):
        return self.__comandos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f"Aoba, bão ô não?! Prazer, sou o {self.__nome}. E ocê, cê é fí de quem?"

    def mostra_comandos(self):
        return self.__comandos

    def executa_comando(self, cmd):
        try:
            return self.__comandos[cmd]
        except:
            print('Atrapaiô o trem tudo!')

    def boas_vindas(self):
        print(
            f"Prazer, {self.nome}! Eu tenho um primo em Uberlândia com esse mesmo nome.")

    def despedida(self):
        print("Vai não sô, tá cedo!! Fica só mais um cadin, vou passar um cafezin nesse instante.")
