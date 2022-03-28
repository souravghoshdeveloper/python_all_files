var1 = {}
print(type(var1))

var2 = []
print(type(var2))

var3 = ()
print(type(var3))

var4 = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud"}
print(var4)
print(var4["Sourav"])
print(var4["Chitrajyti"])
print(var4["Shinjini"])

"""
var5 = {"Name":"Sourav", "Sayani":{"B":"biriyani", "C":"cold coffee", "P":"paprichat", "F":"fuchka", "I":"icecream"}}
print(var5["Sayani"])
print(var5["Sayani"]["B"])
print(var5["Sayani"]["C"])
print(var5["Sayani"]["P"])
print(var5["Sayani"]["F"])
print(var5["Sayani"]["I"])"""

var5 = {"Name":"Sayani", "Sourav":{"B":"biriyani", "C":"cold coffee", "P":"paprichat", "F":"fuchka", "I":"icecream"}}
print(var5["Sourav"])
print(var5["Sourav"]["B"])
print(var5["Sourav"]["C"])
print(var5["Sourav"]["P"])
print(var5["Sourav"]["F"])
print(var5["Sourav"]["I"])


var6 = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud"}
var6["Arijit"] = "Nokia"
print(var6)


var7 = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud", "food":{"B":"biriyani", "C":"cold coffee", "P":"paprichat", "F":"fuchka", "I":"icecream"}}
var7["Arijit"] = "Nokia"
print(var7)


var8 = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud"}
var8["Arijit"] = "Nokia"
var8["Srijit"] = "Poulami"
print(var8)
del var8["Arijit"]
print(var8)


var9 = {"Sourav":"Sayani"}
var9[2017] = "Chitrajyoti"
print(var9)
del var9[2017]
print(var9)


var10 = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud"}
print(var10.copy())


var11 = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud"}
var12 = var11
del var12["Chitrajyti"]
print(var11)



var13 = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud"}
var14 = var13.copy()
del var13["Shinjini"]
print(var13)

var15 = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud"}
print(var15.get("Sourav"))

var16 = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud", "food":{"B":"biriyani", "C":"cold coffee", "P":"paprichat", "F":"fuchka", "I":"icecream"}}
var16.update({"PA":"pastry"})
print(var16)


dict1 = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud"}
print(dict1.keys())
print(dict1.items())


user = {"Sourav":"Sayani", "Chitrajyti":"Anushka", "Shinjini":"Masud"}
input_user = input("Enter a name ")
input_user1 = input_user.capitalize()
print(user[input_user1])

