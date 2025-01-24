#The length of a list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

 #Access list items:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Change Item Value:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Add List Item(append):
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Remove Specified Item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Clear the List:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Through a List:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#List Comprehension:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Sort List Alphanumerically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort Descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Copy Lists:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Join Lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


