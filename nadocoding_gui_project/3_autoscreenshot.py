"""
    나도코딩
    활용편2
    https://youtu.be/bKPIcoou9N8
"""
import time
from PIL import ImageGrab

time.sleep(5)

for i in range(1, 11):
    img = ImageGrab.grab()      # 현재 스크린의 이미지를 가져옴)
    img.save("image{}.png".format(i))   # 파일로 저장 (image1.png ~ image 10,png)
    time.sleep(2)