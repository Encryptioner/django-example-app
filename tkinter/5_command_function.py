import tkinter

# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

window.geometry("1400x700")


# creating a function called DataCamp_Tutorial()
def DataCamp_Tutorial():
    tkinter.Label(window, text="GUI with Tkinter!").pack()


tkinter.Button(window, text="Click Me!", command=DataCamp_Tutorial).pack()
window.mainloop()
