"""
    나도코딩
    활용편2
    https://youtu.be/bKPIcoou9N8
"""

from tkinter import *

root = Tk()
root.title("Hello GUI")
#root.geometry("600x480")
#root.geometry("600x480+300+100")    # 가록 * 세로 + x좌표 + y좌표
#root.resizable(False, False)        # x(너비), y(너비) 값 변경 불가 (창 크리 변경 불가) / 최대화 아이콘도 비활성화

btn1 = Button(root, text="버튼1")
btn1.pack()

root.mainloop()