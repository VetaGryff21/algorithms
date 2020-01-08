count = 0
list = []
with open('dataset_3363_4.txt') as file:
    for string in file:
        string = string.strip().split(';')
        print(string)
        for i in string[1::]:
            count += int(i)
        print(count / 3)
        string.append(count / 3)
        print(string)
        list.append(string)

        print(list)
        count = 0

math = 0
phys = 0
rus = 0

for i in list:
    math += int(i[1])
    phys += int(i[2])
    rus += int(i[3])
print(math / len(list), phys / len(list), rus / len(list))