"""
    나도코딩
    활용편2
    https://youtu.be/bKPIcoou9N8
"""

from tkinter import *

root = Tk()
root.title("Hello GUI")
root.geometry("640x480")

chkvar = IntVar()   # chkvar에 int형으로 값을 저장
checkbox = Checkbutton(root, text="오늘하루 보지 않기", variable=chkvar)
checkbox.select()
checkbox.deselect()
checkbox.pack()

def btncmd():
    pass

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()