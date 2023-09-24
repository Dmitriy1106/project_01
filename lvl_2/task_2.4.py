# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

print("Пункт А")
def remove_exclamation_marks(s):
 return s.replace("!", "")
text = "Hi! Hello!!"
clean_text = remove_exclamation_marks(text)
print(clean_text)

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
print("Пункт В")
def remove_last_em(v):
    if v.endswith("!"):
        return v[:-1]
    else:
        return v
text = "!Hi!"
clean_text = remove_last_em(text)
print(clean_text)


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove(# Объединяем слова обратно в предложение) === "!Hi!"
print("Допольнительный пункт С")
# def remove_word_with_one_em(x):
def remove_word_with_one_em(x):
        words = x.split()  # Разделяем предложение на слова
        result = []
        for word in words:
            if word.count('!') == 1: # Проверяем количество восклицательных знаков в слове(не работает как надо)
                continue
            result.append(word)
        return ' '.join(result) # Объединяем слова обратно в предложение
x = "!Hi Hi! Hi!! Hi"
clean_x = remove_word_with_one_em(x)
print("Должно удалять с одним знаком, ! , ... и удаляет же:", clean_x)

# print("Тест")
# def remove_words_with_one_em(sentence):
#     words = sentence.split()
#     result = []
# for word in words:
#     if word.count('!') == 1:
#         continue
#         result.append(word)
#         return ' '.join(result)
# sentence = "Привет! Как дела?! Ты готов!"
# clean_sentence = remove_words_with_one_em(sentence)
# print(clean_sentence)