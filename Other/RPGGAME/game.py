from random import randint
import os

class Player():
    hp = 15
    max_hp = 15
    pw = 5
    level = 0
    sp = 5  #skill points
    xp = 0
    max_xp = 100    # To gain next level (max xp will multiply by 5)
    heal_hp = 5
    live = True

def menu_upgrade(p):
    while p.sp > 0:
        print("Выбери своё улучшение! Очки навыка: {}".format(p.sp))
        print("---")
        print("1. ХП {}/{}".format(p.hp, p.max_hp))
        print("2. Сила {}".format(p.pw))
        print("3. Хилл {}".format(p.heal_hp)) # Heal
        n = input("Число: ")
        if n == "1":
            p.hp += 5
            p.sp -= 1
            p.max_hp += 5
        if n == "2":
            p.pw += 1
            p.sp -= 1
        if n == "3":
            p.heal_hp += 1
            p.sp -= 1


def menu_stats(p):
    print("Характеристики игрока!")
    print("---")
    print("ХП: {}/{}".format(p.hp, p.max_hp))
    print("Сила {}".format(p.pw))
    print("Исцеление {}".format(p.heal_hp))
    input("Нажмите чтобы продолжить. ")


def menu_simple(p):
    while p.live:
        print("Выбери что делать")
        print("1. Вступить в битву!")
        print("2. Посмотреть характеристики!")
        print("3. Улучшения!")
        n = input("Число: ")
        if n == "1":
            menu_fight(p)
        if n == "2":
            menu_stats(p)
        if n == "3":
            menu_upgrade(p)

def menu_fight(p):
    ehp = 5 * randint(4, 20)
    epw = 2 * randint(1, 5)
    while ehp > 0:
        print("Враг: {} Сила: {}".format(ehp, epw))
        print("Ты: {}/{} Сила: {}".format(p.hp, p.max_hp, p.pw))
        print("---")
        print("1. Ударь с силой {}".format(p.pw))
        print("2. Исцелится (+{})".format(p.heal_hp))
        print("3. Бежать!")
        n = input("Число: ")
        if n == "1":
            r = randint(1, 2)
            if r == 1:
                ehp -= p.pw
                print("Ты ударил врага!")
            if r == 2:
                p.hp -= epw
                print("Враг ударил тебя!")
                if p.hp < 0:
                    print("Ты проиграл!")
                    p.live = False
                    return p.live
            if ehp <= 0:
                print("Ты убил врага")
                p.xp += randint(5, 20)# random xp
                if p.xp >= p.max_xp:
                    print("LVL_UP")
                    p.sp += 1
                    p.xp -= p.max_xp
                    p.level += 1
        if n == "2":
            p.hp += p.heal_hp
            if p.hp > p.max_hp:
                p.hp = p.max_hp
            print("Исцеление... {}".format(p.hp))
        if n == "3":
            r = randint(1, 3)
            if r == 3:
                print("Ты убежал!")
                return 1
            else:
                print("Ты не можешь убежать!")

game_p = True
p = Player()
menu_simple(p)

print("GG")


















































