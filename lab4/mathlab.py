import math

#1:
degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))

#2:
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
trapezoid_area = 0.5 * (base1 + base2) * height
print("Expected Output:", trapezoid_area)

#3:
import math
sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
apothem = length / (2 * math.tan(math.pi / sides))
polygon_area = (sides * length * apothem) / 2
print("The area of the polygon is:", int(polygon_area))


#4:
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
parallelogram_area = base * height
print("Expected Output:", parallelogram_area)
