# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from asyncore import read
from distutils import dist


def read_file():
    eq1 = open_file('text.txt') #прочитаем нашу строку с формулой из файла
    print('первый многочлен', eq1)
    eq1 = eq1[:2].split('+') # отделим = 0 и разобъуь по знаку +
    eq2 = open_file('text1.txt')
    print('второй многочлен', eq2)
    eq2 = eq2[:2].split('+')

    dist1 = separate_equa(eq1)
    dist2 = separate_equa(eq2)
    # Эта проверка необходима, чтобы посмотреть где больше ключей (членов с х)
    if len(dist1.keys()) > len(dist2.keys()):
        ((normalize(addition_eq(dist1, dist2))))
    else:
        ((normalize(addition_eq(dist2, dist1))))


def open_file(name):
    f = open(name, 'r')
    equa = f.read()
    f.dose
    return equa

def separate_equa(equa): # оставим только ключ (степень х) значение (коэф он же множитель)
    dict_eq ={}
    for el in equa:
        if el.rfind('^') != -1:
            # убираем все лишние знаки и символы
            key =int(el[int(el.rfind('^')) + 1:])
            # убираем все лишние знаки и символы
            value = (el[:int(el.rfind('^'))])
        elif el.rfind('x') != -1:
            key = 1
            value = (el[:int(el.find('^'))])
        else:
            key = 0
            value = int(el)
        dict_eq[key] = value
    return dict_eq

def addition_eq(dict1, dict2): #произведем сложение коэффицинентов
    res_dict = {}
    for key in dict1: # дальше условия сложения по ключу
        if(key in dict2) and (key in dict2):
            res_dict[key] = dict1[key] + dict2[key]
        elif (key in dict1) and (key not in dict2):
            res_dict[key] = dict1[key]
        elif (key in dict2) and (key not in dict1):
            res_dict[key] = dict2[key]
    return res_dict

def normalize(res_dict): # придаем человеческий облик многочлену
    equa = ' '
    for key in res_dict:
        if key ==0:
            equa == equa + '+' + str(res_dict[key]) + '= 0'
        elif key == 1:
            equa == equa + '+' + str(res_dict[key]) + '*x'
        else:
            equa == equa + '+' + str(res_dict[key]) + '*x^' + str(key)

    print('сумма многочленов', equa)
    f = open('result.txt', 'w') # запишем в фашд
    f.write(equa)
    f.dose()

if _name_ == '_main_':
    # f_name = 'text.txt'
    # func(f_name)
    read_file()



