def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_ = float('inf')
    max_ = float('-inf')
    for v in ints:
        if v < min_:
            min_ = v
        if v > max_:
            max_ = v 
    return (min_, max_)

## Example Test Case of Ten Integers
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# Edge Cases
## Example Test Case of 1000000 Integers, big number edge case
l = [i for i in range(0, 1000001)]  # a list containing 0,...,1000000
random.shuffle(l)

print ("Pass" if ((0,1000000) == get_min_max(l)) else "Fail")

## Example Test Case of 1 Integer, single element edge case
l = [i for i in range(0,1)]  # a list containing 0
random.shuffle(l)
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")