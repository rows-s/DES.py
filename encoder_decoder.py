def GetKeys( word : str ):
    # Функция преобразовывает ключевое слово в массив цифр, необходимый для определения маски смещения. Принимает str возращает list
    word = list(word.upper())
    sort = sorted(word)
    ch = 0
    for symbol in sort:
        i = word.index(symbol)
        word[i] = ch
        ch += 1
    return word

with open('text_to_encod.txt') as file:
    text = file.read()
# Вызов функции преобразования ключ-слова.
key_word = input('Input your key-word: ')
keys = GetKeys(key_word)
# Замена пробелов на нижнее подчеркивание для улучшения читабельности для немоноширных шрифтов при условии нескольких подряд идущих пробелов.
text.replace(' ', '_')
print('\nKEYS:', keys)
print('\nENTERED TEXT:', text)
print('    BITES:',  ' '.join(format(ord(x), 'b') for x in text) )

# Длинны текста и ключ-слова выделенны в отдельную переменную потому что они будут часто встречатся
len_text = len(text)
len_key = len(key_word)

# Дополнение нижнеми подчеркиваниями нехватающим количеством текста до длины кратной длине ключ-слова
if len_text % len_key:
    dif = len_key - (len_text % len_key)
    tmp = '_'*dif
    text += tmp
    len_text += dif

# encod_word будет увеличеватся постепенно, т.к. кодировка/декодировка идет по блочно, где размер блока равен длине ключ-слова
encod_word = ''
# tmp представляет собой список, т.к. строки в Python не предусматривают редактирование.
# tmp заполняет генератором списков, с длиной равной длине ключ-слова.
# tmp будет использоватся для временного хранения результата кодирование/декодирования.
tmp = [None for _ in range(len_key)]
# Цикл кодирования, одна итерация цикла - один блок. range создает итерируемый объект с шагом в длину ключ-слова.
for part in range(0, len_text, len_key):
    # Выделение блока из текта
    proc_text = text[part : part + len_key]
    # Цикл применят маску смещению.
    for i in range(len_key):
        tmp[keys[i]] = proc_text[i]
    # преобразование списка в строку методом join
    encod_word += ''.join(tmp)
print(encod_word)

# Вывод закодированного текста и его представления в битах
with open('encoded.txt', 'w') as file:
    file.write('TEXT: ' + encod_word)
    file.write('\nBITES: ' + ' '.join(format(ord(x), 'b') for x in encod_word) )
# decod_word аналогично encod_word
decod_word = ''
# Цикл декодирования аналогично кодированию
for part in range(0, len_text, len_key):
    proc_text = encod_word[part : part + len_key]

    for i in range(len_key):
        tmp[i] = proc_text[keys[i]]
    decod_word += ''.join(tmp)
print(decod_word)
# Вывод декодированного текста и его представления в битах
with open('decoded.txt', 'w') as file:
    file.write('TEXT: ' + decod_word)
    file.write('\nBITES: ' + ' '.join(format(ord(x), 'b') for x in decod_word) )