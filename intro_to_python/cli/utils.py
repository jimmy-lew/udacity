from sys import platform
from time import sleep
from window import Window
import os


def clear_terminal():
    os.system('clear' if platform == "linux" or "darwin" else 'cls')


def throw_error():
    print('Sorry, I didn\'t understand that. Please try again.')
    sleep(1.0)
    clear_terminal()


def repeating_prompt(win: Window, prompt: str):
    win.create([prompt])
    response = input('[y/n]: ')

    if response.lower() == 'n':
        return False
    elif response.lower() == 'y':
        return True
    else:
        throw_error()
        return repeating_prompt(win, prompt)
