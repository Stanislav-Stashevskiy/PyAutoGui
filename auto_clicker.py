import pyautogui as pg
import time

quantity = int(input('введите кол-во кликов:'))
print('у вас 10 секунд чтобы навести мышь на место кликов!')
time.sleep(10)

for i in range(quantity):
    pos = pg.position()
    pg.click(pos)
