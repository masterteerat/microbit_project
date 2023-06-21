
#Importing library
from microbit import *
import random
import music
import time



#Initialize starting var
speaker.on
lvl = 1
score = 0
timeout = 0
life = 3
start = 0

#level loop
while True:
    #Initialize var
    ms = 0
    sec = 0
    ans = 0    
    weight = 7
    #Random ascii char
    if lvl == 1:
        ascii = random.randint(48, 57)
        timeout = 20
    if lvl == 2:
        ascii = random.randint(65, 90)
        timeout = 17
    if lvl == 3:
        ascii = random.randint(65, 122)
        timeout = 14
    if lvl == 4:
        ascii = random.randint(48, 126)
        timeout = 10
    #ascii = 255
    display.show(chr(ascii))

    #round loop
    while True:
        if button_b.is_pressed():
            music.set_tempo(bpm=1500)
            music.play(['C5', 'C5', 'B', 'B', 'C5'], wait=False)
            display.clear()
            display.show(1)
            time.sleep(0.2) 
            display.show(chr(ascii))
            ans = ans + 2 ** weight
            weight += -1
        if button_a.is_pressed():
            music.set_tempo(bpm=1500)
            music.play(['E', 'E', 'F', 'F', 'G'], wait=False)
            display.clear()
            display.show(0)
            time.sleep(0.2) 
            display.show(chr(ascii))
            weight += -1
        if weight == -1:
            if ans == ascii:
                music.set_tempo(bpm=500)
                music.play(['E', 'E', 'E', 'E', 'G'], wait=False)
                display.show(Image.YES)
                time.sleep(0.5)
                score += 1
                break
            if ans != ascii:
                music.set_tempo(bpm=500)
                music.play(['F', 'F', 'F', 'F', 'G'], wait=False)
                display.show(Image.NO)
                time.sleep(0.5)
                life += -1
                break
        #time out warning        
        if sec >= (timeout - 5):
            display.clear()
            time.sleep(0.5)
            display.show(chr(ascii))    
        #time out        
        if sec > timeout:
            music.set_tempo(bpm=500)
            music.play(['F', 'F', 'F', 'F', 'G'], wait=False)
            display.show(Image.NO)
            time.sleep(1)
            life += -1
            break       
        ms = ms + 300
        sec = ms // 1000
        time.sleep(0.3)
    #Game over checker
    if life == 0:
        display.show(Image.SAD)
        time.sleep(1)
        break       
    #Win checker
    if score == 5:
        display.show(Image.HAPPY)
        time.sleep(1)
        #level up
        score = 0
        life = 3
        lvl += 1
        lvlup = "level" + str(lvl)
        display.scroll(lvlup)
        #End game.
        if lvl == 5:
            display.scroll("You win!")
            break
               
    
    
    
    
            