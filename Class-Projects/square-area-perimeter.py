def square_area_perimeter(side):
    area = side ** 2
    perimeter = 4 * side
    return area, perimeter

# Example Usage:
side = 5
area, perimeter = square_area_perimeter(side)
print(f"Area: {area}, Perimeter: {perimeter}")