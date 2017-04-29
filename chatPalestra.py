# -*- coding: latin-1 -*-
import time
import aiml
from crawler import *
from tarefas import *


def conversa():
    k = aiml.Kernel()
    k.learn("startup.xml")
    k.respond("PALESTRA")
    while True:
        opcao = False
        while opcao is False:
            op = raw_input("AGUARDANDO...")
            if op != "":
                opcao = True
        print ">>"
        fala = voz()
        resposta = k.respond(fala)
        try:
            converteParaFala(resposta.decode("utf-8").encode('latin-1'))
            if resposta == "TAREFA":
                realiza_tarefas("lista")
            time.sleep(1)
        except:
            resposta = k.respond("PROBLEMA")
            converteParaFala(resposta.decode("utf-8").encode('latin-1'))
            time.sleep(1)


if __name__ == "__main__":
    busca_concursos()
    conversa()
