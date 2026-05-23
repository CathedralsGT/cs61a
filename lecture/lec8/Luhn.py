def split(n):
    """Take in a number and split it by the last digit.

    >>> split(12345)
    (1234, 5)
    """
    assert type(n) == int, "The input has to be an integer."
    return n // 10, n % 10
    
def sum_digits(m):
    """Return the sum of all digits of m.
    
    >>> sum_digits(12345)
    15
    >>> sum_digits(13579)
    25
    """
    assert type(m) == int, "The input has to be an integer."
    if m < 10:
        return m
    else:
        m_split, last = split(m)
        return sum_digits(m_split) + last
        
def new_sum_digits(m):
    """Compute the sum of all digits of m by recursion.
    
    >>> new_sum_digits(12345)
    15
    """
    assert type(m) == int, "The input has to be an integer."
    result = 0
    while m != 0:
        result, m = result + m % 10, m // 10
    return result
        
#sum_digits(123456789)
#new_sum_digits(123456789)

# Compute the Luhn sum of the credit card number iteratively.
def Luhn(m):
    """Takes in a credit card number and checks if it's valid
    
    -m: The card number a user entered
    """
    assert type(m) == int, "The input has to be an integer."
    result, i = 0, 1
    while m != 0:
        if i % 2 == 1:
            result, m = result + m % 10, m // 10
            i = i + 1
        else:
            curr, m = 2*(m % 10), m // 10
            if curr > 9:
                result = result + new_sum_digits(curr)
            else:
                result = result + curr
            i = i + 1
    return result
                
#Luhn(138743)
# Compute by mutual recursion.
def recursive_Luhn(m):
    assert type(m) == int, "The input has to be an integer."
    if m < 10:
        return m
    else:
        all_but_last, last_digit = split(m)
        return last_digit + recursive_Luhn_double(all_but_last)
        
def recursive_Luhn_double(m):
    assert type(m) == int, "The input has to be an integer."
    if m < 10:
        return m
    else:
        all_but_last, last_digit = split(m)
        luhn_digit = 2 * last_digit
        if luhn_digit > 9:
            return new_sum_digits(luhn_digit) + recursive_Luhn(all_but_last)
        else:
            return luhn_digit + recursive_Luhn(all_but_last)
            
#recursive_Luhn(138743)

# Compute by strict recursion
def Luhn_pro(m, is_odd=True):
    """Check if the card number is valid by using recursion.
    
    Args:
        m: the card number user enters
        is_odd: a T/F flag which indicates whether the last digit
            is in the odd-th place of the original number
    """
    assert type(m) == int, "The input has to be an integer."
    if is_odd:
        if m < 10:
            return m
        else:
            m, last_digit = split(m)
            return last_digit + Luhn_pro(m, not is_odd)
    else:
        if m < 10:
            return new_sum_digits(2*m)
        else:
            m, last_digit = split(m)
            luhn_digit = new_sum_digits(2*last_digit)
            return luhn_digit + Luhn_pro(m, not is_odd)
    
Luhn_pro(138743)
        
    