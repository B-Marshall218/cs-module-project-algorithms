'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(list_to_sort):
    for i in range(1, len(list_to_sort)):
        temp = list_to_sort[i]
        j = i

        while j > 0 and temp < list_to_sort[j-1]:
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
            list_to_sort[j] = temp
    return list_to_sort


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    list_to_sort = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(list_to_sort)}")
