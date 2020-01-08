def find(s, i):
    j = i + 1
    print(s[i], s[j], j)

    while '0' <= s[j] <= '9' and j < len(s) - 1:
        j += 1
    print(s[i + 1:j])
    print()



file = open('dataset_3363_2.txt', 'r')
str = file.readline()
#print(s)

list = []
count = -1

for i in range(len(str)):
    if 'a' <= str[i] <= 'z':
        list.append([str[i]])
        count += 1
    elif 'A' <= str[i] <= 'Z':
        list.append([str[i]])
        count += 1
    elif '0' <= str[i] <= '9':
        list[count].append(str[i])

for i in range(len(list)):
    str2 = ''
    for j in list[i][1::]:
        str2 = str2 + j
    print(list[i][0]*int(str2), end='')
print()