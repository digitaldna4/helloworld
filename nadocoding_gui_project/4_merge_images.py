"""
    나도코딩
    활용편2
    https://youtu.be/bKPIcoou9N8
"""
import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *   # __all__ 
from tkinter import filedialog  # 서브 모듈이기 때문에..
from PIL import Image

root = Tk()
root.title("Hello Project GUI")


# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir=r"d:\Workspaces\HelloWorld\helloworld\nadocoding_pygame_project\images")
    
    for file in files:
        #print(file)
        list_file.insert(END, file)

# 저장 경로
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None: # 사용자가 취소를 누를때
        return
    #print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합
def merge_image():
    #print(list_file.get(0, END))
    images = [Image.open(x) for x in list_file.get(0, END)]
    widths = [x.size[0] for x in images]
    heights = [x.size[1] for x in images]
    # print("width : ", widths)
    # print("height : ", heights)

    max_width, total_height = max(widths), sum(heights)
    print("max width :", max_width)
    print("total height : ", total_height)

    result_img = Image.new("RGM", (max_width, total_height), (255, 255, 255))
    y_offset = 0    # y위치
    for img in images:
        result_img.paste(img, (o, y_offset))
        y_offset += img.size[1]

    dest_path = os.path.join(txt_dest_path.get(), "hello_photo.jpg")

# 시작
def start():
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    # 이미지 통합 작업
    merge_image()

# 선택 삭제
def del_file():
    #print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)
 
        
# 파일 프레임 (파일 추가, 선택 삭제 버튼)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")


# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


# 저장경로 프레임
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)       # "1.0" END
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)  # ipady 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


# 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(padx=5, pady=5, ipady=5)

lbl_width = Label(option_frame, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)


lbl_space = Label(option_frame, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(option_frame, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)


lbl_format = Label(option_frame, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


# 진행상황 progress bar
progress_frame = LabelFrame(root, text="진행상황")
progress_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_close = Button(run_frame, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(run_frame, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()