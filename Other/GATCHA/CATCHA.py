from tkinter import *
import random

root = Tk()
root.resizable(False, False)
W = 350
H = 600
# Создаємо канвас
c = Canvas(root, width=W, height=H, bg="#111111")
c.pack()
# Ворота
c.create_rectangle(0, 562, 410, 610, fill="#5C5C5C")
c.create_line(0, 560, 350, 560, fill="#000", width=4, dash=(100, 5))
# Мяч
BALL = c.create_oval(50, 50, 80, 80, fill="#4CC4CD")
# Плитка яка хаває мяча
vrotar = c.create_rectangle(0, 550, 50, 565, fill="#CD7500")

# Рух мяча по вертикалі
BALL_S = 5
def move_ball():
    global gm_over
    c.move(BALL, 0, BALL_S)
    if c.coords(BALL)[1] >= 535:

        bottom = c.coords(BALL)[0] + 15
        if c.coords(vrotar)[0] < bottom < c.coords(vrotar)[2]:
           gm_over = 1
           BALL_x = random.randint(0, 9)*35
           c.coords(BALL, BALL_x, 0, BALL_x + 35, 35)
        else:
            gm_over = 0
        BALL_x = random.randint(0, 9)*35
        c.coords(BALL, BALL_x, 0, BALL_x + 35, 35)

vrotar_s = 0
def move_vrotar():
    if vrotar_s > 0 and c.coords(vrotar)[2] < 355:
        c.move(vrotar, vrotar_s, 0)
    elif vrotar_s < 0 and c.coords(vrotar)[0] > 5:
        c.move(vrotar, vrotar_s, 0)

def key_handl(event):
    #print(event.keysym)
    global vrotar_s, gm_over
    if event.keysym == "Down":
        vrotar_s = 0
    elif event.keysym == "Left":
        vrotar_s = -5
    elif event.keysym == "Right":
        vrotar_s = 5
    elif event.keysym == "Return":
        gm_over = 1
        main()

c.bind("<KeyPress>", key_handl)
c.focus_set()

def quit_prog():
    root.destroy()

btn = Button(root, width=43, height=1, text="Exit", bg="#5C5C5C",
            fg="#4CC4CD", font="Arial 10", command=quit_prog)
btn.pack()

gm_over = 0
def main():
    move_ball()
    move_vrotar()
    if gm_over:
        root.after(30, main)
main()

root.mainloop()
