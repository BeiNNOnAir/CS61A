# Q2: Two of Three
# Write a function that takes three positive numbers and returns the sum of the squares of the two largest numbers.
# Use only a single line for the body of the function.

def two_of_three(a, b, c):
    x,y = max(a,b),max(b,c)
    return x*x + y*y

"""Return x*x + y*y, where x and y are the two largest members of the
positive numbers a, b, and c.

>>> two_of_three(1, 2, 3)
13
>>> two_of_three(5, 3, 1)
34
>>> two_of_three(10, 2, 8)
164
>>> two_of_three(5, 5, 5)
50
"""
