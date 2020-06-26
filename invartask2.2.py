def f1(a,b,c):
  return f'{int((a or b) and (not c))}'

def f2(a,b,c):
  return f'{int((not((not(c or b) or b) and (a and b)) or b))}'

def f3(a,b,c):
  return f'{int(not(a or not c) or not(b==a))}'

def table():
  print('-' * 60)
  print('|A|B|C|(A||B)&& !C| ((C||B)=>B)&&(A&&B)=>B |A||!C=>!(B<=>A)|')
  print('-' * 60)
  for a in range(2):
    for b in range(2):
      for c in range(2):
        print(f'|{a}|{b}|{c}|     {f1(a,b,c)}     |            {f2(a,b,c)}           |       {f3(a,b,c)}       |')
  print('-' * 60)


table()
