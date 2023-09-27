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
arr0=[4, 6, 2, 1, 9, 63, -134, 566]
arr1=[-52, 56, 30, 29, -54, 0, -110]
arr2=[42, 54, 65, 87, 0]
arr3=[5]

def maximum(arr0):
 maximum = arr0[0] # Инициализируем maximum первым элементом списка
 for number in arr0:
  if number > maximum:
      maximum= number # Обновляем значение maximum, если находим болшее число
 return maximum
maximum = maximum(arr0)
# print("Максимум", maximum)

def minimum(arr0):
 minimum = arr0[0] # Инициализируем minimum первым элементом списка
 for number in arr0:
  if number < minimum:
      minimum = number # Обновляем значение minimum, если находим более малое число
 return minimum
minimum = minimum(arr0)
# print("Минимум", minimum)

print(arr0, "-> max", maximum," min", minimum, )
def maximum(arr1):
 maximum = arr1[0] # Инициализируем maximum первым элементом списка
 for number in arr1:
  if number > maximum:
      maximum= number # Обновляем значение maximum, если находим болшее число
 return maximum
maximum = maximum(arr1)
# print("Максимум", maximum)

def minimum(arr1):
 minimum = arr1[0] # Инициализируем minimum первым элементом списка
 for number in arr1:
  if number < minimum:
      minimum = number # Обновляем значение minimum, если находим более малое число
 return minimum
minimum = minimum(arr1)
# print("Минимум", minimum)

print(arr1, "-> max", maximum," min", minimum, )
def maximum(arr2):
 maximum = arr2[0] # Инициализируем maximum первым элементом списка
 for number in arr2:
  if number > maximum:
      maximum= number # Обновляем значение maximum, если находим болшее число
 return maximum
maximum = maximum(arr2)
# print("Максимум", maximum)

def minimum(arr2):
 minimum = arr2[0] # Инициализируем minimum первым элементом списка
 for number in arr2:
  if number < minimum:
      minimum = number # Обновляем значение minimum, если находим более малое число
 return minimum
minimum = minimum(arr2)
# print("Минимум", minimum)

print(arr2, "-> max", maximum," min", minimum, )
def maximum(arr3):
 maximum = arr3[0] # Инициализируем maximum первым элементом списка
 for number in arr3:
  if number > maximum:
      maximum= number # Обновляем значение maximum, если находим болшее число
 return maximum
maximum = maximum(arr3)
# print("Максимум", maximum)

def minimum(arr3):
 minimum = arr3[0] # Инициализируем minimum первым элементом списка
 for number in arr3:
  if number < minimum:
      minimum = number # Обновляем значение minimum, если находим более малое число
 return minimum
minimum = minimum(arr3)
# print("Минимум", minimum)

print(arr3, "-> max", maximum," min", minimum, )

print(" ")
print("По занятию, циклами")
arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]
def vibor(lst):
    n=len(lst)
    i=0
    while i <n-1:
        m=i
        j=i+1
        while j<n:
            if lst[j]<lst[m]:
                m=j
            j+=1
        lst[i],lst[m]=lst[m],lst[i]
        i+=1
    return lst

def maximum(arr):
    print("МАКСИМУМ")
    print('Сортировка выбором')
    # start_time = datetime.now()
    for lst in arr:
        print('максимальное значение из списка', lst,vibor(lst)[-1])
    # end_time = datetime.now()
    # print('Продолжительность: {}'.format(end_time-start_time))

def minimum(arr):
    print("МИНИМУМ")
    print('Сортировка выбором')
    # start_time = datetime.now()
    for lst in arr:
        print('минимальное значение из списка', lst,vibor(lst)[0])
    # end_time = datetime.now()
    # print('Продолжительность: {}'.format( end_time - start_time ))
def main():
    print(maximum(arr))
    print(minimum(arr))
main()