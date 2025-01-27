import tkinter
import os

# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

window.geometry("1400x700")

project_root = os.path.dirname(os.path.dirname(__file__))
# Construct the full path to the image
image_path = os.path.join(project_root, "media", "sample", "Sample-PNG-Image.png")

# In order to display the image in a GUI, you will use the 'PhotoImage' method of Tkinter. It will an image from the directory (specified path) and store the image in a variable.
icon = tkinter.PhotoImage(file=image_path)

# Finally, to display the image you will make use of the 'Label' method and pass the 'image' variriable as a parameter and use the pack() method to display inside the GUI.
label = tkinter.Label(window, image=icon)
label.pack()

window.mainloop()
