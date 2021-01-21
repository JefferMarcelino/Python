import time
from PIL import ImageGrab
import pyautogui
from random import randint


# bg_color = (255, 255, 255)
# dino_color = (83, 83, 83)

x = randint(445, 450)
y = randint(215, 220)

def capture_screen():
    screen_o = ImageGrab.grab()
    return screen_o


def detect_enemy(screen):
     color = screen.getpixel((432, 216))
     if color == (83, 83, 83):
         return True


def jump():
    pyautogui.press("up")


print("Start in 5 seconds...")
time.sleep(5)


while True:
    screen_ = capture_screen()
    if detect_enemy(screen_):
        jump()
