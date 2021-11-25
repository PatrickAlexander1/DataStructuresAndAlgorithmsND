def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    # Credit given to the jupyter notebook in the Nanodegree materials for showing
    # how to inplace sort the input list in len(input_list) steps

    n = len(input_list)
    twos_index = n - 1
    zeros_index = 0
    i = 0
    iterations = 0 # extra variable for tracking number of steps

    while i <= twos_index:
        # number of iterations to confirm the algorithm takes len(input_list) steps
        iterations += 1
        if input_list[i] == 0:
            # swap values at zeros_index and i, increment i and zeros index
            input_list[i], input_list[zeros_index] = input_list[zeros_index], input_list[i]
            i += 1
            zeros_index += 1
        elif input_list[i] == 2 and i < twos_index: # not necessary to swap when i == twos_index
            # swap values at twos_index and i, decrement twos_index, do not increment i
            input_list[i], input_list[twos_index] = input_list[twos_index], input_list[i]
            twos_index -= 1
        else:
            # increment i when the current element is 1
            i += 1

    assert(iterations == n) # confirm that iterations is equal to n
    return input_list



def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Edge Cases
# Empty list edge case
test_function([])

# All ones edge case
test_function([1,1,1,1,1,1,1,1])

# All twos edge case
test_function([2,2,2,2,2,2,2,2])

# All zeros edge case
test_function([0,0,0,0,0,0,0,0,0,0])