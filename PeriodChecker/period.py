from datetime import datetime
from pygame import mixer
import os
import time

def playSound():
    mixer.init()
    mixer.music.load(os.path.dirname(os.path.realpath(__file__)) + "\\src\\beep.mp3")
    mixer.music.play()

def checkTime(curr_time):
    t_time = str(curr_time)
    if t_time == "07:25:00":
        print("Period 1")
        playSound()
    elif t_time == "08:19:00":
        print("Period 2")
        playSound()
    elif t_time == "09:07:00":
        print("Period 3")
        playSound()
    elif t_time == "09:55:00":
        print("Period 4")
        playSound()
    elif t_time == "10:43:00":
        print("Period B")
        playSound()
    elif t_time == "11:16:00":
        print("Period 5")
        playSound()
    elif t_time == "12:04:00":
        print("Period 6")
        playSound()
    elif t_time == "12:52:00":
        print("Period 7")
        playSound()
    elif t_time == "13:40:00":
        print("Period 8")
        playSound()
    elif t_time == "14:25:00":
        print("After School")
        playSound()

print("Period checker by Andrew Wang")
while(True):
    curr_time = datetime.now().strftime("%H:%M:%S")
    checkTime(curr_time)
    time.sleep(1)
