def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Example Usage:
length = 6
width = 4
area, perimeter = rectangle_area_perimeter(length, width)
print(f"Area: {area}, Perimeter: {perimeter}")