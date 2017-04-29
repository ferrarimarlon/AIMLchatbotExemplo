# -*- coding: latin-1 -*-

from vozDoBot import converteParaFala
from test import voz
import datetime
import smtplib


def mandar_email(mensagem):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("mfmarlonferrari@gmail.com", "p9s800dx")
    server.sendmail("mfmarlonferrari@gmail.com", "mfmarlonferrari@gmail.com", mensagem)
    server.quit()


def realiza_tarefas(qualTarefa):
    numeros = {'1': 1, '2': 2, '3': 3, 'um': 1, 'três': 3}
    # lista padrao
    quantidade = 4
    if qualTarefa == 'lista':
        conseguiu = False
        while conseguiu is False:
            try:
                converteParaFala("Quantos itens?")
                print ">>"
                tarefa = voz()
                print "--"
                print(tarefa)
                quantidade = numeros[tarefa]
                conseguiu = True
            except:
                converteParaFala("Não escutei. De novo:")
        itens = []
        for x in range(quantidade):
            try:
                converteParaFala("Item " + str(x + 1))
                item = voz().encode('latin-1')
                print item
                if item == "FALHA":
                    raise ArithmeticError
                converteParaFala(item)
                itens.append(item)
            except:
                x = x - 1
        converteParaFala("Pronto: Vou mandar por email.")
        mensagem = ""
        for l in itens:
            mensagem += l + "\n"
        mandar_email(mensagem)

        # realiza_tarefas('lista')
