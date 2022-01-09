import cv2
import math
import numpy as np
from PIL import ImageGrab
from pyautogui import press
import time


SEARCH_WINDOW_WIDTH = 50
TIME_PERIOD = 5
MODIFIER = 3
BOUNDING_BOX = (0, 250, 1366, 500)


def play_game():
    last_time = time.time()
    search_start_pixel = 175

    while True:
        screen = cv2.Canny(np.array(ImageGrab.grab(bbox=BOUNDING_BOX)), 100, 110)

        if time.time() - last_time >= TIME_PERIOD:
            search_start_pixel = search_start_pixel + MODIFIER
            last_time = time.time()

        pixel_row = screen[200][
            search_start_pixel : search_start_pixel + SEARCH_WINDOW_WIDTH
        ]

        if 255 in pixel_row:
            press("up")


play_game()
