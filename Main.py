import math
from tkinter import messagebox
from tkinter import *

wnd = Tk()
wnd.title('Калькулятор')
wnd.geometry('235x460')
wnd.resizable(False, False)
frame = Frame(wnd)
setStyle = {'bg': '#4f4f4f', 'font': 'bold', 'foreground': 'white', 'width': '4', 'height': '3'}

def clc(n):
    text.insert(10.0, str(n))

def clc_delete_all():
    text.delete(1.0, END)

def clc_delete():
    t = text.get(1.0, END)
    removed_last = t[:-2]
    text.delete(1.0, END)
    text.insert(10.0, str(removed_last))

def clc_result():
    try:
        result = eval(text.get(1.0, END))
        clc_delete_all()
        text.insert(10.0, result)
        print('im fuckin u with ur percents :)')
    except SyntaxError:
        formula = text.get(1.0, END)
        ind_proc = formula.index('%')
        if formula.find('-') != -1:
            ind_min = formula.index('-')
            print(ind_proc, ind_min)
            if ind_proc < ind_min:
                messagebox.showerror('Ошибка', 'Введите числа по порядку еп!')
            else:
                ind_x = ind_proc - ind_min
                x = float(formula[:ind_x])
                y = float(formula[(ind_min + 1):-2])
                res = x - (x * y * 0.01)
                clc_delete_all()
                text.insert(10.0, str(res))
        else:
            ind_plus = formula.index('+')
            ind_x = ind_proc - ind_plus
            x = float(formula[:ind_x])
            y = float(formula[(ind_plus + 1):-2])
            res = x + (x * y * 0.01)
            clc_delete_all()
            text.insert(10.0, str(res))
    except (ValueError, NameError):
        messagebox.showerror('Ошибка', 'Неверный формат ввода!')

def clc_pow():
    result = pow(eval(text.get(1.0, END)), 2)
    clc_delete_all()
    text.insert(10.0, result)

def clc_sqrt():
    result = math.sqrt(eval(text.get(1.0, END)))
    clc_delete_all()
    text.insert(10.0, result)

text = Text(frame, height=6, width=25, font = 'bold', bg = '#7c7c7c', foreground = 'white')
text.grid(row = 0, column = 0, columnspan = 5)
Button(frame, setStyle, text = '1', command=lambda:[clc(1)]).grid(row = 2, column = 0)
Button(frame, setStyle, text = '2', command=lambda:[clc(2)]).grid(row = 2, column = 1)
Button(frame, setStyle, text = '3', command=lambda:[clc(3)]).grid(row = 2, column = 2)
Button(frame, setStyle, text = '4', command=lambda:[clc(4)]).grid(row = 3, column = 0)
Button(frame, setStyle, text = '5', command=lambda:[clc(5)]).grid(row = 3, column = 1)
Button(frame, setStyle, text = '6', command=lambda:[clc(6)]).grid(row = 3, column = 2)
Button(frame, setStyle, text = '7', command=lambda:[clc(7)]).grid(row = 4, column = 0)
Button(frame, setStyle, text = '8', command=lambda:[clc(8)]).grid(row = 4, column = 1)
Button(frame, setStyle, text = '9', command=lambda:[clc(9)]).grid(row = 4, column = 2)
Button(frame, setStyle, text = '0', width=9, height=3, command=lambda:[clc(0)]).grid(row = 5, column = 0, columnspan = 2)
Button(frame, setStyle, text = '.', command=lambda:[clc('.')]).grid(row = 5, column = 2)
Button(frame, setStyle, text = '+', command=lambda:[clc('+')]).grid(row = 1, column = 0)
Button(frame, setStyle, text = '*', command=lambda:[clc('*')]).grid(row = 1, column = 1)
Button(frame, setStyle, text = '/', command=lambda:[clc('/')]).grid(row = 1, column = 2)
Button(frame, setStyle, text = '-', command=lambda:[clc('-')]).grid(row = 1, column = 3)
Button(frame, setStyle, text = 'CE', command=clc_delete_all).grid(row = 2, column = 4)
Button(frame, setStyle, text = 'C', command=clc_delete).grid(row = 3, column = 4)
Button(frame, setStyle, text = '=', width=4, height=7, command=clc_result).grid(row = 4, column = 4, rowspan = 2)
Button(frame, setStyle, text = '%', command=lambda:[clc('%')]).grid(row = 1, column = 4)
Button(frame, setStyle, text = 'x²', command=clc_pow).grid(row =4, column = 3)
Button(frame, setStyle, text = '√х', command=clc_sqrt).grid(row = 5, column = 3)
Button(frame, setStyle, text = '(', command=lambda:[clc('(')]).grid(row =2, column = 3)
Button(frame, setStyle, text = ')', command=lambda:[clc(')')]).grid(row = 3, column = 3)

frame.pack(expand=True)
wnd.mainloop()