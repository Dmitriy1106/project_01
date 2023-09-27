# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
import sqlite3
def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection
def close_connection(connection):
    if connection:
        connection.close()
def task2():
    try:
        con =get_connection()
        cursor = con.cursor()
        cursor.execute('SELECT sqlite_version();')
        version = cursor.fetchone()
        print('Вы подключились, версия:', version)
        close_connection(con)
    except(exeption, sqlite3.error) as error:
        print ('Ошибка', error)
task2()
# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# sqlquery = """SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
# FROM Students
# JOIN School ON School.School_Id = Students.School_Id;"""
# cursor.execute(sqlquery)
# connection.commit()
# connection.close()
# print(sqlquery)
print(" ")
print("Домашнее задание 4")
import sqlite3
def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection
def close_connection(connection):
    if connection:
        connection.close()
def task3():
    try:
        con =get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name"
                       " FROM Students JOIN School ON School.School_Id = Students.School_Id;")
        version = cursor.fetchall()
        print(version)
        close_connection(con)
    except(exeption, sqlite3.error) as error:
        print ('Ошибка', error)
task3()