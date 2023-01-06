import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry('500x550')
window.configure(bg='black')
window.resizable(False, False)


def calculate(operation):
    global formula

    if operation == 'C':
        formula = ''
    elif operation == 'del':
        formula = formula[0:-1]
    elif operation == '=':
        formula = str((eval(formula)))
    elif operation == 'CE':
        formula = ''
    else:
        if formula == '0':
            formula = ''
        formula += operation
    label_text.configure(text=formula)


formula = '0'
label_text = tk.Label(text=formula, font=('Roboto', 30, 'bold'), bg='black', fg='white')
label_text.place(x=12, y=50)


buttons = ['del', 'CE', '%', '+', '7', '8', '9', '-', '4', '5',
           '6', '*', '1', '2', '3', '/', '+/-', '0', '.', '=']
x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text=button, bg='grey', font=("Robooto", 20), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 18
        y += 81

window.mainloop()

