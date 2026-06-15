import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("Admin Login")
root.geometry("300x200")

tk.Label(root, text="Username").pack()

username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()

password = tk.Entry(root, show="*")
password.pack()


def login():

    user = username.get()
    pwd = password.get()

    if user == "admin" and pwd == "1234":

        messagebox.showinfo(
            "Success",
            "Login Successful"
        )

        root.destroy()

        os.system("python gui.py")

    else:

        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
        )


tk.Button(
    root,
    text="Login",
    command=login
).pack(pady=20)

root.mainloop()