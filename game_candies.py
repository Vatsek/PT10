from random import randrange
import time

def input_and_check_the_number_of_candies(message):
    quantity = int(input(message))
    while quantity > 28 or quantity < 1:
        quantity = int(input('Можно взять от 1 до 28 конфет. Введите снова: '))
    return quantity

candies = 2021
id = randrange(0,2)

print('На столе лежит 2021 конфета. Два игрока делают ход друг после друга. Первый ход определяется жеребьёвкой.\
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. ')
time.sleep(1)
print(f'Всего на столе {candies} конфет')
if id == '0':
    print('Игру начинаете Вы')
else: print('Игру начинает компьютер')
time.sleep(1)
while(candies > 0):

    match id:
        case '0':
            quantity = input_and_check_the_number_of_candies('Введите какое количество конфет хотите взять: ')
            candies -= quantity
            print(f'На столе осталось {candies} конфет')
            id = '1'
        case _:
            if candies < 29:
                quantity = candies
            else:
                quantity = randrange(1,29)
            print(f'Компьютер берет {quantity} конфет')
            candies -= quantity
            print(f'На столе осталось {candies} конфет')
            id = '0'
if id == '1':
    print('Ты выиграл))!!')
else: print('Ты проиграл :((')

