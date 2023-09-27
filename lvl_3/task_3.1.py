# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения,
#       * заменять существующие значения,
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание!
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns # Создаем пустую матрицу размером rows x columns
        self.data = [[None for _ in range(columns)]
                     for _ in range(rows)]
    def get_rows(self):
            return self.rows
    def get_columns(self):
            return self.columns
    def set_value(self, row, column, value): # Проверяем, что индексы строки и столбца находятся внутри границ матрицы
         if (0 <= row < self.rows and 0 <= column < self.columns):self.data[row][column] = value
         else:
             print("Ошибка: Неверные индексы строки или 1.")
    def get_value(self, row, column): # Проверяем, что индексы строки и столбца находятся внутри границ матрицы
     if (0 <= row < self.rows and 0 <= column < self.columns):
         return self.data[row][column]
     else:
      print("Ошибка: Неверные индексы строки или столбца 2.")
def print_size(self):
    print("число строк", self.rows)
    print("число столбцов", self.columns)

matrix = Matrix(5, 4) # Создаем матрицу размером 5x4
print("Строк:", matrix.get_rows()) # Вывод: 5
print("Столбцов",matrix.get_columns()) # Вывод: 4

matrix.set_value(0, 0, 1) # Устанавливаем значение 1 в ячейку (0, 0)
matrix.set_value(0, 1, 2) # Устанавливаем значение 3 в ячейку (0, 1)
matrix.set_value(0, 2, 3)
matrix.set_value(0, 3, 4)
matrix.set_value(1, 0, 11)
matrix.set_value(1, 1, 12)
matrix.set_value(1, 2, 13)
matrix.set_value(1, 3, 14)
matrix.set_value(2, 0, 21)
matrix.set_value(2, 1, 22)
matrix.set_value(2, 2, 23)
matrix.set_value(2, 3, 24)
matrix.set_value(3, 0, 31)
matrix.set_value(3, 1, 32)
matrix.set_value(3, 2, 33)
matrix.set_value(3, 3, 34)
matrix.set_value(4, 0, 41)
matrix.set_value(4, 1, 42)
matrix.set_value(4, 2, 43)
matrix.set_value(4, 3, 44)
print(matrix.get_value(0, 0))
print(matrix.get_value(0, 1))
print(matrix.get_value(0, 2))
print(matrix.get_value(0, 3))
print(matrix.get_value(1, 0))
print(matrix.get_value(1, 1))
print(matrix.get_value(1, 2))
print(matrix.get_value(1, 3))
print(matrix.get_value(2, 0))
print(matrix.get_value(2, 1))
print(matrix.get_value(2, 2))
print(matrix.get_value(2, 3))
print(matrix.get_value(3, 0))
print(matrix.get_value(3, 1))
print(matrix.get_value(3, 2))
print(matrix.get_value(3, 3))
print(matrix.get_value(4, 0))
print(matrix.get_value(4, 1))
print(matrix.get_value(4, 2))
print(matrix.get_value(4, 3))


