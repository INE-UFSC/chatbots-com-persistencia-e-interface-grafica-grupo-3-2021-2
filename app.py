#encoding: utf-8
from controller import SistemaChatBot as scb
from model.Bots.BotMarombeiro import BotMarombeiro
from model.Bots.BotGamer import BotGamer
from model.Bots.BotEspelhado import BotEspelhado
from model.Bots.BotMusical import BotMusical
from model.Bots.BotJose import BotJose
from model.Bots.BotManezinho import BotManezinho
from model.Bots.BotMinerin import BotMinerin
from model.Bots.BotFeliz import BotFeliz

# construa a lista de bots disponíveis aqui
lista_bots = [BotMarombeiro("Bambam"), BotGamer("Ninja"), BotEspelhado("oãoJ"), BotMinerin("Renato"), BotManezinho(
    "Moquirido"), BotMusical("Thiaguinho"), BotJose("José"), BotFeliz("Happy Bot")]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
