def main():
    number_of_tests = int(input())

    for _ in range(number_of_tests):
        s = input()
        even_chars = []
        odd_chars = []

        for j in range(len(s)):
            if j % 2 == 0:
                even_chars.append(s[j])
            else:
                odd_chars.append(s[j])

        print("".join(even_chars), "".join(odd_chars))


if __name__ == "__main__":
    main()
