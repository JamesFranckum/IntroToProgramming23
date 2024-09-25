print()
import math
radius = int(input('What is your height in centimeters? '))
print(f'The area of the circle you can fit in is {radius ** 2 * math.pi} square centimeters')
print(f'The area of the circle you can fit in is {(radius ** 2 * math.pi) / 100} square meters')
print()
print(f'The area of a rectangle you can fit in is {radius ** 2}')
print(f'The area of a cube you can fit in is {radius ** 2 * 6}')
print(f'The area of a sphere you can fit in is {4 * math.pi * radius ** 2}')
