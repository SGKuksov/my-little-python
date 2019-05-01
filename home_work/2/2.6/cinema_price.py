'''
Программа для определения стоимости билетов в кино с учетом скидок.
'''


def cinema_price():
    # Фильм «Пятница», 
    # сеансы: 12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб. 
    # Фильм «Чемпионы», 
    # сеансы: 10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб. 
    # Фильм «Пернатая банда», 
    # сеансы: 10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб. 

    film = input('Выберите фильм: ')
    date = input('Выберите дату (сегодня, завтра): ')
    time = int(input('Выберите время: '))
    qt = int(input('Укажите количество билетов: '))

    film_data = {
        'Пятница': {
            12: 250,
            16: 350,
            20: 450
        },
        'Чемпионы': {
            10: 350,
            13: 350,
            16: 350
        },
        'Пернатая банда': {
            10: 350,
            14: 450,
            18: 450
        },
    }

    # if not film in film_data:

    price = film_data[film][int(time)]

    if date == 'завтра' and qt < 20:
        sale = 0.95

    elif qt >= 20:
        sale = 0.80

    else:
        sale = 1

    total_price = price * sale 

    return f'Стоимость билетов {total_price}'



print(cinema_price())

if __name__ == "__main__":
    import doctest
    doctest.testmod()