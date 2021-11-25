def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # find the pivot
    def find_pivot(input_list, low, high):

        if len(input_list) == 1:
            return 0
        if low >= high:
            return -1
        mid = (low + high) // 2
        if input_list[mid] > input_list[mid + 1]:
            return mid + 1
        else:
            return max(find_pivot(input_list, low, mid), find_pivot(input_list, mid + 1, high))
            
    def binary_search(arr, target, low, high):

        if low > high:
            return -1

        mid = (low + high) // 2
        current = arr[mid]

        if current == target:
            return mid
        elif target < current:
            return binary_search(arr, target, low, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, high)

    # get pivot index
    pivot_index = find_pivot(input_list, 0, len(input_list) - 1)
    # search left and right sublists
    target_index_right = binary_search(input_list[pivot_index:], number, 0, len(input_list[pivot_index:]) - 1)
    target_index_left = binary_search(input_list[:pivot_index], number, 0, len(input_list[:pivot_index]) - 1)
    
    # return the correct index
    if target_index_right != -1:
        # adjust index by adding pivot_index
        return target_index_right + pivot_index
    elif target_index_left != -1:
        return target_index_left
    else:
        return -1



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge Cases
# Edge case where there is no rotation in the array
test_function([[1, 2, 3, 4], 2])

# Edge case when there is a two element list with a rotation
test_function([[1, 0], 1])

# Edge case when there an array with one element
test_function([[2], 2])

# Edge case with empty array
test_function([[], 2])

