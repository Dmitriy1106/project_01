# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
# Например,
# Введите номер месяца: 3
# Вы ввели март. 31 дней
# Введите номер месяца: 2
# Вы ввели февраль. 28 дней
# Введите номер месяца: 15
# Такого месяца нет!
a = input('Номер месяца: ')
if (a == '1' or a == '3' or a == '5' or a == '7'  or a == '8' or a == '10' or a == '12'):
    print(31)
elif a == '2':
    print('28')
elif (a == '4''6''9''11'):
    print(30)
else:
    print('Это не является номером месяца')




