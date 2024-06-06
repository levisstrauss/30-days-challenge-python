import math
import os
import random
import re
import sys


def max_consecutive_ones(n):
    binary_number = bin(n)[2:]
    consecutive_ones = binary_number.split('0')
    return max(len(group) for group in consecutive_ones)


if __name__ == '__main__':
    n = int(input().strip())
    print(max_consecutive_ones(n))

