import pyautogui as pg
import random as ran
import time as tm

while True:
    pos = pg.position()
    a = ran.randint(1, 5)

    if a == 1:
        for i in range(10):
            pg.click(pos)
        tm.sleep(5)
        continue

    if a == 2:
        pg.hotkey('alt', 'shift')
        tm.sleep(5)
        continue

    if a == 3:
        pg.hotkey('alt', 'tab')
        tm.sleep(5)
        continue

    if a == 5:
        pg.write('Hello world!', interval=0.25)
        pg.moveTo(0, 0, duration=0.2)
        tm.sleep(5)
        continue
