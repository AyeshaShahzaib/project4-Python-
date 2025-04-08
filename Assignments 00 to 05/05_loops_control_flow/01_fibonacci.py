# Constant for maximum value
MAX_VALUE = 10000

# Starting values
a, b = 0, 1

# Print the Fibonacci sequence
while a < MAX_VALUE:
    print(a, end=" ")
    a, b = b, a + b
