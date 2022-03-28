# Set
set1 = set()
print(type(set1))

a_list = set([1, 2, 3])
print(a_list)
print(type(a_list))

food = {"pizza", "coffee", "tea", "bread"}
print(type(food))

number1 = [1, 2, 3, 4, 5]
number2 = set(number1)
print(type(number2))



set2 = set()
set2.add(1)
print(set2)

set2.add(1)
print(set2)

set2.add(2)
print(set2)

set2.union({1,2})
print(set2)

set3 = set2.union({1, 2, 3})
print(set2, set3)

set4 = set2.intersection({1, 2, 3})
print(set2, set4)

print(len(set2))
print(max(set2))
print(min(set2))

number3 = {4, 6}
number3.remove(6)
print(number3)


name = {"Sourav", "Sayani"}
print(len(name))

name1 = {"Sourav", "Sayani", "Sayani"}
name2 = set(name1)
print(name2)

name3 = ("Sayani", 21, 54.0)
name4 = set(name3)
print(name3)
print(type(name4))

number4 = {1, 2}
number5 = set(number4)
number6 = {4, 6}
number7 = set(number6)
print(number5.isdisjoint(number7))