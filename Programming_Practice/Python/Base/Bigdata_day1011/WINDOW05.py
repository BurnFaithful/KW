from tkinter import *
from tkinter import messagebox

def onclick():
    messagebox.showinfo("버튼", "클릭")


window = Tk()
window.title("이미지 클릭시 메시지박스")
window.geometry("400x200")

photo = PhotoImage(file="test.gif")
button = Button(window, image=photo, command=onclick)

button.pack()
window.mainloop()