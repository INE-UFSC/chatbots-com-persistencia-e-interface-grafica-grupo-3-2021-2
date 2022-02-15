import PySimpleGUI as sg

class Choose_Menu:
    def _init_(self, lista):
        self.__lista = lista
        self.__container = []
        self._window = sg.Window('CHAT BOT').Layout(self._container)


    def desenha_menu(self):

        sg.theme('Dark Grey 13')
        lista_dropbox = []
        for i in range(len(self.__lista)):
            lista_dropbox.append(self.__lista[i].nome)

        tupla_dropbox = tuple(lista_dropbox)
        dropbox = sg.InputCombo(tupla_dropbox, size=(20, 1) )

        layout = [
            [sg.Text('Escolha um bot para entrar em chat')],
            [dropbox],
            [sg.Submit('CHAT')]
                  ]

        self.__container = layout
        self._window = sg.Window('CHAT BOT').Layout(self._container)


    def le_eventos(self):
        return self.__window.Read()