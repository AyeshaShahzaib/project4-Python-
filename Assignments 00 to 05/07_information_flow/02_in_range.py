def in_range(n, low, high):
    """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """
    return low <= n <= high

# Test cases
print(in_range(5, 1, 10))  # True, because 5 is between 1 and 10
print(in_range(0, 1, 10))  # False, because 0 is less than 1
print(in_range(15, 10, 20))  # True, because 15 is between 10 and 20
print(in_range(25, 10, 20))  # False, because 25 is greater than 20
