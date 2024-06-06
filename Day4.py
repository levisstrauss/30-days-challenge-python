class Person:

    def __init__(self, initialAge):
        # Confirm if the initialAge is non-negative
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        # Check the value of age and print the appropriate message
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age by 1
        self.age += 1


# Provided stub code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        age = int(input())
        p = Person(age)
        p.amIOld()
        for _ in range(3):  # Incrementing age by 3 years
            p.yearPasses()
        p.amIOld()
        print("")