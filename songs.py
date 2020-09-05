import sys
import os
import pygame
from random import choice
from gpiozero import Button, PWMLED
from time import sleep


led = PWMLED(25)
button = Button(23)

# Enter path to music files directory
os.chdir('/home/pi/Music/soundtracks/')

file = os.listdir()


pygame.mixer.init()
sleep(2)


def play():
    led.on()
    song = choice(file)
    print('playing song...')
    pygame.mixer.music.load(song)
    sleep(2)
    try:
        pygame.mixer.music.play()
    except:
        pass

def stop():
    try:
        led.off()
        print('stopping song')
        pygame.mixer.music.stop()
    except:
        pass


def change_song():
    led.pulse()
    print('changing song')
    pygame.mixer.music.pause()
    sleep(3)
    play()	



while True:
  
    sleep(0.1)

    if button.is_held:
        stop()

    elif led.is_lit and button.is_pressed:
            change_song()

    elif not led.is_lit and button.is_pressed:
            sleep(2)
            play()
        


