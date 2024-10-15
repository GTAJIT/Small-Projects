import math

def triangle_area_perimeter(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula
    return area, perimeter

# Example Usage:
a = 3
b = 4
c = 5
area, perimeter = triangle_area_perimeter(a, b, c)
print(f"Area: {area}, Perimeter: {perimeter}")