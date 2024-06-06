import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    names = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]

        # Check if the email ID ends with "@gmail.com"
        if emailID.endswith("@gmail.com"):
            names.append(firstName)

    # Sort the names alphabetically
    names.sort()

    # Print the names
    for name in names:
        print(name)