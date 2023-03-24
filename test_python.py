"""
тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot
"""
import math
from math import pi, sqrt, pow, hypot

# функция, которая фильтрует нечетные числа
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

def test_filter():
    assert list(filter(filter_odd_num, [1, 2, 4, 5, 7, 8, 10, 11])) == [2, 4, 8, 10]

def square(number):
    return number ** 2

def test_square():
    assert list(map(square, [1, 2, 3, 4, 5]))==[1, 4, 9, 16, 25]

def test_sorted():
    assert list(sorted(['one', 'two', 'list', '', 'dict']))== ['', 'dict', 'list', 'one', 'two']

def test_pi():
    assert round(math.pi,2) == 3.14

def test_sqrt():
    assert sqrt(4) == 2

def test_pow():
    assert pow(3,2) == 9

def test_hypot():
    assert hypot(3, 4) == 5