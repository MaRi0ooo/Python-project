import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile

def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, "w")
    out.write(data)
    out.close()

def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def Read1():
    file_info = Read()
    user_text.insert(tkinter.END, file_info)

def Count():
    text1 = Read()
    index = 0
    c1 = 0
    c2 = 0
    c3 = 0
    for i in text1:
        if i == ".":
            index += 1
        elif i == ",":
            c1 += 1
        elif i == "!":
            c2 += 1
        elif i == " ":
            c3 += 1

window = tkinter.Tk()
window.title("Текстовий блокнот")
# Розмір
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
# Текстовик
text = tkinter.Text(window, width=60, height=29, wrap=WORD)
# Скрол-бар справа
scrl_b = Scrollbar(window, orient=VERTICAL, command=text.yview)
scrl_b.pack(side=RIGHT, fill=Y)
text.configure(yscrollcommand=scrl_b.set)
text.pack()
# Кнопки
btn_open = Button(text="Відкрити", width=30, command=open_file, font=("sans 10"))
btn_save = Button(text="Зберегти", width=30, command=save_file, font=("sans 10"))
btn_open.pack(side=LEFT)
btn_save.pack(side=RIGHT)

count_button = tkinter.Button(window, text="Count")
count_button.place(x=105,y=0, width=100)

count_button.config(command = Count, bg = "RosyBrown3")

window.mainloop()








































