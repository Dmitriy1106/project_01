# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя
arr0 = [4, 6, 2, 1, 9, 63, -134, 566]
arr1=[-52, 56, 30, 29, -54, 0, -110]
arr2=[42, 54, 65, 87, 0]
arr3=[5]
# minimum(arr0)
# minimum(arr1)
# minimum(arr2)
# minimum(arr3)
# maximum(arr0)
# maximum(arr1)
# maximum(arr2)
# maximum(arr3)
# a = input('массив: ')

def maximum(arr1):
 maximum = arr1[0] # Инициализируем maximum первым элементом списка
 for number in arr1:
  if number > maximum:
      maximum= number # Обновляем значение maximum, если находим болшее число
 return maximum
maximum = maximum(arr1)
print("Максимум", maximum)
def minimum(arr1):
 minimum = arr1[0] # Инициализируем minimum первым элементом списка
 for number in arr1:
  if number < minimum:
      minimum = number # Обновляем значение minimum, если находим более малое число
 return minimum
minimum = minimum(arr1)
print("Минимум", minimum)
