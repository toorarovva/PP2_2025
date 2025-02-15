#1:
def square_generator(N):
    for i in range(N + 1):
        yield i * i

for num in square_generator(5):
    print(num)

#2:
def even(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(str(i))
    print(", ".join(evens))
n = int(input("n: "))
even(n)

#3:
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            print(i)

n = int(input("n: "))
div_by_3_and_4(n)

#4:
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
a, b = int(input()), int(input())
for num in squares(a, b):
    print(num)

#5:
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("n: "))
for number in countdown(n):
    print(number)

