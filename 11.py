list1 = ["Sourav", "Sayani"]
for item in list1:
    print(item)

tuple1 = ("Sourav", "Sayani")
for item in tuple1:
    print(item)

list2 = [["Sourav", 1], ["Sayani", 2]]
for item in list2:
    print(item)

for item, biriyani in list2:
    print(item, biriyani)

for item, biriyani in list2:
    print(item, "has", biriyani, "Packet biriyani")

"""list3 = [[input("Enter name "), int(input("No of packet has "))], [input("Enter name "), int(input("No of packet has "))]]
for item, biriyani1 in list3:
    print(item, "has", biriyani1, "Packet biriyani")"""

dict1 = dict(list2)
print(dict1)

"""
# we can not write this type of code
for item, biriyani2 in dict:
    print(item, "has", biriyani2, "Packet biriyani")"""

for item, biriyan2 in dict1.items():
    print(item, "has", biriyan2, "Packet biriyani")

for item in dict1:
    print(item)

items = ["Sourav", "Sayani", 2021]
for item in items:
    if str(item).isnumeric():
        print(item)


items1 = ["Sourav", "Sayani", 2021, 2022, 2023, 2024]
for item in items1:
    if str(item).isnumeric() and  item >= 2021:
        print(item)

for Sayani_Sourav in range(0,10):
    print(Sayani_Sourav)

for Sayani_Sourav1 in range(6):
    if Sayani_Sourav1 == 3:
        print(Sayani_Sourav1)
        break
    else:
        print("Value of Sayani_Sourav1 ", Sayani_Sourav1)


for i in range(7,17,7):
    print(i)

for i1 in "Srijit":
    print(i1)


name = ["Sourav", "Sayani"]
food = ["Biriyani", "pizza"]
for x in name:
    for y in food:
        print(x, y)



