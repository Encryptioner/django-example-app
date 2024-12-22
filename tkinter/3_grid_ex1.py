import tkinter
from tkinter import *

top = tkinter.Tk()

top.geometry("1400x700")

CheckVar1 = IntVar()
CheckVar2 = IntVar()


tkinter.Checkbutton(
    top, text="Machine Learning", variable=CheckVar1, onvalue=1, offvalue=0
).grid(row=0, sticky=W)
tkinter.Checkbutton(
    top, text="Deep Learning", variable=CheckVar2, onvalue=0, offvalue=1
).grid(row=1, sticky=W)

top.mainloop()
