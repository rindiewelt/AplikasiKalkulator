from tkinter import *
from tkinter import font as tkfont

root = Tk()
root.title('Kalkulator')
root.resizable(width=False, height=False)

HEIGHT = 500
WIDTH = 300
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

numFont = tkfont.Font(family='Helvetica', size=16)

tambah = 0
kurang = 0
kali = 0
bagi = 0
persentase = 0


def append_number(num):
    current = str(number.get())
    number.delete(0, END)
    if num == ".":
        if current.find(".") == -1:
            number.insert(0, current + str(num))
        else:
            number.insert(0, current)
    else:
        number.insert(0, current + str(num))


def PlusMinus():
    check = number.get()
    if check[0] == '-':
        number.delete(0)
    else:
        number.insert(0, "-")


def Backspace():
    number.delete(len(number.get()) - 1)


def ClearNumber():
    number.delete(0, END)
    number.insert(0, 0)


def Tambah():
    var = number.get()
    global x
    x = float(var)
    number.delete(0, END)
    global tambah
    tambah = 1


def Kurang():
    var = number.get()
    global x
    x = float(var)
    number.delete(0, END)
    global kurang
    kurang = 1


def Kali():
    var = number.get()
    global x
    x = float(var)
    number.delete(0, END)
    global kali
    kali = 1


def Bagi():
    var = number.get()
    global x
    x = float(var)
    number.delete(0, END)
    global bagi
    bagi = 1


def Persentase():
    var = number.get()
    global x
    x = float(var)
    number.insert(len(number.get()), "%")
    global persentase
    persentase = 1


def SamaDengan():
    global tambah, kurang, kali, bagi, persentase
    y = number.get()
    number.delete(0, END)
    if tambah == 1:
        number.insert(0, x + float(y))
        tambah, kurang, kali, bagi, persentase = 0,0,0,0,0
    elif kurang == 1:
        number.insert(0, x - float(y))
        tambah, kurang, kali, bagi, persentase = 0,0,0,0,0
    elif kali == 1:
        number.insert(0, x * float(y))
        tambah, kurang, kali, bagi, persentase = 0,0,0,0,0
    elif bagi == 1:
        number.insert(0, x / float(y))
        tambah, kurang, kali, bagi, persentase = 0,0,0,0,0
    elif persentase == 1:
        number.insert(0, x / 100)
        tambah, kurang, kali, bagi, persentase = 0,0,0,0,0


frameNOL = Frame(root)
frameNOL.place(relx=0.5, rely=1, relheight=0.15, relwidth=1, anchor='s')
plusminus = Button(frameNOL, text='+/-', borderwidth=0, command=PlusMinus)
plusminus.place(relx=0, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
nol = Button(frameNOL, text='0', borderwidth=0, command=lambda: append_number(0))
nol.place(relx=0.25, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
dot = Button(frameNOL, text='.', borderwidth=0, command=lambda: append_number("."))
dot.place(relx=0.5, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
equal = Button(frameNOL, text='=', borderwidth=0, command=SamaDengan)
equal.place(relx=0.75, rely=0.5, relheight=1, relwidth=0.25, anchor='w')

frame123 = Frame(root)
frame123.place(relx=0.5, rely=0.85, relheight=0.15, relwidth=1, anchor='s')
satu = Button(frame123, text='1', borderwidth=0, command=lambda: append_number(1))
satu.place(relx=0, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
dua = Button(frame123, text='2', borderwidth=0, command=lambda: append_number(2))
dua.place(relx=0.25, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
tiga = Button(frame123, text='3', borderwidth=0, command=lambda: append_number(3))
tiga.place(relx=0.5, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
plus = Button(frame123, text='+', borderwidth=0, command=Tambah)
plus.place(relx=0.75, rely=0.5, relheight=1, relwidth=0.25, anchor='w')

frame456 = Frame(root)
frame456.place(relx=0.5, rely=0.7, relheight=0.15, relwidth=1, anchor='s')
empat = Button(frame456, text='4', borderwidth=0, command=lambda: append_number(4))
empat.place(relx=0, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
lima = Button(frame456, text='5', borderwidth=0, command=lambda: append_number(5))
lima.place(relx=0.25, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
enam = Button(frame456, text='6', borderwidth=0, command=lambda: append_number(6))
enam.place(relx=0.5, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
minus = Button(frame456, text='-', borderwidth=0, command=Kurang)
minus.place(relx=0.75, rely=0.5, relheight=1, relwidth=0.25, anchor='w')

frame789 = Frame(root)
frame789.place(relx=0.5, rely=0.55, relheight=0.15, relwidth=1, anchor='s')
tujuh = Button(frame789, text='7', borderwidth=0, command=lambda: append_number(7))
tujuh.place(relx=0, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
delapan = Button(frame789, text='8', borderwidth=0, command=lambda: append_number(8))
delapan.place(relx=0.25, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
sembilan = Button(frame789, text='9', borderwidth=0, command=lambda: append_number(9))
sembilan.place(relx=0.5, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
times = Button(frame789, text='x', borderwidth=0, command=Kali)
times.place(relx=0.75, rely=0.5, relheight=1, relwidth=0.25, anchor='w')

framePersen = Frame(root)
framePersen.place(relx=0.5, rely=0.4, relheight=0.15, relwidth=1, anchor='s')
clear_button = Button(framePersen, text='AC', borderwidth=0, command=ClearNumber)
clear_button.place(relx=0, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
backspace = Button(framePersen, text='←', borderwidth=0, command=Backspace)
backspace.place(relx=0.25, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
persen = Button(framePersen, text='%', borderwidth=0, command=Persentase)
persen.place(relx=0.5, rely=0.5, relheight=1, relwidth=0.25, anchor='w')
divide = Button(framePersen, text='/', borderwidth=0, command=Bagi)
divide.place(relx=0.75, rely=0.5, relheight=1, relwidth=0.25, anchor='w')

number = Entry(root, bg='black', borderwidth=0, justify='right', font=numFont, fg='white')
number.place(relx=0.5, rely=0.125, relheight=0.1, relwidth=0.9, anchor='center')
number.insert(0, 0)
number.get()

root.mainloop()
