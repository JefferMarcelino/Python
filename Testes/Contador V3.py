"""Contador V2"""

import os
from time import sleep


def contador(time):
    os.system("clear")
    c = 0
    time = time + 1
    while True:
        time = time - 1
        if time == -1:
            break
        print("\033[31mStart in {} seconds\033[m".format(time), end="")
        print("." * c)
        if c < 3:
            c = c + 1
        else:
            c = c - 3
        sleep(1)
        os.system("clear")


contador(150)

