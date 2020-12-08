from tkinter import *
Calci = Tk()
Calci.title("calculator")
def on_click(n) :
    global operator
    operator = operator + str(n)
    text_input.set(operator)
def Equal_to():
    global operator
    Sumup = eval(operator)
    text_input.set(Sumup)

text_input = StringVar()
operator = ''
Display = Entry(Calci, bg='grey', bd=30, font=('arial', 16, 'bold'), justify='right', textvariable=text_input).grid(columnspan=4)
all_clear = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='10px', text="AC", pady='4px', bd=5).grid(row=1, column=0)
sum_minus = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='11px', text="+/-", pady='4px', bd=5).grid(row=1, column=1)
percent = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='14px', text="%", pady='4px', bd=5).grid(row=1, column=2)
divide = Button(Calci, bg='orange', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="/", pady='5px', bd=5, command = lambda: on_click('/')).grid(row=1, column=3)

btn1 = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="1", pady='5px', bd=5, command = lambda: on_click(1)).grid(row=2, column=0)
btn2 = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="2", pady='5px', bd=5, command = lambda: on_click(2)).grid(row=2, column=1)
btn3 = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="3", pady='5px', bd=5, command = lambda: on_click(3)).grid(row=2, column=2)
multiple = Button(Calci, bg='orange', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="*", pady='5px', bd=5, command = lambda:on_click('*')).grid(row=2, column=3)

btn4 = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="4", pady='5px', bd=5, command = lambda: on_click(4)).grid(row=3, column=0)
btn5 = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="5", pady='5px', bd=5, command = lambda: on_click(5)).grid(row=3, column=1)
btn6 = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="6", pady='5px', bd=5, command = lambda: on_click(6)).grid(row=3, column=2)
subtract = Button(Calci, bg='orange', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="-", pady='5px', bd=5, command = lambda:on_click('-')).grid(row=3, column=3)

btn7 = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="7", pady='5px', bd=5, command = lambda: on_click(7)).grid(row=4, column=0)
btn8 = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="8", pady='5px', bd=5, command = lambda: on_click(8)).grid(row=4, column=1)
btn9 = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="9", pady='5px', bd=5, command = lambda: on_click(9)).grid(row=4, column=2)
add = Button(Calci, bg='orange', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="+", pady='5px', bd=5, command = lambda: on_click('+')).grid(row=4, column=3)

btn0 = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="0", pady='5px', bd=5, command = lambda: on_click(0)).grid(row=5, column=0)
bracket = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='15px', text="()", pady='5px', bd=5).grid(row=5, column=1)
dot = Button(Calci, bg='black', fg='light grey', font=('arial', 16, 'bold'), padx='18px', text=".", pady='5px', bd=5, command = lambda: on_click('.')).grid(row=5, column=2)
equal = Button(Calci, bg='orange', fg='light grey', font=('arial', 16, 'bold'), padx='16px', text="=", pady='5px', bd=5, command = lambda: Equal_to()).grid(row=5, column=3)

Calci.mainloop()
