import mouse
import keyboard
import sys
import os
import threading
from screeninfo import get_monitors
# mouse.move(300, 300, True, 2)
# mouse.move(300, 300, False, 2)


def func1():
    os.system("notepad.exe")



def func2():

    screen_w = 0
    screen_h = 0

    for monitor in get_monitors():
        screen_w = monitor.width
        screen_h = monitor.height

    mouse.move(screen_w/2-50, screen_h/2-50, True, 2)

    while True:
        keyboard.write('Deep Ocean Code \n', 0)
        mouse.move(100, 0, False, 0.2)
        if keyboard.is_pressed('e'):
            sys.exit()
        mouse.move(0, 100, False, 0.2)
        if keyboard.is_pressed('e'):
            sys.exit()
        mouse.move(-100, 0, False, 0.2)
        if keyboard.is_pressed('e'):
            sys.exit()
        mouse.move(0, -100, False, 0.2)
        if keyboard.is_pressed('e'):
            sys.exit()


# t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

# t1.start()
t2.start()
