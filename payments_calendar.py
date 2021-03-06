# -*- coding: utf-8 -*-
import datetime
from datetime import date
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox

# Функция для подчета количества дней которые интернет будет работать

def days_calculate(pay_sum, tarif):
    # Получаем текущую дату
    current_date = datetime.date.today()
    # Получаем результат ввода, берем модуль числа
    try:
        pay_sum = abs(int(pay_sum.get()))
        tarif = abs(int(tarif.get()))
    except Exception as ex:
        messagebox.showerror('Ошибка', 'Введены некорректные данные')
        last_day = 'Ошибка данных'
        lbl_last_day['text'] = last_day
        return last_day
    # Вычисляем количество дней, которые интернет будет работать
    try:
        days = pay_sum // tarif
    except ZeroDivisionError as exception_zero:
        messagebox.showerror('Ошибка', 'На 0 делить нельзя')
        last_day = 'Ошибка вычисления'
        lbl_last_day['text'] = last_day
        return last_day
    # Вычисляем дату когда интернет отключится
    inet_end = datetime.timedelta(days=days)
    last_day = 'Интернет закончится: '+str(current_date+inet_end)
    # Присваиваем дату label для вывода даты
    lbl_last_day['text'] = last_day
    # Присвиваем количество дней label для вывода количеества дн
    lbl_days['text'] = 'Интернет будет работать: '+str(days)+ ' дней(дня)'
    return last_day

# Конфигурация окна
window = Tk()
window.geometry('400x250')
window.title("Калькулятор дней")

# Label для поля Сумма платежа
lbl_pay_sum = Label(window, text="Введите сумму платежа: ")
lbl_pay_sum.pack()
# Поле для ввода суммы платежа
pay_sum = Entry(window, width=15)
pay_sum.pack()

# Label для поля Тариф
lbl_tarif = Label(window, text="Введите сумму списания за день: ")
lbl_tarif.pack()
# Поле для ввода суммы списания за сутки
tarif = Entry(window, width=15)
tarif.pack()

# Кнопка для подсчета количества дней
btn_calculate = Button(window, text='Подсчитать дни', width=15, command=lambda:days_calculate(pay_sum,tarif))
btn_calculate.pack()

# Label для вывода даты в котороую интернет не будет работать
lbl_last_day = Label(window, text="",font=("Arial Bold", 15))
lbl_last_day.pack()
# Label для вывода количества дней, которые интернет будет работать
lbl_days = Label(window, text="",font=("Arial Bold", 15))
lbl_days.pack()

window.mainloop()



