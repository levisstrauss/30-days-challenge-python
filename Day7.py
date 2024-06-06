def main():
    n = int(input().strip())

    # Ensure that n adheres to the given constraints
    if n < 1 or n > 1000:
        raise ValueError("The value of N is out of bounds")

    arr = list(map(int, input().strip().split()))

    # Check each value in the list for constraints
    for num in arr:
        if num < 1 or num > 10000:
            raise ValueError("Array element value is out of bounds")

    # Print elements in reverse order
    for i in reversed(arr):
        print(i, end=' ')
    print()  # Print a newline after printing all elements


if __name__ == '__main__':
    main()
