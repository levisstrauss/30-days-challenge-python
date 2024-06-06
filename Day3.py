if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1:  # Check if n is odd
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:  # Check if n is even and between 2 to 5
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:  # Check if n is even and between 6 to 20
        print("Weird")
    else:  # If n is even and greater than 20
        print("Not Weird")