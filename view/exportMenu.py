

import PySimpleGUI as sg


class ExportMenu ():
    def __init__(self):
        self.__container = []
        self.__window = sg.Window('CHAT BOT').Layout(self.__container)

    def desenha_menu(self):
        layout = [[sg.Text('Digite o nome do arquivo que deseja salvar:')],
                  [sg.InputText('', key='caminho_export')],
                  [sg.Button('Exportar')]]

        self.__container = layout
        self._window = sg.Window('EXPORT MENU').Layout(self.__container)
