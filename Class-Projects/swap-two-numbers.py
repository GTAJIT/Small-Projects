def swap_numbers(a, b):
    a, b = b, a
    return a, b

# Example Usage:
a = 3
b = 7
a, b = swap_numbers(a, b)
print(f"Swapped values: a = {a}, b = {b}")