from model.Bots.Bot import Bot


class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        ehBot = True
        for i in lista_bots:
            try:
                if isinstance(i, Bot) == False:
                    raise TypeError
            except TypeError:
                ehBot = False

        self.__empresa = nomeEmpresa
        if ehBot:
            self.__lista_bots = lista_bots
            self.__bot = None
            self.__message = ''
        else:
            self.__message = 'Erro! Nem todos os elementos são bots!'

    def boas_vindas(self):
        self.__message = f'Sejam bem vindos à imersão de bots da {self.__empresa}!'

    def mostra_menu(self):
        self.__message = 'Os chat bots disponíveis no momento são:'
        for i in range(len(self.__lista_bots)):
            self.__message = f'{i+1} - Bot: {self.__lista_bots[i].nome} - Mensagem de apresentação: {self.__lista_bots[i].apresentacao()}'

    def escolhe_bot(self):

        entrada = int(
            input('Digite o número do chat bot desejado:(-1 para encerrar o programa)  '))
        if entrada == -1:
            self.__message = 'Programa encerrado!'
            return True
        else:
            while entrada < 0 or entrada > len(self.__lista_bots):
                self.__message = 'Valor inválido!'
                entrada = int(input('Digite o número do chat bot desejado: '))

            self.__bot = self.__lista_bots[entrada-1]
            return False

    def mostra_comandos_bot(self):
        return self.__bot.mostra_comandos()

    def le_envia_comando(self):
        try:
            entrada = int(
                input('Digite o comando desejado:(-1 para encerrar o programa) '))

            if entrada == -1:
                return True

            resposta_obj = self.__bot.executa_comando(entrada)
            self.__message = f'{self.__bot.nome} diz: {resposta_obj.getRandomResposta()}'
        except ValueError:
            self.__message = "Informe um número válido"
        except KeyError:
            self.__message = "Indíce não existe"

        return False

    def inicio(self):
        # mostra mensagem de boas-vindas do sistema
        self.boas_vindas()
        # mostra o menu ao usuário
        self.mostra_menu()
        # escolha do bot
        check = self.escolhe_bot()
        if check:
            return "Tchau!"
        # mostra mensagens de boas-vindas do bot escolhido
        print(self.__bot.boas_vindas())
        # entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        # ao sair mostrar a mensagem de despedida do bot
        while True:
            self.mostra_comandos_bot()
            end = self.le_envia_comando()
            if end:
                print(self.__bot.despedida())
                break

    @ property
    def message(self):
        return self.__message

    @ message.setter
    def message(self, value):
        self.__message = value
