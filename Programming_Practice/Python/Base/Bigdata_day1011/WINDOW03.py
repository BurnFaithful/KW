from tkinter import *

window = Tk()
window.title("이미지 넣기")

imageFrame = [PhotoImage(file="test.gif", format="gif -index {}".format(i)) for i in range(10)]


def update(index):
    frame = imageFrame[index]
    index += 1
    label.configure(image=frame)
    window.after(100, update, index)


label = Label(window)
label.pack()
window.after(0, update, 0)

window.mainloop()