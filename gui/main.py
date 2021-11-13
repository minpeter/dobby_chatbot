from tkinter import *

root = Tk()

label = Label(root, text='test text')
label.pack()

button1 = Button(root, text='button 1')
button1.pack()


root.title("test")
root.geometry("300x200+100+100")
root.resizable(False, False)

root.mainloop()