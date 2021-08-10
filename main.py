from tkinter import *

def f(event):
    text = entry.get()
    label['text'] = text


root = Tk()
root.geometry('400x300')

button = Button(text ='Нажать')
entry = Entry(width=50)
label = Label(text='Это текст')

button.bind('<Button-1>', f)

entry.pack()
button.pack()
label.pack()

root.mainloop()