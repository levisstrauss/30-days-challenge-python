if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    totalSwaps = 0  # to keep track of total swaps
    for i in range(n):
        # Inner loop to actually perform the swapping
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # swap
                totalSwaps += 1

        # Optimized approach: If no two elements were swapped in inner loop, then break
        if totalSwaps == 0:
            break

    # Printing the results
    print("Array is sorted in", totalSwaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])