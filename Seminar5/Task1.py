# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

def pvp_mode(player1_candy, player2_candy):
    print('PvP mode!')
    candy = int(input('Введите количество конфет в стопке: '))
    while candy > 0:
        take1_candy = int(input('Первый игрок берет конфет ?: '))
        while take1_candy <= 0 or take1_candy > 28:
            print('Брать можно от 0 до 28 конфет')
            take1_candy = int(input('Первый игрок берет конфет ?: '))
        while take1_candy > candy:
            print('В стопке недостаточно конфет')
            take1_candy = int(input('Первый игрок берет конфет ?: '))
        else:
            if 0 <= take1_candy <= 28:
                player1_candy = player1_candy + take1_candy
                candy = candy - take1_candy
                print(f'У первого игрока {player1_candy}  конфет')
                print(f'Первый игрок победил!!! \n с колличеством: {player1_candy}  конфет')
                print('Игра окончена!')
                return
        take2_candy = int(input('Второй игрок берет конфет ?: '))
        while take2_candy <= 0 or take1_candy > 28:
            print('Брать можно от 0 до 28 конфет')
            take2_candy = int(input('Второй игрок берет конфет ?: '))
            while take2_candy > candy:
                print('В стопке недостаточно конфет')
                take2_candy = int(input('Второй игрок берет конфет ?: '))
            else:
                if 0 <= take2_candy <= 28:
                    player2_candy = take2_candy + player2_candy
                    candy = candy - take2_candy
                    print(f'У второго игрока {player2_candy}  конфет')
                    print(f'Конфет в стопке осталось {candy}')
                    if candy == 0:
                        player2_candy = player2_candy + player1_candy
                        print(f'Второй игрок победил!!! \n с колличеством: {player2_candy}  конфет')
                        print('Игра окончена!')
                        return

def pve_mode(comp_candy, player_candy):
    print('PvE mode!')
    candy = int(input('Введите количество конфет в стопке: '))
    while candy > 0:
        take1_candy = random.randint(0, 29)
        if take1_candy > candy:
            take1_candy = candy
        print(f'Компьютер берет {take1_candy} конфет')
        comp_candy = comp_candy + take1_candy
        candy = candy - take1_candy
        print(f'У Компьютеа {comp_candy} конфет')
        print(f'Конфет в стопке осталось {candy}')
        if candy == 0:
            player_candy = comp_candy + player_candy
            print(f'Компьютер победил!!! \n с колличеством: {player_candy}  конфет')
            print('Игра окончена!')
            return
        take2_candy = int(input('Игрок берет конфет ?: '))
        while take2_candy <= 0 or take2_candy > 28:
            print(f'Брать можно от 0 до 28 конфет')
            take2_candy = int(input('Игрок берет конфет ?: '))
        while take2_candy > candy:
            print('В стопке недостаточно конфет')
            take2_candy = int(input('Игрок берет конфет ?: '))
        else:
            if 0 <= take2_candy <= 28:
                player_candy = take2_candy + player_candy
                candy = candy - take2_candy
                print(f'У игрока {player_candy} конфет')
                print(f'Конфет в стопке осталось {candy}')
                if candy == 0:
                    player_candy = player_candy + comp_candy
                    print(f'Игрок победил!!! \nс колличеством: {player_candy}  конфет')
                    print('Игра окончена!')
                    return

def mode_sel(mode):
    if mode == 1:
        player1_candy = 0
        player1_candy = 0
        pvp_mode(player1_candy, player1_candy)
    elif mode == 2:
        comp_candy = 0
        player_candy = 0
        pve_mode(comp_candy, player_candy)
    else:
        print('Нет такого режимма')

mod = int(input('Введите 1 -против игрока; 2 -против бота: '))
mode_sel(mod)
