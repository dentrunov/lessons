from tkinter import *
dig = ''
num = 0
op = ''

def C(event):
    global dig
    dig = ''
    label['text'] = ''

def plus(event):
   global op
   op = 'plus'
   global num
   global dig
   num = int(dig)
   dig = ''
   label['text'] = ''

def minus(event):
    global op
    op = 'minus'
    global num
    global dig
    num = int(dig)
    dig = ''
    label['text'] = ''

def equal(event):
    global op
    global num
    global dig
    num1 = int(dig)
    dig = ''
    if op == 'plus':
        label['text'] = num + num1
    elif op == 'minus':
        label['text'] = num - num1

def digit(d):
    global dig
    dig += str(d)
    label['text'] = dig

root = Tk()
root.geometry('400x600')

label = Label(width=20, font=("Arial", 22))
button1 = Button(width=5, height=2, text ='1', font=("Arial", 22, "bold"), command= lambda x=1: digit(x))
button2 = Button(width=5, height=2, text ='2', font=("Arial", 22, "bold"), command= lambda x=2: digit(x))
button3 = Button(width=5, height=2, text ='3', font=("Arial", 22, "bold"), command= lambda x=3: digit(x))
button4 = Button(width=5, height=2, text ='4', font=("Arial", 22, "bold"), command= lambda x=4: digit(x))
button5 = Button(width=5, height=2, text ='5', font=("Arial", 22, "bold"), command= lambda x=5: digit(x))
button6 = Button(width=5, height=2, text ='6', font=("Arial", 22, "bold"), command= lambda x=6: digit(x))
button7 = Button(width=5, height=2, text ='7', font=("Arial", 22, "bold"), command= lambda x=7: digit(x))
button8 = Button(width=5, height=2, text ='8', font=("Arial", 22, "bold"), command= lambda x=8: digit(x))
button9 = Button(width=5, height=2, text ='9', font=("Arial", 22, "bold"), command= lambda x=9: digit(x))
button0 = Button(width=10, height=2, text ='0', font=("Arial", 22, "bold"), command= lambda x=0: digit(x))
buttonC = Button(width=5, height=2, text ='C', font=("Arial", 22, "bold"), bg='#ff0000')
button_equal = Button(width=5, height=2, text ='=', font=("Arial", 22, "bold"))
button_plus = Button(width=5, height=2, text ='+', font=("Arial", 22, "bold"))
button_minus = Button(width=5, height=2, text ='-', font=("Arial", 22, "bold"))



button_equal.bind('<Button-1>', equal)
button_plus.bind('<Button-1>', plus)
button_minus.bind('<Button-1>', minus)
buttonC.bind('<Button-1>', C)


label.grid(row=5 , column=0, columnspan=3)
button1.grid(row=2 , column=0)
button2.grid(row=2 , column=1)
button3.grid(row=2 , column=2)
button4.grid(row=1 , column=0)
button5.grid(row=1 , column=1)
button6.grid(row=1 , column=2)
button7.grid(row=0 , column=0)
button8.grid(row=0 , column=1)
button9.grid(row=0 , column=2)
button0.grid(row=3 , column=0, columnspan=2)
buttonC.grid(row=3 , column=3)
button_equal.grid(row=4 , column=0)
button_plus.grid(row=4 , column=1)
button_minus.grid(row=4 , column=2)




root.mainloop()