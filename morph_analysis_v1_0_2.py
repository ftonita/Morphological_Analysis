import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from tkinter import font
import sqlite3



def free_input():
    input_text.config(highlightbackground='#BBBBBB')
    input_text.delete(0, END)
    for i in range(number_of_chars):
        char_name[i].grid(row = i + 1 + 5 * (i + 1), column = 3)
        char_name[i].config(highlightbackground = "#777777")
        char_name[i].delete(0, END)
        for j in range(number_of_points[i]):
            char_input[i][j].grid(row = i + 2 + 5 * (i + 1) + j, column = 3)
            char_input[i][j].config(fg='#444444', highlightbackground='#BBBBBB', highlightthickness = 3)
            char_input[i][j].delete(0, END)

def database_update(res_arr, theme, char_title): #Создание/Подключение к БД, создание новой таблицы и сохранение в ней результатов
    try:
        sqlite_connection = sqlite3.connect('morph_analysis.db')
        cursor = sqlite_connection.cursor()
        # print("База данных создана и успешно подключена к SQLite")
        sqlite_create_table_query = """CREATE TABLE """ + theme +"""(
                                id INTEGER,
                                result TEXT NOT NULL);"""
        cursor = sqlite_connection.cursor()
        # print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        # print("Таблица SQLite создана")
        res = (0, str(char_title[0] + '-' + char_title[1]+ '-' + char_title[2]))
        sqlite_insert_query = '''INSERT INTO '''+theme+'''(id, result) VALUES(?, ?)'''
        cnt = cursor.execute(sqlite_insert_query, res)
        sqlite_connection.commit()
        for i in range(len(res_arr)):
            res = (i + 1, res_arr[i])
            sqlite_insert_query = '''INSERT INTO '''+theme+'''(id, result) VALUES(?, ?)'''
            cnt = cursor.execute(sqlite_insert_query, res)
            sqlite_connection.commit()
        # print('Inserted: ', i + 1)
        # print("Результаты занесены в таблицу", theme ,"успешно")
        err = 0
        cursor.close()

    except sqlite3.Error as error:
        # print("Ошибка при подключении к sqlite: ", error)
        err = 1
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")
        return err

def parsing(char, theme, c, char_title): #Парсинг всех комбинаций 
    res_arr = []
    for i in range(c):
        res_arr.append('')
    def func(m, i):
        n = m
        if m != 0:
            count = 0
            while n <= c // number_of_points[0]:
                n += m
                for j in range(number_of_points[i]):
                        for k in range(m):
                            if (i == 0):
                                res_arr[count] = char[i][j]
                            else:
                                res_arr[count] = res_arr[count] + '/' + char[i][j]
                            count += 1
            if (i + 1 < number_of_chars):
                func(m // number_of_points[i + 1], i + 1)
    # print('c = ',c)
    func(c // number_of_points[0], 0)
    return(database_update(res_arr, theme, char_title))

    


def arr_fill(input_text, char_input): #Заполнение листов введенными данными
    char = [[]]
    char_title = []
    c = 1
    for i in range(number_of_chars):
        c *= number_of_points[i]
    for i in range(number_of_chars):
        char.append([])
        char_title.append(char_name[i].get())
        for j in range (number_of_points[i]):
            char[i].append(char_input[i][j].get())
    char.pop()
    c = 1
    for i in range(number_of_chars):
        c *= number_of_points[i]
    theme = input_text.get()
    return(parsing(char, theme, c, char_title))

def check(): #Проверка валидности заполнения полей
    err = 0
    if len(input_text.get()) == 0:
        e_text.config(text = 'Ошибка! Введите тему!', fg = '#990000')
        input_text.config(highlightbackground ='#990000')
    else:
        input_text.config(highlightbackground ='#009900')
        for i in range(number_of_chars):
            if len(char_name[i].get()) == 0:
                char_name[i].config(highlightbackground ='#770000')
                err = 1
            else:
                char_name[i].config(highlightbackground='#007700')
            for j in range(number_of_points[i]):
                if len(char_input[i][j].get()) == 0:
                    char_input[i][j].config(highlightbackground ='#990000')
                    err = 1
                else:
                    char_input[i][j].config(highlightbackground='#009900')

        if err == 1:
            e_text.config(text = 'Ошибка! Заполнены не все характеристики', fg = '#990000')
        else:
            e_text.config(text = 'Данные готовы к анализу', fg = '#009900')
            answer = mb.askyesno(
                title="Сокранение", 
                message="Сохранить результат анализа в базу данных?")
            if answer:
                if arr_fill(input_text, char_input) == 0:
                    mb.showinfo(title = "Успешно", message="База данных успешно дополнена")
                    e_text.config(text = 'База данных успешно дополнена. Вы можете ввожить новые данные!', fg = '#009900')
                    free_input()
                else:
                    mb.showerror(title = "Ошибка", message="При анализе произошла ошибка")
        

def windowInit(): # Инициализация рабочего окна
    master = tk.Tk()
    master.title("Морфологический анализ v1.0.2")
    # master.geometry("500x600")
    master.lift()
    master.config(bg='#BBBBBB', relief='flat', highlightbackground='#000000')
    master.resizable(0, 0)
    global input_text, title
    title = tk.Label(master, text="\tВведите тему:", bg='#BBBBBB')
    input_text = tk.Entry(master, highlightbackground='#BBBBBB')
    title.grid(row = 0)
    input_text.grid(row = 0, column = 1)
    for i in range(number_of_chars):
        char_input.append([])
        char_name.append(tk.Entry(master))

        txt = '\tХарактеристика '+str(i + 1)
        t = tk.Label(master, text = txt)
        t.grid(row = i + 1 + 5 * (i + 1), column = 0)
        t.config(bg='#BBBBBB')
        char_name[i].grid(row = i + 1 + 5 * (i + 1), column = 3)
        char_name[i].config(highlightbackground = "#777777")
        for j in range(number_of_points[i]):
            txt = 'Характеристика '+str(i + 1)+'.'+str(j + 1)+':'
            tt = tk.Label(master, text=txt, bg='#BBBBBB')#
            tt.grid(row = i + 2 + 5 * (i + 1) + j)
            char_input[i].append(tk.Entry(master))
            char_input[i][j].grid(row = i + 2 + 5 * (i + 1) + j, column = 3)
            char_input[i][j].config(fg='#444444', highlightbackground='#BBBBBB', highlightthickness = 3)

    b_enter = tk.Button(master, font=font.Font(family='Arial'), highlightbackground='#BBBBBB', fg ='#AAAAAA' , text = "Enter")
    b_clearall = tk.Button(master, font=font.Font(family='Arial'), highlightbackground='#BBBBBB', fg ='#AAAAAA' , text = "Clear input")
    b_enter.config(command = check)
    b_clearall.config(command = free_input)

    b_enter.grid(row = 25, column = 1)
    b_clearall.grid(row = 25, column = 3)
    global e_text
    e_text = tk.Label(master, text = 'Press Enter', bg = '#BBBBBB', wraplength=180)
    e_text.grid(row = 26, column = 1)
    master.mainloop()

number_of_chars = 3
char_input = [[]]
char_name = []
number_of_points = [5, 5, 5]

if __name__ == '__main__':
    windowInit()