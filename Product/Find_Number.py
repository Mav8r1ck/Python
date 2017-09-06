#Game 'Find_number'
from random import *
#import random
true = "Y"
print("Играем?(Да(Y)")
x = str(input())
while str(true) == x:
        print("Загадано число от 100 до 1000, угадай его!)")
        i = 0
        Score = 0
        x = randrange(100, 1000, 1)
        while i != x:
            i = int(input())

# Проверка диапазона значений

            while i < 100 or i > 1000:
                print("Введенное число находится за диапазоном значений\n! Повторите ввод")
                i = int(input())

# Нахождение числа

            if i < x:
                print("Искомое число больше введенного!")
                Score += 1
            elif i > x:
                print("Искомое число меньше введенного!")
                Score += 1
            else:
                print("Вы угадали число!", x)
                print("Ваше количество попыток: ", Score)

