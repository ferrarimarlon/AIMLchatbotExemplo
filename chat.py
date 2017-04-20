# -*- coding: latin-1 -*-

import aiml
from crawler import busca_fofocas


def conversa():
    k = aiml.Kernel()
    k.learn("startup.xml")
    k.respond("FOFOCAR")
    while True:
        resposta = k.respond(raw_input("> "))
        print resposta.decode("utf-8").encode('latin-1')


if __name__ == "__main__":
    busca_fofocas()
    conversa()
