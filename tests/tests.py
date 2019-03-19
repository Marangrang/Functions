def sum_array():
    """
    make sure sum array works correctly
    """

    print(sum_array([8, 3, 2, 7])) == 20, 'correct'
    print(sum_array([10, 1, 12, 9, 2])) == 34, 'correct'
    print(sum_array([1, 2, 3, 4, 5])) == 15, 'correct'


def fibonacci():
    """
    make sure fibonacci works correctly
    """

    print (fibonacci(int(input(9)))) == 34, 'correct'
    print (fibonacci(int(input(23)))) == 28657, 'correct'
    print (fibonacci(int(input(6)))) == 8, 'correct'


def factorial():
    """
    make sure factorial works correctly
    """

    print (factorial(int(input(7)))) == 5040, 'correct'
    print (factorial(int(input(3)))) == 6, 'correct'
    print (factorial(int(input(6)))) == 720, 'correct'


def reverse():
"""
make sure reverse works correctly
"""

print (reverse(str(input(hello)))) == olleh, 'correct'
print (reverse(str(input(Marang)))) == gnaram, 'correct'
print (reverse(str(input(busy day ?)))) == ? yad ysub, 'correct'


def bubble_sort():
"""
make sure bubble bubble_sort works correctly
"""

items = [1, 3, 78, 15, 9, 23]
bubble_sort(items)
print(items) == [1, 3, 9, 15, 23, 78], 'correct'


def merge_sort(items):
"""
make sure merge_sort works correctly
"""

items = [12, 11, 13, 5, 6, 7]
merge_sort(items)
print(items) == [5, 6, 7, 11, 12, 13], 'correct'


def quick_sort(items):
"""
make sure quick_sort works correctly
"""

items = [12, 4, 5, 6, 7, 3, 1, 15]
merge_sort(items)
print(items) == [1, 3, 4, 5, 6, 7, 12, 15], 'correct'
