'''
Программа, которая возвращает 
наибольшее из переданных ей из 2х чисел.
'''


def my_max(num1, num2):
    '''
    >>> my_max(10, 5)
    10
    >>> my_max(10, 15)
    15
    '''

    if not (num1.isdigit() and num2.isdigit()):
        return 'Ошибка! Введите число'

    num1 = int(num1)
    num2 = int(num2)

    if num1 > num2:
        return num1

    return num2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
