'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    list1 = []
    list2 = []
    for num in arr:
        if num not in list1:
            list1.append(num)
        else:
            list2.append(num)
    for num in list1:
        if num not in list2:
            return num
    # return -1


arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

print(f"The odd-number-out is {single_number(arr)}")

# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

#     print(f"The odd-number-out is {single_number(arr)}")
