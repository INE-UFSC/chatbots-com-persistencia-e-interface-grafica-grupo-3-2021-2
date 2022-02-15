# implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r


class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def mostra_comandos(self):
        lista = []
        for key, val in self.__comandos:
            lista.append((key, val))

        return lista

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass

    @abstractmethod
    def despedida():
        pass
