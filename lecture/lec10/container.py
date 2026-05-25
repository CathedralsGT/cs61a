def mysum(L):
    """Takes in a list and compute the sum of its members. Done recursively.
    
    Args:
        L: a list containing numbers.

    >>> mysum([4, 2, 3, 1])
    10
    >>> mysum([])
    0
    """
    if len(L) == 0:
        return 0
    else:
        return L.pop() + mysum(L)
    # or: L[0] + mysum(L[1:])

def reverse_str(str):
    """Takes in a string and reverse it.
    
    >>> reverse_str('draw')
    'ward'
    """
    if len(str) == 1:
        return str
    return reverse_str(str[1:]) + str[0]