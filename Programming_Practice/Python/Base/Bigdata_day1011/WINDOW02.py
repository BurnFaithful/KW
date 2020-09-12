from tkinter import *

window = Tk()
window.title("윈도우 창 연습")
window.geometry("400x100")

label1 = Label(window, text="Windows ~~~ Python을")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")

label1.pack()
label2.pack()

window.mainloop()