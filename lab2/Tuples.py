#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuple Length:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Access Tuple Items:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Change Tuple Values:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add Items:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Unpacking a Tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Loop Through a Tuple:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Loop Through the Index Numbers:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Join Two Tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

