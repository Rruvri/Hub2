import time
import os


def clear_console():
    os.system('clear')

def sleep(int):
    return time.sleep(int)

def menu_hold(func):
    def wrapper(*args, **kwargs):
        check = True
        while check:
            func(*args, **kwargs)
            exit = input("\n[return] to exit")
            if exit == '':
                check = False             
    return wrapper

def indexer(func):
    def wrapper(*args, **kwargs):
        pass