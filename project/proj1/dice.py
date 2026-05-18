"""Functions that simulate dice rolls.

A dice function takes no arguments and returns a number from 1 to n
(inclusive), where n is the number of sides on the dice.

Types of dice:

 -  Dice can be fair, meaning that they produce each possible outcome with equal
    probability. Examples: four_sided, six_sided

 -  For testing functions that use dice, deterministic test dice always cycle
    through a fixed sequence of values that are passed as arguments to the
    make_test_dice function.
"""

from random import randint

def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    # If the number of sides isn't greater than 1, it is illegal!
    # If it's even not a number, then it's INDEED illegal!
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'    
    def dice():
        # Use randint to return random int ranging from 1 to sides.
        return randint(1,sides)
    # We return this function. (So it's a higher-order function!!!)
    return dice

# Just a four sided dice, as we have seen above.
four_sided = make_fair_dice(4)
# Normal six sided dice.
six_sided = make_fair_dice(6)
# If we want to go wild, we can even define a dice that has 1000 sides...

def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice