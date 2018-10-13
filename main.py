import sys

def test(x, y):
    '''
    :param x: one
    :param y: two
    :return:
    '''
    return x+y

print(f'{test.__doc__}\n\n')

string = 'Namespaces are one honking great idea -- let\'s do more of those!'
print(f'\n{sys.version}')
