import random
import sys

monster_counter = 0  # счетчик поверженных героем чудовищ
hp = 20  # текущее состояние здоровье героя
attack = 12  # текущая сила удара героя

print("Ну ты и соня! Неужели, не замечаешь этого мерзкого воя?"
      "Скорее, хватай палку и беги, монстры уже рядом!")
print(f"Текущее здоровье: {hp}. Оружие: палка, {attack} единиц урона.")
print()


def fight():  # функция встречи с монстром и выбора действия
    monster_attack = random.randint(1, 20)
    monster_hp = random.randint(10, 50)
    print(f"Отсторожно! Ты встречаешься с монстром! "
          f"Из пасти разит, а дубинка намекает: он здесь не для переговоров. "
          f"Здоровье монстра: {monster_hp}. Сила монстра: {monster_attack}. "
          f"Примешь БОЙ? "
          f"1 - А говорят, рыцарей больше нет... "
          f"2 - я бегу, следовательно, я существую!")
    key_input = input()
    mistake_digit = True
    while mistake_digit:  # бесконечный цикл проверки корректности ввода
        if key_input != '1' and key_input != '2':
            print("Решай скорее, время не ждёт! "
                  "Введи 1, если принимаешь бой или 2, если хочешь сбежать.")
            key_input = input()
        else:
            mistake_digit = False
    if int(key_input) == 1:
        battle(monster_attack, monster_hp)
    elif int(key_input) == 2:
        print("Жизнь дороже славы! Ты бежишь как можно быстрее...")


def battle(monster_attack, monster_hp):  # функция боя с одним монстром, параметры из def fight()
    global attack
    global hp
    global monster_counter
    while hp != 0 and monster_hp > 0:
        while (monster_hp > attack) and (hp > monster_attack):
            hp -= monster_attack  # бой происходит однововременно
            monster_hp -= attack  # здоровье отнимается тоже одновременно
            print(f"Идёт бой! "
                  f"Твоё здоровье: {hp}. Здоровье монстра: {monster_hp}.")
        if monster_attack > hp:
            hp = 0
            print("ПОРАЖЕНИЕ! Попытай удачу в следующий раз.")
            sys.exit(0)
        else:
            hp -= monster_attack
            monster_hp = 0
            monster_counter += 1
            print(f"Монстр побежден, хоть и успел атаковать тебя! "
                  f"Твоё здоровье: {hp}. ")


def apple():
    new_hp = random.randint(1, 11)
    global hp
    hp += new_hp
    print(f"Перед тобой открылся таинственный сад. Ты решаешь восполнить силы и отдохнуть. "
          f"Твоё здоровье повысилось на {new_hp}. Текущее здоровье: {hp}.")


def weapon():
    new_attack = random.randint(1, 50)
    print(f"Холодно. Ты решаешь переждать в заброшенном доме, но тут видишь зачарованный сундук. "
          f"Внутри лежит новый МЕЧ, который наносит {new_attack} урона. Возьмёшь ли ты его? "
          f"1 - конечно, обновка мне не помешает! "
          f"2 - нет уж, спасибо, таким и крысу забороть не получится!")
    key_input = input()
    mistake_digit = True
    while mistake_digit:  # бесконечный цикл проверки корректности ввода
        if key_input != '1' and key_input != '2':
            print("Решай скорее, время не ждёт! "
                  "Введи 1, если хочешь взять оружие или 2, если ты отказываешься.")
            key_input = input()
        else:
            mistake_digit = False
    if int(key_input) == 1:  # текущая сила удара героя заменяется новым значением
        global attack
        attack = new_attack
        print(f"Поздравляю, у тебя теперь новое оружие! Оно наносит {attack} единиц урона.")
    elif int(key_input) == 2:
        print("Ты отказываешь от нового оружия! Надеюсь, последствия не станут плачевными...")


def game():
    while monster_counter < 10:   # т.к. условие проверяется после прохождения одной иттерации, равенство строгое
        location = random.randint(1, 4)
        if location == 1:
            fight()
            print()
        if location == 2:
            apple()
            print()
        if location == 3:
            weapon()
            print()
    print("ПОБЕДА! Тебе удалось сбежать, чтобы умереть в другой раз.")


game()
