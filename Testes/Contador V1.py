"""Contador V1"""

import os
from time import sleep

c = 0
n = 101

while True:
    n = n - 1
    if n == -1:
        break
    print("Start in {} seconds".format(n), end="")
    print("." * c)
    if c < 3:
        c = c + 1
    else:
        c = c - 3
    sleep(1)
    os.system("cls")

