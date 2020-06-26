def unique_func(lst):
    '''
        Get one argument which is list - lst.
        Returns new list with unique elements
    '''
    result_lst = []
    for i in lst:
        if i not in result_lst:
            result_lst.append(i)
    return result_lst


print(unique_func([5, 2, 5, 6, 2, 54, 8, 6, 75, 3, 21, 5, 51, 4, 262, 15]))

assert unique_func([1, 2, 2, 2, 8, 4, 6, 6, 7]) == [1, 2, 8, 4, 6, 7], "Ошибка при составлении уникального списка!"
