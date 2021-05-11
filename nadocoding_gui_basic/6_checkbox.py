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
# checkbox.select()
# checkbox.deselect()
checkbox.pack()

chkvar2 = IntVar() 
checkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
checkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: 체크해제, 1: 체크
    print(chkvar2.get())
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()