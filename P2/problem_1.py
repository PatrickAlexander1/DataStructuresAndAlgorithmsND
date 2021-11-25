import math
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    assert(number >= 0)
    assert(type(number) == float or type(number) == int)
    def good_enough(number, guess, eps = 0.01):
        diff = number - guess ** 2
        if diff < 0:
            diff *= -1
        if diff <= eps:
            return True
        else:
            return False

    def sqrt_helper(number, low, high, guesses=0):
        
        guess = (low + high) / 2.0

        if good_enough(number, guess):
            # print(guesses) good for observing the time complexity
            return math.floor(guess + 0.01)
        elif guess ** 2 > number:
            return sqrt_helper(number, low, guess, guesses= guesses + 1)
        else:
            return sqrt_helper(number, guess, high, guesses= guesses + 1)

    return sqrt_helper(number, 0, number)




print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge Cases
# Large input edge case
print ("Pass" if  (1000 == sqrt(1000000)) else "Fail")

# Negative number edge case: assertion error thrown as sqrt only takes values gt or eq to 0
sqrt(-1) # assertion error

# Wrong type edge case: assertion error thrown because input is a string
sqrt('1') # assertion error