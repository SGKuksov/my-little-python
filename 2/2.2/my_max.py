'''
Программа, которая возвращает 
наибольшее из переданных ей из 2х чисел.
'''

def my_max(num1, num2):
    if num1 > num2:
        return num1
    
    return num2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    

print(my_max(10, 5))
print(my_max(10, 15))
