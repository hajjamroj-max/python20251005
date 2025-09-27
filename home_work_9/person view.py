from tkinter import *
from moudle import clear, calculate, add_character

# Create window
win = Tk()
win.title("Simple Calculator")
win.geometry("400x500")

# Use StringVar for easier display management
display_text = StringVar()
display = Entry(win, font=('Arial', 18), justify='right', textvariable=display_text)
display.place(x=50, y=30, width=300, height=60)

# Create wrapper functions
def wrapper_clear():
    clear(display_text)

def wrapper_calculate():
    calculate(display_text)

def wrapper_add_character(char):
    def inner():
        add_character(display_text, char)
    return inner

# دکمه‌ها (مانند قبل)
Button(win, text='7', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("7")).place(x=50, y=120)
Button(win, text='8', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("8")).place(x=130, y=120)
Button(win, text='9', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("9")).place(x=210, y=120)
Button(win, text='/', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("/")).place(x=290, y=120)

Button(win, text='4', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("4")).place(x=50, y=180)
Button(win, text='5', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("5")).place(x=130, y=180)
Button(win, text='6', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("6")).place(x=210, y=180)
Button(win, text='*', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("*")).place(x=290, y=180)

Button(win, text='1', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("1")).place(x=50, y=240)
Button(win, text='2', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("2")).place(x=130, y=240)
Button(win, text='3', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("3")).place(x=210, y=240)
Button(win, text='-', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("-")).place(x=290, y=240)

Button(win, text='0', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("0")).place(x=50, y=300)
Button(win, text='.', font=('Arial', 16), width=6, height=2, command=wrapper_add_character(".")).place(x=130, y=300)
Button(win, text='+', font=('Arial', 16), width=6, height=2, command=wrapper_add_character("+")).place(x=290, y=300)

# Equal button
Button(win, text='=', font=('Arial', 16), width=6, height=2, command=wrapper_calculate).place(x=210, y=300)

# Control buttons
Button(win, text='C', font=('Arial', 16), width=6, height=2, bg='red', fg='white', command=wrapper_clear).place(x=290, y=360)

win.mainloop()