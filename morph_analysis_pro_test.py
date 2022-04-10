number_of_chars = int(input('Введите количество характеристик: '))
char = [[]]
number_of_points = []
for i in range(number_of_chars):
    print('Характеристика', i + 1,':')
    char.append([])
    number_of_points.append(int(input('Введите количество пунктов характеристики '+str(i + 1)+': ')))
    for j in range (number_of_points[i]):
        char[i].append(input('Введите пункт '+str(j + 1)+': '))
    print('+ --------+ --------+ --------+ --------')
char.pop()
c = 1
for i in range(number_of_chars):
    c *= number_of_points[i]
print('Всего', c, 'вариантов')

print('_________________')

# m = c
s = []
for i in range(c):
    s.append(str(i + 1) + ':')
def func(m, i):
    n = m
    if m != 0:
        count = 0
        while n <= c // number_of_points[0]:
            n += m
            for j in range(number_of_points[i]):
                    for k in range(m):
                        s[count] = s[count] + '/' + char[i][j]
                        count += 1
        print('~~~')
        if (i + 1 < number_of_chars):
            func(m // number_of_points[i + 1], i + 1)

func(c // number_of_points[0], 0)

print(s)