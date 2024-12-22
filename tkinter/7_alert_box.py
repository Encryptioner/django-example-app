import tkinter
import tkinter.messagebox

# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

window.geometry("1400x700")

# Let's create a alert box with 'messagebox' function
tkinter.messagebox.showinfo("Alert Message", "This is just a alert message!")

# Let's also create a question for the user and based upon the response [Yes or No Question] display a message.
response = tkinter.messagebox.askquestion(
    "Tricky Question", "Do you love Deep Learning?"
)

# A basic 'if/else' block where if user clicks on 'Yes' then it returns 1 else it returns 0. For each response you will display a message with the help of 'Label' method.
if response == 1:
    tkinter.Label(window, text="Yes, offcourse I love Deep Learning!").pack()
else:
    tkinter.Label(window, text="No, I don't love Deep Learning!").pack()

window.mainloop()
