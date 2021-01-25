from tkinter import *
def motion2(event):
    global x2
    global y2
    x2 = event.x
    y2 = event.y
    pole.coords(ball2, x2, y2, x2 + 100, y2 +100)

def motion():
    global x
    global y
    x = x+dx
    y = y+dy
    pole.coords(ball, x, y, x+100, y+100)
    window.after(20, motion)

window = Tk()
pole = Canvas(window, width = 600, height = 500, bg = "purple")
pole.pack()
dx = 5
dy = 5
x = 0
y = 0
ball = pole.create_oval(x, y, x+100, y+100, fill = "white")
x2 = 100
y2 = 100
ball2 = pole.create_oval(x2, y2, x2 + 100, y2 + 100, fill = "black")
window.after(0, motion)

window.bind("<Motion>", motion2)
window.mainloop()

