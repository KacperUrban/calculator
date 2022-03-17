from tkinter import *

root = Tk()
root.title("Kalkulator")

# tworzenie miejsca na wpisanie liczb
e = Entry(root, width=45, borderwidth=6)
# wyświetlanie i umiejscawianie tego miejsca
e.grid(row=0, column=0, columnspan=5, padx=10, pady=20)


def button_click(number):
    # funkcja odpowiadająca za reagowanie na przyciśnięcie odpowiedniego przycisku
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(number))


def button_clear():
    # funkcja czyszcząca wynik
    e.delete(0, END)


def button_add():
    # funkcja odpowiadająca za obsługę przycisku dodawania i przekazywania informacji dalej
    first_number = e.get()
    global fnum
    global name
    name = "add"
    fnum = float(first_number)
    e.delete(0, END)


def button_sub():
    # funkcja odpowiadająca za obsługę przycisku odejmowania i przekazywania informacji dalej
    first_number = e.get()
    global fnum
    global name
    name = "sub"
    fnum = float(first_number)
    e.delete(0, END)


def button_multi():
    # funkcja odpowiadająca za obsługę przycisku mnożenia i przekazywania informacji dalej
    first_number = e.get()
    global fnum
    global name
    name = "multi"
    fnum = float(first_number)
    e.delete(0, END)


def button_divide():
    # funkcja odpowiadająca za obsługę przycisku dodawania i przekazywania informacji dalej
    first_number = e.get()
    global fnum
    global name
    name = "divide"
    fnum = float(first_number)
    e.delete(0, END)


def button_pow():
    # funkcja odpowiadająca za obsługę przycisku potęgowania oraz oblicza wynik potęgowania, aby ułatwic korzystanie
    # z kalkulatora i nie wywoływac znaku równa się
    first_number = e.get()
    global fnum
    global name
    name = "power"
    fnum = float(first_number)
    e.delete(0, END)
    e.insert(0, pow(fnum, 2))


def button_mod():
    # funkcja odpowiadająca za obsługę przycisku obliczania reszty z dzielenia i przekazywania informacji dalej
    first_number = e.get()
    global fnum
    global name
    name = "mod"
    fnum = float(first_number)
    e.delete(0, END)


def button_root():
    # funkcja odpowiadająca za obsługę przycisku pierwiastkujący oraz oblicza pierwiastek liczby, aby ułatwić
    # korzystanie z kalkulatora i nie wywoływac znaku równa się
    first_number = e.get()
    global fnum
    global name
    name = "root"
    fnum = float(first_number)
    e.delete(0, END)
    e.insert(0, pow(fnum, 1 / 2))


def button_equal():
    # Funkcja zbiera informacje od wcześniejszych funkcji i określa co powinna wykonać, a następnie wykonuje
    second_number = e.get()
    e.delete(0, END)
    if name == "add":
        e.insert(0, fnum + float(second_number))
    if name == "sub":
        e.insert(0, fnum - float(second_number))
    if name == "divide":
        e.insert(0, fnum / float(second_number))
    if name == "multi":
        e.insert(0, fnum * float(second_number))
    if name == "mod":
        e.insert(0, fnum % float(second_number))


# tworznie przycisków
# funkcja lambda została użyta, ponieważ bez tego funkcja command nie pozwolila byc funkcji button_click zbierać
# domyślnych liczby z buttonów
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_equal = Button(root, text='=', padx=87, pady=20, command=button_equal)
button_add = Button(root, text='+', padx=38, pady=20, command=button_add)
button_clear = Button(root, text='clear', padx=28, pady=20, command=button_clear)
button_sub = Button(root, text='-', padx=41, pady=20, command=button_sub)
button_multi = Button(root, text='x', padx=40, pady=20, command=button_multi)
button_div = Button(root, text='/', padx=42, pady=20, command=button_divide)
button_mod = Button(root, text='mod', padx=28, pady=20, command=button_mod)
button_pow = Button(root, text='pow', padx=30, pady=20, command=button_pow)
button_root = Button(root, text='sqr', padx=34, pady=20, command=button_root)

# wyświetlanie oraz ustawianie miejsca przycisku
button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)
button_3.grid(row=1, column=3)
button_add.grid(row=1, column=4)
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)
button_sub.grid(row=2, column=4)
button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)
button_9.grid(row=3, column=3)
button_multi.grid(row=3, column=4)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2, columnspan=2)
button_mod.grid(row=5, column=3)
button_div.grid(row=4, column=4)
button_pow.grid(row=5, column=1)
button_clear.grid(row=5, column=2)
button_root.grid(row=5, column=4)

root.mainloop()
