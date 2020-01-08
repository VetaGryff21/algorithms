# -*- coding: utf-8 -*-
import txt_manager
import random
import numpy

quick_compare = 0
quick_change = 0
shell_compare = 0
shell_change = 0


def bubble(A):
    n = 1
    comp_count = 0
    change_count = 0
    while n < len(A):
        for i in range(len(A) - 1):
            comp_count += 1
            if A[i] > A[i + 1]:
                change_count += 3
                A[i], A[i + 1] = A[i + 1], A[i]
        n += 1
    return comp_count, change_count



def bubble_n(A):
    n = 1
    comp_count = 0
    change_count = 0
    while n < len(A):
        for i in range(len(A) - n):
            comp_count += 1
            if A[i] > A[i + 1]:
                change_count += 3
                A[i], A[i + 1] = A[i + 1], A[i]
        n += 1
    return comp_count, change_count, A



def bubble_with_flag(A):
    n = 1
    comp_count = 0
    change_count = 0
    flag = True
    while n < len(A) and flag:
        flag = False
        for i in range(len(A) - n):
            comp_count += 1
            if A[i] > A[i + 1]:
                flag = True
                change_count += 3
                A[i], A[i + 1] = A[i + 1], A[i]
        n += 1
    return comp_count, change_count, A



def shaker(a):

    # lb, ub границы неотсортированной части массива
    k = ub = len(a) - 1
    lb = 1
    comp_count = 0
    change_count = 0
    while lb < ub:
        # проход сверху вниз
        for j in range(ub, lb - 1, -1):
            comp_count += 1
            if a[j - 1] > a[j]:
                change_count += 3
                a[j - 1], a[j] = a[j], a[j - 1]
                k = j
            lb = k
        # проход снизу вверх
        for j in range(lb, ub + 1):
            comp_count += 1
            if a[j - 1] > a[j]:
                change_count += 3
                a[j - 1], a[j] = a[j], a[j - 1]
                k = j
            ub = k
    return comp_count, change_count, a



def shaker_with_flag(a):

    # lb, ub границы неотсортированной части массива
    k = ub = len(a) - 1
    lb = 1
    comp_count = 0
    change_count = 0
    flag = True
    while lb < ub and flag:
        flag = False
        # проход сверху вниз
        for j in range(ub, lb - 1, -1):
            comp_count += 1
            if a[j - 1] > a[j]:
                flag = True
                change_count += 3
                a[j - 1], a[j] = a[j], a[j - 1]
                k = j
            lb = k
        # проход снизу вверх
        for j in range(lb, ub + 1):
            comp_count += 1
            if a[j - 1] > a[j]:
                flag = True
                change_count += 3
                a[j - 1], a[j] = a[j], a[j - 1]
                k = j
            ub = k
    return comp_count, change_count, a


def selection_sort(a):
    comp_count = 0
    change_count = 0
    for i in range(len(a)):
        idxMin = i
        for j in range(i + 1, len(a)):
            comp_count += 1
            if a[j] < a[idxMin]:
                idxMin = j
        change_count += 3
        a[idxMin], a[i] = a[i], a[idxMin]
    return comp_count, change_count, a


def insertion_sort(a):
    comp_count = 0
    change_count = 0
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j - 1] > v) and (j > 0):
            comp_count += 1
            change_count += 1
            a[j] = a[j - 1]
            j = j - 1
        change_count += 1
        a[j] = v
    return comp_count, change_count, a


def quicksort(nums):
    global quick_compare
    global quick_change
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                quick_compare += 1
                quick_change += 1
                s_nums.append(n)
            elif n > q:
                quick_compare += 2
                quick_change += 1
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


def shellsort(a):
    global shell_compare
    global shell_change

    def new_increment(a):
        i = int(len(a) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(numpy.round(i / 2.2))
            yield i

    for increment in new_increment(a):
        for i in range(increment, len(a)):
            for j in range(i, increment - 1, -increment):
                shell_compare += 1
                if a[j - increment] < a[j]:
                    break
                shell_change += 1
                a[j], a[j - increment] = a[j - increment], a[j]
    return a


def merge(left, right):
    """Merge two lists in ascending order."""
    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst


def mergesort(lst):
    """Sort the list by merging O(n * log n)."""
    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = merge(mergesort(lst[:mid]), mergesort(lst[mid:]))
    return lst


A = txt_manager.txt_read_list("1000 five")
for i in range(len(A)):
    A[i] = int(A[i])



print('type of sort            compare  change  list')
print("bubble sort:           ", bubble_n(A.copy()))
print("bubble sort with flag: ", bubble_with_flag(A.copy()))
print("shaker:                ", shaker(A.copy()))
print("shaker with flag:      ", shaker_with_flag(A.copy()))
print("selection:             ", selection_sort(A.copy()))
print("insertion:             ", insertion_sort(A.copy()))
quicksort(A.copy())
print("quick sort:             ", quick_compare, quick_change)
shellsort(A.copy())
print("shell sort:             ", shell_compare, shell_change)