import math

# calculating area of rectangle
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Taking user input for length and width of rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# calculating area of rectangle
area_of_rectangle = calculate_rectangle_area(length, width)
print(f"The area of the rectangle with length {length} and width {width} is: {area_of_rectangle}")

# Area of circle
def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

# Taking user input for the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# calculating area of circle
area_of_circle = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area_of_circle}")

# Area of triangle
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

# Taking user input for the base and height of the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# calculating area of triangle
area_of_triangle = calculate_triangle_area(base, height)
print(f"The area of the triangle with base {base} and height {height} is: {area_of_triangle}")

# Area of square
def calculate_square_area(side):
    area = side**2
    return area

# Taking user input for the side of the square
side = float(input("Enter the side length of the square: "))

# calculating area of square
area_of_square = calculate_square_area(side)
print(f"The area of the square with side length {side} is: {area_of_square}")

# Area of trapezoid
def calculate_trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

# Taking user input for the bases and height of the trapezoid
base1 = float(input("Enter the length of base 1 of the trapezoid: "))
base2 = float(input("Enter the length of base 2 of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))

# calculating area of trapezoid
area_of_trapezoid = calculate_trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid with bases {base1} and {base2} and height {height} is: {area_of_trapezoid}")

# Area of parallelogram
def calculate_parallelogram_area(base, height):
    area = base * height
    return area

# Taking user input for the base and height of the parallelogram
base = float(input("Enter the base length of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

# calculating area of parallelogram
area_of_parallelogram = calculate_parallelogram_area(base, height)
print(f"The area of the parallelogram with base {base} and height {height} is: {area_of_parallelogram}")