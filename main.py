from random import randrange

candys = 2021
id = randrange(0,2)
    
print(f'Всего конфет: {candys}')
while(candys > 0):

    match id:
        case '0':
            quantity = int(input('Введите какое количество конфет хотите взять: '))
            candys -= quantity
            print(f'Осталось {candys} конфет')
            id = '1'
        case _:
            if candys < 29:
                quantity = candys
            else:
                quantity = randrange(1,29)
            print(f'Компьютер берет {quantity} конфет')
            candys -= quantity
            print(f'Осталось {candys} конфет')
            id = '0'
if id == '1':
    print('Ты выиграл))!!')
else: print('Ты проиграл :((')