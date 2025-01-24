#Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Access Items:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Add Items:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Remove Item:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Loop Items:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
