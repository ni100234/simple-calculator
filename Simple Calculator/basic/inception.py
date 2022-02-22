#recurtion

from ast import Return


def factorial(n):
    if n==1:
       return 1
    else:
       Return (n * factorial(n-1))