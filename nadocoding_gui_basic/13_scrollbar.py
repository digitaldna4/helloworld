"""
    나도코딩
    활용편2
    https://youtu.be/bKPIcoou9N8
"""

import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Hello GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set )
for i in range(1,32):   # 1 ~ 31일 (미만)
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()