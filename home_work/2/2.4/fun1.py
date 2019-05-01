def fun1(x):
    '''
    >>> fun1(-5)
    25
    >>> fun1(0)
    0
    >>> fun1(2)
    2
    >>> fun1(10)
    100
    '''

    if not x.isdigit():
        return 'Ошибка! Введите число'

    x = int(x)

    if x > -2.4 and x <= 5.7:
        return x
    else:
        return x ** 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
