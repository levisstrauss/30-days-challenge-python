class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        max_val = max(self.__elements)
        min_val = min(self.__elements)
        self.maximumDifference = max_val - min_val


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)