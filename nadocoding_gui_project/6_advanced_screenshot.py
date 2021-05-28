"""
    나도코딩
    활용편2
    https://youtu.be/bKPIcoou9N8
"""

import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")     # 2020년 6월 1일 10시 20분 30초 --> _20200601_102030
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("tbF9", screenshot)

keyboard.wait("esc")