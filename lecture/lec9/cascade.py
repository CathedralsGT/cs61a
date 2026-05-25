def cascade(n):
    """A function that prints the cascade of an integer.
    
    >>> cascade(123)
    123
    12
    1
    12
    123
    """
    assert type(n) == int, "You must input a integer."
    assert n >= 0, "The integer should be greater than or equal to 0."

    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)

def inverse_cascade(n, is_called=False,is_growing=True):
    # 缺点：状态耦合度较高，函数职责不够单一
    """A function that prints the inverse cascade of an integer.
    
    >>> inverse_cascade(123)
    1
    12
    123
    12
    1
    """
    assert type(n) == int, "You must input a integer."
    assert n >= 0, "The integer should be greater than or equal to 0."

    if n < 10:
        print(n)
    else:
        if is_growing == True:
            inverse_cascade(n//10, is_called=True, is_growing=True)
            print(n)
            if is_called == False:
                inverse_cascade(n//10, is_called=True, is_growing=False)
        else:
            print(n)
            inverse_cascade(n//10, is_called=True, is_growing=False)


def better_i_c(n):
    """A better way to use recursion to implement inverse cascade.
    
    >>> better_i_c(123)
    1
    12
    123
    12
    1
    """
    assert type(n) == int and n >= 0, "The input must be a integer greater than or equal to 0."
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)


# An example of tree recursion.
def count_partitions(num, biggest):
    """Returns the number of partition of a positive integer num, using parts up to size(value) biggest, in an increasing order.
    
    >>> count_partitions(3, 2)
    2
    >>> count_partitions(4, 2)
    3
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(2, 2)
    2
    >>> count_partitions(3, 4)
    3
    """
    assert type(num) == int, "You should enter an integer."
    assert num > 0, "The integer should be strictly positive."

    if num == 1 or biggest == 1:
        return 1
    
    if num - biggest > 0:
            return count_partitions(num, biggest-1) + count_partitions(num-biggest, biggest)
    
    return count_partitions(num, min(num, biggest-1)) + int(num - biggest == 0)    # !!
