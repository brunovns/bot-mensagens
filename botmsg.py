from pip import main
import pyautogui
import time
from threading import Thread
from pynput import keyboard

def main():
    main.status = 'run'

    #f = open("text", "r")
    while True:

        #for word in f:
        while main.status == 'pause':
            exit()

        time.sleep(1.55)
        pyautogui.typewrite('t')
        pyautogui.press("enter")

def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'pause'
            exit()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

Thread(target=main).start()
Thread(target=exit_program).start()