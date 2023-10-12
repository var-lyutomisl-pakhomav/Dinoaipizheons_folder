import tkinter as tk
from tkinter import messagebox

def show_messages(i, message, top):
    for _ in range(i):
        messagebox.showinfo(top, message)

root = tk.Tk()
root.title("")
root.geometry("0x0")

show_messages(10, "你是智障", "警告")
root.destroy()
root.mainloop()






