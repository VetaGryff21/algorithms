def take():  #читает поле из файла
    field = open('life.txt', 'r').read().split()
    for i in range(len(field)):
        field[i] = int(field[i])
    n = field[0]
    m = field[1]
    del field[0]
    del field[0]
    given = []
    for i in range(n):
        extention = []
        for j in range(m):
            extention.append(field[i * m + j])
        given.append(extention)
    return given


n = len(take())
m = len(take()[0])


def neighbours(ar, y, x):
    neigh = []
    for i in range(n):
        for j in range(m):
            if i >= 0 and i < n and abs(i - y) <= 1 and j >= 0 and j < m and abs(j - x) <= 1 and (i != y or j != x):
                neigh.append([i, j])
    return neigh


def one_next(ar, y, x):
    q = 0
    for i in neighbours(ar, y, x):
        if ar[i[0]][i[1]] == 1:
            q += 1
    if (q == 3) or (q == 2 and ar[y][x] == 1):
        p = 1
    else:
        p = 0
    return p


def global_next(ar):
    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(one_next(ar, i, j))
        a.append(b)
    return a


def cute_print(ar):
    for i in range(n):
        for j in range(m):
            print(ar[i][j], end='  ')
            if j == m - 1:
                print('\n')
    print('-' * (m + 2 * (m - 1)))


def output(ar, k):
    uni = ar[:]
    for i in range(k):
        if global_next(uni) == uni:
            break
        uni = global_next(uni)
        cute_print(uni)


cute_print(take())
output(take(), int(input()))