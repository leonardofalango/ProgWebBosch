# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:18:34 2022

@author: DISRCT
"""

import pynput
import time
from pynput.keyboard import Key, Controller
from pynput import keyboard
controller = Controller()

a = ''

commands = [Key.delete, Key.delete, Key.delete, Key.down] #Enter the command list here

timestart = 3 #Enter the time ti start the repetitions
timebkeys = 0.01 #Time between keys

rep = 12 #Enter with the repetitions



time.sleep(timestart)
for rep in range(rep):
    for i in range(len(commands)):
        if rep >=9:
            if i == 1:
                pass
            else:
                controller.press(commands[i])
                time.sleep(timebkeys)
        else:
            controller.press(commands[i])
            time.sleep(timebkeys)
            



