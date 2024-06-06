def hourglassSum(arr):
    # Initialize max_sum to a very small negative number as hourglasses can also have negative sums.
    max_sum = -63  # as the minimum value in the array is -9, so the smallest sum is 7*-9 = -63

    for i in range(4):  # loop to go through rows
        for j in range(4):  # loop to go through columns
            # Calculate the sum for the current hourglass
            top = sum(arr[i][j:j + 3])
            middle = arr[i + 1][j + 1]
            bottom = sum(arr[i + 2][j:j + 3])
            hourglass = top + middle + bottom

            if hourglass > max_sum:
                max_sum = hourglass

    return max_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)