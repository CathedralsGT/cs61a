HW_SOURCE_FILE=__file__


def num_eights(x):    # passed
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    assert type(x) == int, "You should pass in an integer."
    assert x >= 0, "The integer should not be negative."
    if x < 10:
        return int(x == 8)
    else:
        return int(x%10 == 8) + num_eights(x//10)


# def num_knots(n):    # The helper function for pingpong(n)
#     """Calculate the number of knots exactly before n.
    
#     >>> num_knots(8)
#     0
#     >>> num_knots(15)
#     1
#     >>> num_knots(16)
#     1
#     >>> num_knots(17)
#     2
#     >>> num_knots(18)
#     2
#     >>> num_knots(19)
#     3
#     """
#     if n-1 < 8:
#         return 0
#     else:
#         return int((n-1)%8==0 or num_eights(n-1)) + num_knots(n-1)
# WARNING：Using this kind of implementation would reach a time complexity of O(n^2), which is not the most elegant way!

def pingpong_cond(k):    # Check whether number k is the knot in the pingpong sequence.
    return (k % 8 == 0 or num_eights(k) != 0)
    

def pingpong(n):    # passed
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # if n <= 8: 
    #     return n
    # else:
    #     if num_knots(n) % 2 == 0:
    #         return pingpong(n-1) + 1
    #     else:
    #         return pingpong(n-1) - 1
    assert n>=1, "You should input a strictly positive integer!"
    def pingpong_helper(ppn=1, index=1, sgn=1):
        if index < n:
            if pingpong_cond(index):    # num "index" is a knot
                return pingpong_helper(ppn-sgn, index+1, -sgn)
            else:
                return pingpong_helper(ppn+sgn, index+1, sgn)
        else:
            return ppn
    return pingpong_helper()






def missing_digits(n):    # passed
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        return max(0, (n % 10 - (n//10) % 10 - 1)) + missing_digits(n // 10)


def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
    
def real_count_coins(total, smallest):
    assert smallest == 1 or smallest == 5 or smallest == 10 or smallest == 25, "Invalid choice of coins!"

    if total < 0:
        return 0
    elif total == 0:
        return 1
    else:
        if next_largest_coin(smallest) != None:
            return real_count_coins(total - smallest, smallest) + real_count_coins(total, next_largest_coin(smallest))
        else:
            if total % smallest == 0:
                return 1
            else:
                return 0
    
def prev_largest_coin(coin):
    """Return the previous coin.
    """
    if coin == 25:
        return 10
    if coin == 10:
        return 5
    if coin == 5:
        return 1
    
def new_count_coins(total, biggest):
    assert biggest == 1 or biggest == 5 or biggest == 10 or biggest == 25, "Invalid choice of coins!"

    if total == 0 or biggest == 1:
        return 1
    elif total < 0:
        return 0
    else:
        return new_count_coins(total, prev_largest_coin(biggest)) + new_count_coins(total-biggest, biggest)

def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    # return new_count_coins(total, 25)    # First big then small.
    return real_count_coins(total, 1)    # First small then big.
    



from operator import sub, mul

def make_anonymous_factorial():    # ???
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # return lambda n: 1 if n == 1 else mul(n, make_anonymous_factorial()(sub(n, 1)))
    return (lambda f: f(f))(lambda f: lambda n: 1 if n == 0 else mul(n, f(f)(sub(n, 1))))

