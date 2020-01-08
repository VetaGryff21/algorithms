# -*- coding: utf-8 -*-
import numpy as np


# 5x5
# Входные данные (См. условие задачи)
in_matrix = np.array([[1, 2, 5, 7, 9],
                    [5, 2, 7, 3, 6],
                    [7, 7, 8, 7, 7],
                    [6, 21, 6, 2, 8],
                    [0, 2, 1, 6, 0]])


# Жадный алгоритм

def lower_assessment_a(np_matrix: np.array):
    assessment = None
    for i in range(len(np_matrix)):
        worker = np.argmin(np.max(np_matrix, axis=1))
        machine = np.argmax(np_matrix, axis=1)[worker]
        assessment = min(np_matrix[worker][machine], assessment) if assessment is not None else np_matrix[worker][machine]
        np_matrix = np.delete(np_matrix, worker, 0)
        np_matrix = np.delete(np_matrix, machine, 1)
    return assessment


def upper_assessment_a(np_matrix: np.array):
    work_max = np.min(np.max(np_matrix, axis=1))  # Ограничения самый плохой работник не может выдать больше
    machine_max = np.min(np.max(np_matrix, axis=0))  # Ограничения самый плохой машина не может выдать больше
    return min(work_max, machine_max)


 # Жадный алгоритм

def lower_assessment_b(np_matrix: np.array):

    assessment = 0
    for i in range(len(np_matrix)):
        worker = np.argmin(np.min(np_matrix, axis=1))
        machine = np.argmin(np_matrix, axis=1)[worker]
        assessment += np_matrix[worker][machine]
        np_matrix = np.delete(np_matrix, worker, 0)
        np_matrix = np.delete(np_matrix, machine, 1)
    return assessment


def upper_assessment_b(np_matrix: np.array):

    work_max = np.sum(np.max(np_matrix, axis=1))  # Работники не могут выдать больше
    machine_max = np.sum(np.max(np_matrix, axis=0)) # Станки не могут выдать больше
    return min(work_max, machine_max)


def rec_solver_a(in_matrix, point_now):

    global best_lower_assessment_a
    if len(in_matrix) == 1:  # База
        answer = in_matrix[0][0] if point_now is None else min(point_now, in_matrix[0][0])
        if answer > best_lower_assessment_a:
            best_lower_assessment_a = answer
            return

    for i in range(len(in_matrix)):
        for j in range(len(in_matrix[i])):
            temp_point_now = in_matrix[i][j] if point_now is None else min(point_now, in_matrix[i][j])
            temp_matrix = np.delete(in_matrix, i, axis=0)
            temp_matrix = np.delete(temp_matrix, j, axis=1)
            UAA = upper_assessment_a(temp_matrix)
            temp_point_now = min(temp_point_now, UAA)
            if temp_point_now <= best_lower_assessment_a:  # Верхняя оценка не превосходит лучшую
                continue
            rec_solver_a(temp_matrix, temp_point_now)


def rec_solver_b(in_matrix, point_now):
    global best_lower_assessment_b
    if len(in_matrix) == 1:  # База
        answer = in_matrix[0][0] if point_now is None else point_now + in_matrix[0][0]
        if answer > best_lower_assessment_b:
            best_lower_assessment_b = answer
            return

    for i in range(len(in_matrix)):
        for j in range(len(in_matrix[i])):
            temp_point_now = in_matrix[i][j] if point_now is None else point_now + in_matrix[i][j]
            temp_matrix = np.delete(in_matrix, i, axis=0)
            temp_matrix = np.delete(temp_matrix, j, axis=1)
            UAB = upper_assessment_b(temp_matrix)
            if temp_point_now + UAB <= best_lower_assessment_b:  # Верхняя оценка не превосходит лучшую
                continue
            rec_solver_b(temp_matrix, temp_point_now)


issue = "a"

if issue == "a":
    best_lower_assessment_a = lower_assessment_a(in_matrix)
    print(in_matrix)
    rec_solver_a(in_matrix, None)
    print("Лучшая производительность конвеера: ", best_lower_assessment_a)

if issue == "b":
    best_lower_assessment_b = lower_assessment_b(in_matrix)
    rec_solver_b(in_matrix, None)
    print("Лучшая производительности параллельных станков: ", best_lower_assessment_b)