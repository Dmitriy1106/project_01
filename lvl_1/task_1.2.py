# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
x=my_favorite_songs[1][1]+my_favorite_songs[2][1]+my_favorite_songs[4][1]
print("Пункт А")
print('Три песни звучат '+str(x))
#print(5.28+3.40+4.02)

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
y=my_favorite_songs_dict['New Salvation']+my_favorite_songs_dict['A Sorta Fairytale']+my_favorite_songs_dict['Beautiful Day']
print('Пункт Б')
print('Три песни звучат '+str(y))

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
print('Пункт СА')
from random import sample
rand_song = sample(my_favorite_songs, 3)
print(rand_song)
#print('Пункт СB')
#from random import sample
#rand_song = sample(my_favorite_songs_dict,3)
#print(rand_song)
# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime
print('Пункт Д из списка А')
import datetime
total_time2 = datetime.timedelta()
time_songs2 = [
    str(my_favorite_songs[0][1]),
    str(my_favorite_songs[1][1]),
    str(my_favorite_songs[2][1]),
    str(my_favorite_songs[3][1]),
    str(my_favorite_songs[4][1]),
    str(my_favorite_songs[5][1]),
    str(my_favorite_songs[6][1]),
    str(my_favorite_songs[7][1]),
    str(my_favorite_songs[8][1])
]
for time in time_songs2:
    minutes, seconds = time.split(".")
    minutes, seconds = int(minutes), int(seconds)
    total_time2 += datetime.timedelta(minutes=minutes, seconds=seconds)
sec1 = total_time2.total_seconds()
print(str(sec1) +' секунд' )

#print('Пункт Д на основе B')
#import datetime
#date = y
#for time in time_songs2:
 #   minutes, seconds = time.split(".")
  #  minutes, seconds = int(minutes), int(seconds)
   # total_time2 += datetime.timedelta(minutes=minutes, seconds=seconds)
#print(datetime.datetime.strptime(date, '%M:%S').timestamp())
#import datetime
#total_time2 = datetime.timedelta()
#time_songs2 = str(y)
#(my_favorite_songs['Waste a Moment']),
#(my_favorite_songs['New Salvation']),
#(my_favorite_songs['Staying\' Alive'])
#'Out of Touch': 3.03,
#'A Sorta Fairytale': 5.28,
#'Easy': 4.15,
#'Beautiful Day': 4.04,
#'Nowhere to Run': 2.58,
#'In This World': 4.02,
#for time in time_songs2:
  #  minutes, seconds = time.split(".")
 #   minutes, seconds = int(minutes), int(seconds)
  #  total_time2 += datetime.timedelta(minutes=minutes, seconds=seconds)
#sec1 = total_time2.total_seconds()
#print(str(sec1) +' секунд' )
