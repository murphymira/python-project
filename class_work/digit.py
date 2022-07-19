def get_digit(number, position):
    '''
    return digit at position in number, counting from right

    >>> 3 == 4
    False
    >>> '2' + 3 # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError:

     '''

    return number // (10 ** position) % 10


print(get_digit(234, 2))


