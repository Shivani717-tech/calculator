import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            input_var.set("")
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)

# Initialize main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""
input_var = tk.StringVar()

# Entry widget for display
entry = tk.Entry(root, textvar=input_var, font="Arial 20", bd=8, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 0, 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 15", relief=tk.RAISED, bd=3, width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()