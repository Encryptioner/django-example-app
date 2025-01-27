import tkinter

window = tkinter.Tk()
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text="Welcome to DataCamp's Tutorial on Tkinter!").pack()
window.mainloop()
