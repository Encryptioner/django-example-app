import tkinter as tk
from tkinter import filedialog, messagebox  # pylint: disable=no-name-in-module
import requests

# API URL (replace with your actual Django contact API endpoint)
API_URL = "http://127.0.0.1:8000/polls/api/contact/"


def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    message = message_entry.get("1.0", tk.END).strip()
    file_path = file_label["text"]

    # Validate inputs
    if not name or not email or not message:
        messagebox.showerror("Validation Error", "All fields except file are required.")
        return

    try:
        # Prepare data and files for API request
        data = {
            "name": name,
            "email": email,
            "message": message,
        }
        files = (
            {"file": open(file_path, "rb")}
            if file_path and file_path != "No file selected"
            else None
        )

        # Send data to the Django API
        response = requests.post(API_URL, data=data, files=files)
        response.raise_for_status()

        # Handle successful submission
        messagebox.showinfo("Success", "Contact information submitted successfully!")
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        message_entry.delete("1.0", tk.END)
        file_label.config(text="No file selected")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to submit contact information: {e}")
    except FileNotFoundError:
        messagebox.showerror("Error", "Selected file not found!")


def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=file_path)


# Create Tkinter window
root = tk.Tk()
root.title("Contact Form")

# Name field
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Email field
tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=1, column=1, padx=10, pady=5)

# Message field
tk.Label(root, text="Message").grid(row=2, column=0, padx=10, pady=5, sticky="ne")
message_entry = tk.Text(root, width=30, height=10)
message_entry.grid(row=2, column=1, padx=10, pady=5)

# File upload
tk.Label(root, text="Attachment").grid(row=3, column=0, padx=10, pady=5, sticky="e")
file_button = tk.Button(root, text="Choose File", command=select_file)
file_button.grid(row=3, column=1, padx=10, pady=5, sticky="w")
file_label = tk.Label(root, text="No file selected", fg="gray")
file_label.grid(row=3, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")

# Run the application
root.mainloop()
