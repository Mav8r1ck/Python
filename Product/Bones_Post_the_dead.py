#coding=utf-8
import random

# Правила игры

def rules():
    print("Игра в кости: Отложи мертвую\n"
          "Правила игры:\n"
          "Количество участников - двое.\n"
          "В игре используется пять костей. В начале жребий определяет очередность ходов.\n"
          "Игрок бросает одновременно все пять костей. Сумма очков записывается за ним,\n"
          "если ни на одной из пяти костей не выпало двоек или пятерок.\n"
          "Если же выпала хотя бы одна двойка или пятерка, то сумма очков игроку не записывается.\n"
          "Та кость, что показала пятерку или двойку, объявляется мертвой: ее откладывают в сторону.\n"
          "Если таких костей несколько, то в сторону откладываются все.\n"
          "Игру продолжает тот же самый участник. При каждом удачном броске его очки плюсуют к записанным прежде.\n"
          "Он выбрасывает кости до тех пор, пока все пять костей не окажутся в мертвых.\n"
          "В таком случае кости передаются следующему игроку, который продолжает игру по тем же правилам.\n"
          "Выигравшим считается тот, кто наберет больше очков. Удачи!")

# Функция ввода имен игроков

def players_name():
    print("Введите свои имена?:\n")
    name=input()
    return name

# Эмуляция кости

def cube(side=6):
    for i in range(random.randrange(5, 50, 1)):
        number=random.randint(1, side)
    return number

# Игровая партия

def game(players1, players2):
    x = 10
    side1 = 0
    side2 = 0
    while x > 0:
        while x > 0:
            print(players1, "нажмите 1 для броска или 0 для окончания игры")
            x = int(input())
            if x == 1:
                side1 = cube()
                print(side1)
                break
            else:
                print("Введено неверное значение")
        while x > 0:
            print(players2, "нажмите 1 для броска или 0 для окончания игры")
            x = int(input())
            if x == 1:
                side2 = cube()
                print(side2)
                break
            else:
                print("Введено неверное значение")
        if side1 > side2:
            print("Первым бросает", players1)
            score_for_player1 = bone()
            print(players1, ",Вы закончили игру с результатом: ", score_for_player1)
            print("Ваша очередь, ", players2)
            score_for_player2 = bone()
            print(players2, ",Вы закончили игру с результатом: ", score_for_player2)
            if score_for_player1 > score_for_player2:
                print(players1,"! Вы победили, поздравляю!")
                print(players1,"и", players2, "До новых встреч в игре!")
                break
            elif score_for_player2 > score_for_player1:
                print(players2,"! Вы победили, поздравляю!")
                print(players2,"и", players1, "До новых встреч в игре!")
                break
            else:
                print(players2, "и", players1, "Победила дружба!")
                break
        elif side2 > side1:
            print("Первым бросает", players2)
            score_for_player2 = bone()
            print(players2, ",Вы закончили игру с результатом: ", score_for_player2)
            print("Ваша очередь, ", players1)
            score_for_player1 = bone()
            print(players1, ",Вы закончили игру с результатом: ", score_for_player1)
            if score_for_player1 > score_for_player2:
                print(players1,"! Вы победили, поздравляю!")
                print(players1,"и", players2, "До новых встреч в игре!")
                break
            elif score_for_player2 > score_for_player1:
                print(players2,"! Вы победили, поздравляю!")
                print(players2,"и", players1, "До новых встреч в игре!")
                break
            else:
                print(players2, "и", players1, "Победила дружба!")
                break
        else:
            print("У вас выпали одинаковые кости, бросайте еще раз)")
            continue

# Игровая сессия

def bone():
    score = 0
    bones = 5
    while bones > 0:
        score_in_while = 0
        res = []
        print("Нажмите 1 для броска")
        x = int(input())
        if x == 1:
            for i in range(0, bones):
                new_element = int(cube())
                res.append(new_element)
                score_in_while += new_element
                print("Выпали кости со значениями: ", res[i])
            a = res.count(2) + res.count(5)
            if a > 0:
                print("Выпало ", a, "костей со значениями 2 или 5")
                bones -= a
                print("Очки в этой попытке не засчитываются, у вас осталось ", bones, "костей")
                print("Ваш общий счет: ", score)
            else:
                score += score_in_while
                print("Позравляю, удачная попытка!")
                print("Ваш счет в этой попытке: ", score_in_while)
                print("Ваш общий счет: ", score)
        else:
            print("Введено неверное значение")
    return score

def main():
    rules()
    players1=players_name()
    players2=players_name()
    print("Здравствуйте, ", players1,"!")
    print("Здравствуйте, ", players2,"!")
    print("Давайте определим кто будет бросать кости первый...")
    game(players1, players2)

main()
