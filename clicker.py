import pyautogui as pg

a = 0

while True:
    pg.alert(a, 'Клики:', button="Жми!")
    a += 1


