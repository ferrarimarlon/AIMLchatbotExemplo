# -*- coding: latin-1 -*-

import gtts
# !/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import time

import speech_recognition as sr

fala = ""


# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        global fala
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        fala = recognizer.recognize_google(audio, language="pt")
    except sr.UnknownValueError:
        fala = "FALHA"
    except sr.RequestError as e:
        fala = "Erro no servico de conversao; {0}".format(e)


def voz():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

    # start listening in the background (note that we don't have to do this inside a `with` statement)
    stop_listening = r.listen_in_background(m, callback)
    # `stop_listening` is now a function that, when called, stops background listening

    # do some other computation for 5 seconds, then stop listening and keep doing other computations
    for _ in range(50):
        time.sleep(0.1)  # we're still listening even though the main thread is doing other things
    stop_listening()  # calling this function requests that the background listener stop listening
    return fala
