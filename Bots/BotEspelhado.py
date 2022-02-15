from Bots.Bot import Bot
from Comando import Comando

class BotEspelhado(Bot):
    def __init__(self, nome):
        self.__nome = nome
        super().__comandos = {
            1: Comando(1, "Conte uma curiosidade", ["...moc.scilobmys es-avamahC .5891 ed oçram ed 51 me odartsiger iof tenretnI ed oinímod oriemirp O"]),
            2: Comando(2, "Conte uma piada", ["...méugnin me anrep a assap oãn ale euqrop ,arboc A ?odnum od otsenoh siam lamina o lauQ"]),
            3: Comando(3, "Como ser um Bot Espelhado", ["...lamron uos ue ,êcov é odahlepse é meuq mim arP"])
        }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        msg = "...oditrevni é olaf euq odut ,odahlepsE toB o " + self.__nome + " uos ue ,álO"
        return msg

    def executa_comando(self, cmd):
        try:
            return self.__comandos[cmd]
        except:
            print("...rezaf ogisnoc oãn ue ossI")

    def boas_vindas(self):
        return "Bot Espelhado: '...rednetne em agisnoc euq orepse ,uehlocse em êcoV'"

    def despedida(self):
        return "Bot Espelhado: '...amixórp a éta ,êcov moc rasrevnoc rezarp mu ioF'"
