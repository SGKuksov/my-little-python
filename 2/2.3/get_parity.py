'''
проверяющую целое число на четность. 
'''


def get_parity(num):
    '''
    >>> get_parity(2)
    True
    >>> get_parity(1)
    False
    '''

    if not num.isdigit():
        return 'Ошибка! Введите число'

    num = int(num)

    if num % 2 != 0:
        print(False)
        return False
    else:
        print(True)
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
