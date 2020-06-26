def equi(a, b):
    return (not(a) or b) and (a or not(b))


def impl(a, b):
    return (not(a) and b)


def divider(rowlen):
    print(' ' + '-' * (len(rowlen) - 2))


print('task nr. 23\n')

# Описание задачи: постройте таблицу истинности для ¬(¬(A∧B)∨A↔B)∨¬A

firstRow = '| A | B | ¬(¬(A∧B)∨A↔B)∨¬A |'
divider(firstRow)
print(firstRow)

a = False
b = False

print('| {} | {} |         {}        |'.format(int(a), int(b), int(not(not(a and b) or equi(a, b) or not a))))

a = True

print('| {} | {} |         {}        |'.format(int(a), int(b), int(not(not(a and b) or equi(a, b) or not a))))

a = False
b = True

print('| {} | {} |         {}        |'.format(int(a), int(b), int(not(not(a and b) or equi(a, b) or not a))))

a = True

print('| {} | {} |         {}        |'.format(int(a), int(b), int(not(not(a and b) or equi(a, b) or not a))))
divider(firstRow) # divider

print('\ntask nr. 26\n')

# Описание задачи: постройте таблицу истинности для ¬(A∧B)∨(C∧B∧A)→¬(A∧¬C↔B∧C)∧¬A∧C∧B∨A

secondRow = '| A | B | C | ¬(A∧B)∨(C∧B∧A)→¬(A∧¬C↔B∧C)∧¬A∧C∧B∨A |'
divider(secondRow)
print(secondRow)

a = False
b = False
c = False

print('| {} | {} | {} |                   {}                  |'.format(int(a), int(b), int(c), int( impl((not(a and b) or (c and b and a)), (not(equi(a and not c, b) and c) or not(a) and c and b or a)))))

a = True

print('| {} | {} | {} |                   {}                  |'.format(int(a), int(b), int(c), int( impl((not(a and b) or (c and b and a)), (not(equi(a and not c, b) and c) or not(a) and c and b or a)))))

a = False
b = True

print('| {} | {} | {} |                   {}                  |'.format(int(a), int(b), int(c), int( impl((not(a and b) or (c and b and a)), (not(equi(a and not c, b) and c) or not(a) and c and b or a)))))

a = True

print('| {} | {} | {} |                   {}                  |'.format(int(a), int(b), int(c), int( impl((not(a and b) or (c and b and a)), (not(equi(a and not c, b) and c) or not(a) and c and b or a)))))

a = False
b = False
c = True

print('| {} | {} | {} |                   {}                  |'.format(int(a), int(b), int(c), int( impl((not(a and b) or (c and b and a)), (not(equi(a and not c, b) and c) or not(a) and c and b or a)))))

a = True

print('| {} | {} | {} |                   {}                  |'.format(int(a), int(b), int(c), int( impl((not(a and b) or (c and b and a)), (not(equi(a and not c, b) and c) or not(a) and c and b or a)))))

a = False
b = True

print('| {} | {} | {} |                   {}                  |'.format(int(a), int(b), int(c), int( impl((not(a and b) or (c and b and a)), (not(equi(a and not c, b) and c) or not(a) and c and b or a)))))

a = True

print('| {} | {} | {} |                   {}                  |'.format(int(a), int(b), int(c), int( impl((not(a and b) or (c and b and a)), (not(equi(a and not c, b) and c) or not(a) and c and b or a)))))

divider(secondRow)  # divider
