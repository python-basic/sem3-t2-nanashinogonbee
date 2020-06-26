import random

abs = lambda x: (x - 2 * x) if x < 0 else x
srclist = [rand(-1000, 1001) for i in range(random.randint(10, 51))]
reslist = [abs(i) for i in srclist]
print('Source list:\n{}\n\nResulting list:\n{}'.format(srclist, leslist))

if __name__ == '__main__':
    assert abs(-5) > 0, 'Error while caculating an absolute value!'

