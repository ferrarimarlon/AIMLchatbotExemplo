# -*- coding: latin-1 -*-

from gtts import gTTS
import os
from playsound import playsound
import time
import random


def converteParaFala(frase):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    arquivo = str(random.randint(10000, 50000)) + ".mp3"
    tts = gTTS(text=frase.decode("latin-1").encode('utf-8'), lang='pt', slow=False)
    tts.save(arquivo)
    SOM = os.path.join(ROOT_DIR, arquivo)
    playsound(SOM)
    time.sleep(1)
    os.remove(arquivo)
