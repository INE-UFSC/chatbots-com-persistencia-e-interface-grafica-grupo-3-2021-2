#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotMarombeiro import BotMarombeiro
from Bots.BotGamer import BotGamer
from Bots.BotEspelhado import BotEspelhado
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotMusical import BotMusical
from Bots.BotJose import BotJose
from Bots.BotManezinho import BotManezinho
from Bots.BotMinerin import BotMinerin
from Bots.BotFeliz import BotFeliz

###construa a lista de bots disponíveis aqui
lista_bots = [BotMarombeiro("Bambam"), BotGamer("Ninja"), BotEspelhado("oãoJ"), BotMinerin("Renato"), BotManezinho("Moquirido"), BotZangado("Tisca"), BotTriste("Sadboy"), BotMusical("Thiaguinho"), BotJose("José"), BotFeliz("Happy Bot")]

sys = scb.SistemaChatBot("4FunBots",lista_bots)
sys.inicio()
