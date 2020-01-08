# -*- coding: utf-8 -*-
from itertools import *
import copy
n = 4


def get_animal():

    # Функция просит пользователя ввести коров и быков
    print("bulls = ")
    bulls = int(input())
    print("cows = ")
    cows = int(input())
    return bulls, cows


def count_combination(undergame_list):
    # Считает кол-во возможных вариантов решения
    """ undergame_list - массив из массивов с множествами"""
    ret_int = 0
    for group in undergame_list:
        for char_set_one in group[0]:
            for char_set_two in group[1].difference(char_set_one):
                for char_set_three in group[2].difference(char_set_one).difference(char_set_two):
                    ret_int += len(group[3].difference(char_set_one).difference(char_set_two).difference(char_set_three))
    return ret_int


def check_new_perm(old_perm, new_perm):
    # Функция для проверки перемещений коров в новой перестановке
    # Коровы должны поменять свое местоположение
    # Быки должны остаться на месте
    for i in range(n):
        if new_perm[i] == "B" != old_perm[i]:
            return False
        if new_perm[i][0] == "C" and new_perm[i] == old_perm[i]:
            return False
    return True


def differention(group_list, perm, number):

    #  perm - некоторое сочетание из B, C, N формата list
    ret_list = [group_list]
    # print("group list =", group_list)
    c_number = set()
    global n

    for i in range(n):
        if perm[i] == "B":
            for choice_set_now in ret_list:
                if choice_set_now[i].__contains__(number[i]):  # Если это не противоречит правилам
                    choice_set_now[i] = {number[i]}  # Ставим число, которое мы угадали
                else:
                    choice_set_now[i] = set()
                for j in {0,1,2,3}.difference({i}):  # Пробегаемся по всем индексам, кроме угаданного
                    choice_set_now[j].discard(number[i])  # Удаляем угаданный элемент
        if perm[i] == "N":
            for choice_set_now in ret_list:
                for j in {0,1,2,3}:
                    choice_set_now[j].discard(number[i])  # Удаляем угаданный элемент (Иначе было бы B)
        if perm[i][0] == "C":
            for choice_set_now in ret_list:
                choice_set_now[i].discard(number[i])
                c_number.add(number[i])  # Взятие цифр, стоящих на предположительных местах коров

    old_len = len(ret_list)
    perm_set = set(permutations(perm, 4))  # Перебор всех сочетаний из быков и  коров
    for new_perm in perm_set:
        if check_new_perm(perm, new_perm):  # Быки должны остаться на месте, а все коровы поменять место
            for choice_set_now in range(old_len):
                temp_set = [None, None, None, None]
                for i in range(n):
                    if new_perm[i][0] == "C":
                        if ret_list[choice_set_now][i].__contains__(number[perm.index(new_perm[i])]):
                            temp_set[i] = {number[perm.index(new_perm[i])]}
                        else:
                            temp_set[i] = set()
                    else:
                        temp_set[i] = ret_list[choice_set_now][i].difference(c_number).copy()
                ret_list.append(temp_set)
    return ret_list[old_len:]


def all_differention(old_undergame_list, perm_set, number):
    new_undergame_list = []
    for group_list in old_undergame_list:
        for perm in perm_set:
            list_of_group = differention(copy.deepcopy(group_list), perm, number)
            for group in list_of_group:
                if not new_undergame_list.__contains__(group) and not group.__contains__(set()):
                    new_undergame_list.append(group)
    return new_undergame_list


def get_perm_set_from_animal(bulls, cows):
    global n
    ret_list = ["B"] * bulls
    for i in range(1, cows + 1):
        ret_list.append("C" + str(i))
    for i in range(len(ret_list), n):
        ret_list.append("N")
    return set(permutations(ret_list))


def assess_my_choice(undergame_list, number, old_q_combination):
    test_perms = [get_perm_set_from_animal(0, 1),
                  get_perm_set_from_animal(2, 0),
                  get_perm_set_from_animal(2, 2),
                  get_perm_set_from_animal(4, 0)
                  ]
    dels = []
    for test_perm in test_perms:
        test_undergame = all_differention(copy.deepcopy(undergame_list), test_perm, number)
        new_del = count_combination(test_undergame) / old_q_combination
        dels.append(new_del)
    return 1 - max(dels)


def find_my_choice(undergame_list, undergame_number, player_answers, count_numbers):
    global n
    print("Начинаю поиск самого информативного числа")
    if undergame_number == 0:  # Кэш
        return "1234"
    elif undergame_number == 1:
        if player_answers[0] == (0, 2):
            return '6149'
        elif player_answers[0] == (0, 1):
            return '7802'
        elif player_answers[0] == (1, 1):
            return '9724'
        elif player_answers[0] == (1, 0):
            return '9208'
        elif player_answers[0] == (0, 0):
            return '5769'
    if count_numbers == 1:
        for group in undergame_list:
            for one in group[0].copy():
                for two in group[1].difference(one):
                    for three in group[2].difference(one).difference(two):
                        for four in group[3].difference(one).difference(two).difference(three):
                            return one + two + three + four
    old_q_combination = count_combination(game_list[undergame_number])
    max_assess = 0
    max_assess_number = ""
    for group in undergame_list:
        for one in group[0].copy():
            for two in group[1].difference(one):
                for three in group[2].difference(one).difference(two):
                    for four in group[3].difference(one).difference(two).difference(three):
                        assess = assess_my_choice(undergame_list, one+two+three+four, old_q_combination)
                        if assess > max_assess:
                            print("оценка номера", one + two + three + four, " равна:", assess)
                            max_assess = assess
                            max_assess_number = one+two+three+four
    return max_assess_number


full_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
game_list = [[[full_set, full_set.copy(), full_set.copy(), full_set.copy()]]]

undergame_number = 0
player_answers = []
count_numbers = 10000
while 1:
    my_number = find_my_choice(game_list[undergame_number], undergame_number, player_answers, count_numbers)
    print(my_number)
    bulls, cows = get_animal()
    player_answers.append((bulls, cows))
    if bulls == 4:  # Игра окончена
        print("Игра окончена, кол-во угадываний:", undergame_number)
        print("Ваше число: ", my_number)
        exit()
    else:
        perm_set = get_perm_set_from_animal(bulls, cows)
        print("Возможные комбинации:", perm_set)
        game_list.append(all_differention(game_list[undergame_number], perm_set, my_number))
        undergame_number += 1
        for i in game_list[undergame_number]:
            print(i)
        count_numbers = count_combination(game_list[undergame_number])
        print("кол-во возможных комбинаций: ", count_numbers)