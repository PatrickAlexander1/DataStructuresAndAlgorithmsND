def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    def get_digit_lengths(n):

        is_even = n % 2 == 0
        if is_even:
            return n // 2, n // 2
        else:
            return (n // 2) + 1, n // 2

    def rearrange_digits_helper(input_list, n_digits1, n_digits2, out = [0, 0]):
        
        if n_digits1 == 0 and n_digits2 == 0:
            print(out)
            return out

        elif n_digits1 >= n_digits2:
            out[0] += input_list[-1] * (10 ** (n_digits1 - 1))
            n_digits1 -= 1
            return rearrange_digits_helper(input_list[:-1], n_digits1, n_digits2)

        elif n_digits1 < n_digits2:
            out[1] += input_list[-1] * (10 ** (n_digits2 - 1))
            n_digits2 -= 1
            return rearrange_digits_helper(input_list[:-1], n_digits1, n_digits2)
    
    def merge_sort(arr):

        def merge(left, right):

            left_index, right_index = 0, 0
            left_len, right_len = len(left), len(right)
            out = []

            while left_index < left_len and right_index < right_len:

                if left[left_index] < right[right_index]:
                    out.append(left[left_index])
                    left_index += 1
                else:
                    out.append(right[right_index])
                    right_index += 1

            return out + left[left_index:] + right[right_index:]

        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            return merge(merge_sort(left), merge_sort(right))

    input_list = merge_sort(input_list)
    n = len(input_list)
    n_digits1, n_digits2 = get_digit_lengths(n)
    return rearrange_digits_helper(input_list, n_digits1, n_digits2)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Standard cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


# Edge Cases
# List with only 0 as element, function still produces the correct output
test_function([[0], [0, 0]])

# Edge case with many zeros
test_function([[1,1,0,0,0,0,0,0,0,0], [10000, 10000]])

# Edge case with empty array
test_function([[], [0, 0]])
