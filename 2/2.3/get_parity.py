def get_parity(num):

    if num % 2 != 0:
        print(False)
        return False
    else:
        print(True)
        return True


get_parity(2)
get_parity(1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
