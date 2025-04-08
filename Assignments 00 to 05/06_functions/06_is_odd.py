def check_even_odd(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")

# Call the function with the desired range
check_even_odd(10, 19)
