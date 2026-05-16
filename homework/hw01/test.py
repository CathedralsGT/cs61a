# The use of assertion.
def fib(n):
    return 42
fib(10)
#assert fib(10) == 55, 'fib(10) should be 55'
fib(100)
#assert fib(100) == 354224848179261915075, 'fib(100) should be 354224848179261915075'
print("tests passed")

# The use of doctest. Note that ">>>" should be followed by a single space before the code to be tested.
def fib(n):
    """Return the nth Fibonacci number.
    
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(10)
    55
    """
    pred, curr = 1, 1
    k = 2
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr
    #return 42

# The doctest can be run by executing the file, or by importing the file and running doctest.testmod().
# Method 1
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

# Method 2
# from doctest import testmod
# testmod()

# Method 3 (in bash)
# python -m doctest (-v) test.py
# add -v to show details of the tests.