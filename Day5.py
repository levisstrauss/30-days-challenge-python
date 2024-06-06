t = int(input())

# Iterate through each test case
for _ in range(t):
    s = input().strip()  # Input string for each test case
    even_chars = ''
    odd_chars = ''

    # Separate the string into even-indexed and odd-indexed characters
    for i in range(len(s)):
        if i % 2 == 0:
            even_chars += s[i]
        else:
            odd_chars += s[i]

    # Print the results
    print(even_chars, odd_chars)