def sum_array(array):
    total = 0
    for i in array:
        total += i
    return total
'''Return sum of all items in array'''
result = sum(array)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    """Function to return the factorial
   of a number using recursion"""
    if n == 1:
        return n
    else:
        '''Return n!'''
        return n * factorial(n-1)


def reverse(word):
    if word == "":
        '''Return word in reverse'''
        return word
    else:
        return reverse(word[1:]) + word[0]
