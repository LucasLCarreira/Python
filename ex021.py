# Exercício Python 020
# Programa que abra e reproduza um arquivo mp3
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input()
