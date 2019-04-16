'''
программа по коду города 
и длительности переговоров вычисляет 
их стоимость и результат выводит на экран
'''


def call_tel(code, time):
    # Екатеринбург-код 343, 15 руб/мин
    # Омск-код 381, 18 руб/мин
    # Воронеж-код 473, 13 руб/мин
    # Ярославль-код 485, 11 руб/мин
    '''
    >>> call_tel(343, 10)
    150
    '''

    if time.isdigit() and code.isdigit():
        time = int(time)
        code = int(code)
        result = 0

        if time <= 0:
            return print('Длительность переговоров не может быть меньше 0')
    else:
        return print('Длительность переговоров не может быть строкой')

    if code == 343:
        result = time * 15
    elif code == 381:
        result = time * 18
    elif code == 473:
        result = time * 13
    elif code == 485:
        result = time * 11
    else:
        return print('Код города введен неверно')

    return print(result)


inp_code = input('Введите код города: ')
inp_time = input('Введите длительность переговоров: ')

call_tel(inp_code, inp_time)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
