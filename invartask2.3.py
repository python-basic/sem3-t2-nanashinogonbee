def fib_gen(n):
    '''Generates a sequence of n Fibonacci elements.'''
    start = 2
    lst = [0, 1]
    for i in range(start, n - start + 2):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst

def slice(elem, first, last, step=1):
    return elem[first:last:step]

lst = fib_gen(22)

print('Сумма четных элементов (со второго по предпоследний элемент) списка.')
sum = 0
for i in range(1, len(lst) - 1):
    if not lst[i] % 2:
        sum += lst[i]
print(f'{sum}')

print('\nСумма нечетных элементов (с пятого по предпредпоследний элемент) списка.')
sum = 0
for i in range(4, len(lst) - 2):
    if lst[i] % 2:
        sum += lst[i]
print(f'{sum}')

print('\nСумма элементов, расположенных на четных позициях, 1ой половины списка.')
sum = 0
newlst = slice(lst, 0, len(lst) // 2, 2)
for i in newlst:
    sum += i
print(f'{sum}')

print('\nСумма элементов, расположенных на нечетных позициях, 2ой половины списка.')
sum = 0
newlst = slice(lst, len(lst) // 2 - 1, len(lst), 2)
for i in newlst:
    sum += i
print(f'{sum}')

print('\nМакс. элемент, стоящий на четн. позиции среди элементов 2ой половины списка.')
print(f'{max(slice(lst, len(lst) // 2, len(lst), 2))}')

print('\nМин. элемент, стоящий на неч. позиции среди элементов 1ой половины списка.')
print(f'{min(slice(lst, 1, len(lst) // 2, 2))}')

print('''
Список элементов, стоящих на четн. позициях
во 2ой половине списка в обратном порядке.''')
print(f'{slice(lst, len(lst), len(lst) // 2, -2)}')

