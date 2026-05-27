import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

entry_var = tk.StringVar()

title_label = tk.Label(
    root,
    text="Scientific Calculator",
    font=("Segoe UI", 11, "bold"),
    bg="#1e1e2e",
    fg="#888888"
)
title_label.grid(row=0, column=0, columnspan=3, padx=15, pady=(10, 0), sticky="w")

mode_label = tk.Label(
    root,
    text="DEG",
    font=("Segoe UI", 11, "bold"),
    bg="#1e1e2e",
    fg="#2ecc71"
)
mode_label.grid(row=0, column=3, columnspan=2, padx=15, pady=(10, 0), sticky="e")

entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Segoe UI", 22, "bold"),
    bg="#2a2a3d",
    fg="#ffffff",
    insertbackground="white",
    bd=0,
    relief="flat",
    justify="right"
)
entry.grid(row=1, column=0, columnspan=5, padx=15, pady=(5, 10), ipady=15, sticky="ew")


def make_btn(text, row, col, cmd, color="#3a3a5c", fg="#ffffff"):
    btn = tk.Button(
        root,
        text=text,
        font=("Segoe UI", 13, "bold"),
        bg=color,
        fg=fg,
        activebackground=color,
        activeforeground=fg,
        bd=0,
        relief="flat",
        cursor="hand2",
        command=cmd
    )
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=8, ipady=10, sticky="ew")
    return btn


def button_click(value):
    entry_var.set(entry_var.get() + str(value))


def clear():
    entry_var.set("")


def backspace():
    entry_var.set(entry_var.get()[:-1])


def calculate():
    try:
        expression = entry_var.get()
        result = eval(expression)
        history_box.insert(tk.END, f"{expression} = {result}")
        history_box.yview(tk.END)
        entry_var.set(result)
    except ZeroDivisionError:
        entry_var.set("Error: Div by Zero")
    except Exception:
        entry_var.set("Invalid Expression")


def sci_operation(op):
    try:
        val = float(entry_var.get())

        if op == "sqrt":
            result = math.sqrt(val)
        elif op == "square":
            result = val ** 2
        elif op == "log":
            result = math.log10(val)
        elif op == "ln":
            result = math.log(val)
        elif op == "sin":
            result = math.sin(math.radians(val))
        elif op == "cos":
            result = math.cos(math.radians(val))
        elif op == "tan":
            result = math.tan(math.radians(val))
        elif op == "cosec":
            result = 1 / math.sin(math.radians(val))
        elif op == "sec":
            result = 1 / math.cos(math.radians(val))
        elif op == "cot":
            result = 1 / math.tan(math.radians(val))

        entry_var.set(round(result, 6))
    except ZeroDivisionError:
        entry_var.set("Math Error")
    except ValueError:
        entry_var.set("Invalid Input")
    except Exception:
        entry_var.set("Error")


def key_press(event):
    key = event.char
    if key == "\r":
        calculate()
    elif key.lower() == "c":
        clear()


root.bind("<Key>", key_press)

buttons = [
    ("C", 2, 0, clear, "#e74c3c"),
    ("⌫", 2, 1, backspace, "#e67e22"),
    ("(", 2, 2, lambda: button_click("("), "#9b59b6"),
    ("%", 2, 3, lambda: button_click("%"), "#9b59b6"),
    (")", 2, 4, lambda: button_click(")"), "#9b59b6"),

    ("7", 3, 0, lambda: button_click("7"), "#3a3a5c"),
    ("8", 3, 1, lambda: button_click("8"), "#3a3a5c"),
    ("9", 3, 2, lambda: button_click("9"), "#3a3a5c"),
    ("*", 3, 3, lambda: button_click("*"), "#9b59b6"),
    ("√", 3, 4, lambda: sci_operation("sqrt"), "#2980b9"),

    ("4", 4, 0, lambda: button_click("4"), "#3a3a5c"),
    ("5", 4, 1, lambda: button_click("5"), "#3a3a5c"),
    ("6", 4, 2, lambda: button_click("6"), "#3a3a5c"),
    ("-", 4, 3, lambda: button_click("-"), "#9b59b6"),
    ("x²", 4, 4, lambda: sci_operation("square"), "#2980b9"),

    ("1", 5, 0, lambda: button_click("1"), "#3a3a5c"),
    ("2", 5, 1, lambda: button_click("2"), "#3a3a5c"),
    ("3", 5, 2, lambda: button_click("3"), "#3a3a5c"),
    ("+", 5, 3, lambda: button_click("+"), "#9b59b6"),
    ("log", 5, 4, lambda: sci_operation("log"), "#2980b9"),

    ("00", 6, 0, lambda: button_click("00"), "#3a3a5c"),
    ("0", 6, 1, lambda: button_click("0"), "#3a3a5c"),
    (".", 6, 2, lambda: button_click("."), "#3a3a5c"),
    ("/", 6, 3, lambda: button_click("/"), "#9b59b6"),
    ("ln", 6, 4, lambda: sci_operation("ln"), "#2980b9"),

    ("=", 7, 0, calculate, "#2ecc71"),
    ("sin", 7, 1, lambda: sci_operation("sin"), "#16a085"),
    ("cos", 7, 2, lambda: sci_operation("cos"), "#16a085"),
    ("tan", 7, 3, lambda: sci_operation("tan"), "#16a085"),
    ("π", 7, 4, lambda: entry_var.set(math.pi), "#8e44ad"),

    ("cosec", 8, 0, lambda: sci_operation("cosec"), "#16a085"),
    ("sec", 8, 1, lambda: sci_operation("sec"), "#16a085"),
    ("cot", 8, 2, lambda: sci_operation("cot"), "#16a085"),
    ("e", 8, 3, lambda: entry_var.set(math.e), "#8e44ad"),
]

for text, row, col, cmd, color in buttons:
    make_btn(text, row, col, cmd, color)

history_label = tk.Label(
    root,
    text="History:",
    font=("Segoe UI", 10, "bold"),
    bg="#1e1e2e",
    fg="#888888",
    anchor="w"
)
history_label.grid(row=9, column=0, columnspan=5, padx=15, pady=(10, 0), sticky="w")

history_box = tk.Listbox(
    root,
    font=("Segoe UI", 10),
    bg="#2a2a3d",
    fg="#cccccc",
    bd=0,
    relief="flat",
    height=4,
    selectbackground="#3a3a5c"
)
history_box.grid(row=10, column=0, columnspan=5, padx=15, pady=(0, 15), sticky="ew")

root.mainloop()
