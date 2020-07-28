# Q1: A Plus Abs B
from operator import add, sub

def a_plus_abs_b(a, b):
    if b < 0:
        f = sub(a,b)
    else:
        f = add(a,b)
    return f
