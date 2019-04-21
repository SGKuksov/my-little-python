'''
Программа-игра. Компьютер загадывает случайное целое число от 1 до 4, пользователь пытается его угадать. Программа запрашивает число ОДИН раз. Если число угадано, то выводим на экран Победа, иначе - Повторите еще раз!
'''
import random

def if_random_game():
    print_str = 'Человек. Мы загадали число от 1 до 4. Угадай, что это за число: '
    comp_num = random.randint(1, 4)
    num = input(print_str)

    if num.isdigit():
        num = int(num)
    else:
        return 'Необходимо ввести число. Повторите еще раз!'

    if comp_num == num:
        return 'Победа'
    else:
        return 'Повторите еще раз!'


print(if_random_game())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
