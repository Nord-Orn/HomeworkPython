# 3 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import encodings
from itertools import count


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        # Если предыдущий и текущий символ не совпадают
        if char != prev_char:
            # то добавляем посчитанное количество символов и сам символ в расшифровку
            if prev_char:
                encoding += str(count) + prev_char
            count += 1
            prev_char = char
        else:
            # Иначе игнорируем счетчик (если символы совпадают)
            count += 1
    else:
        # Завершение расшифровки
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ' '
    count = ' '
    for char in data:
        # Если символ число
        if char.isdigit():
            # Присоединяем его к счетчику
            count += char
        else:
            # Иначе если символ не число печатаем необходимое количество символов в расшифровку
            decode += char * int(count)
            count =' '
    return decode


decoded_val = rle_decode('zdgz4z4gfvzd4v6z44fsf6sagzdv4zd68')
print(decoded_val)
with open('decode.txt', 'a') as file:
    file.write(f'{decoded_val}\n')