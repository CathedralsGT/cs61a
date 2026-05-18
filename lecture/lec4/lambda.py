square = lambda x: x * x
cube = lambda x: x * x * x

def sum(n, term):
    '''Return the sum of the first n terms in the sequence defined by term.
    n -- a positive integer
    term -- a function that takes one argument
    >>> sum(5, cube)
    225
    '''
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

print(square(15))

