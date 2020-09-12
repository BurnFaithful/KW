from tkinter import *
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼 클릭됨.")


window = Tk()

button = Button()

window.bind("<Button-1>", clickLeft)
window.mainloop()