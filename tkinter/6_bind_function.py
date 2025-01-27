import tkinter

# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

window.geometry("1400x700")


# You will create three different functions for three different events
def left_click(event):
    tkinter.Label(window, text="Left Click!").pack()


def middle_click(event):
    tkinter.Label(window, text="Middle Click!").pack()


def right_click(event):
    tkinter.Label(window, text="Right Click!").pack()


window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)

window.mainloop()
