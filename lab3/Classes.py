#1:
class ChangeString:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())
        print(self.input_string.lower())

obj = ChangeString()
obj.getString()
obj.printString()


#2:
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

shape = Shape()
print(f"Area of Shape: {shape.area()}")

square = Square(4)
print(f"Area of Square: {square.area()}")

#3:
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shape = Shape()
print(f"Area of Shape: {shape.area()}")

rectangle = Rectangle(5, 3)
print(f"Area of Rectangle: {rectangle.area()}")

#4:
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


point1 = Point(1, 2)
point1.show() 

point2 = Point(4, 6)
print(f"Distance between points: {point1.dist(point2)}")

point1.move(3, 4)
point1.show() 

#5:
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount}. Balance is now: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Took out {amount}. Balance is now: {self.balance}")
        else:
            print("Not enough money!")


account = Account("Alice", 100)

account.deposit(50)
account.withdraw(30) 
account.withdraw(150) 

#6:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 13, 17, 18, 19]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)


