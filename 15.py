# function
a = 9
b = 8
c = sum((a,b)) # Built in Function
print(c)

# user define function
def function1():
    print("Hello You are in Function 1")

# print(function1())


function1() # here the output is Hello You are in Function 1


"""function1() # output - Hello You are in Function 1
function1() # output - Hello You are in Function 1
function1() # output - Hello You are in Function 1
function1() # output - Hello You are in Function 1
function1() # output - Hello You are in Function 1"""



#-------------------------------------------------------------
def function2(d, e):
    print("Hello you are in function 2", d + e)

function2(5, 7)


#-------------------------------------------------------------
def function3(f, g):
    average = (f + g)/2
    print(average)

function3(5, 7)



#-------------------------------------------------------------
def function4(h, i):
    average1 = (h + i)/2
    print(average1)
    return average1 # It (retun) is mainly used to reflect the value of a function in a Python variable.
v = function4(6, 8)
print(v)




#---------------------------------------------------------------
# Docstrings
def function5(j, k):
    """This is a function which will calculate average of two numbers"""  # Doc String
    average3 = (j + k)/2
    print(average3)
    return average3
u = function5(10, 12)
print(u)
print(function5.__doc__) # Output - This is a function which will calculate average of two numbers



# another example
def function6(l, m):
    """This is a function which will calculate average of two numbers
    This function doesnot work for three numbers"""
    average2 = (l + m)/2
    print(average2)
    return average2
t = function6(15, 17)
print(t)
print(function6.__doc__)






def favorite_food(food):
    print("Sayani's favorite food is", food)

favorite_food("biryani")
favorite_food("Fuchka")
favorite_food("Pizza")




def love(name1, name2):
    print(name1 + " & " + name2 + " love each other")

love("Sourav", "Sayani")



#----------------------------------------------------------------
def friend(name3, name4):
    print(name3 + " & " + name4 + " are very good friend")

friend(name3 = input("Enter a Name ") ,name4 = input("Enter another Name "))



def hi(*name5):
    print("Hi, This is ", name5[1])
hi("Sourav", "Sayani")




def hello(name6, name7):
    print("My name is ", name6)

hello(name6="Sourav", name7="Sayani")




def hi1(**name8):
    print("This is " + name8["Firstname"])
hi1(Firstname= "Sourav", lastname= "Ghosh")



def college(College_name = "Netaji Subhash Engineering College"):
    print("I am from "+ College_name)
college("Ghani Khan Choudhury Institute of Engineering & Technology")
college()



def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)




def Multiplication_function(x):
  return 5 * x

print(Multiplication_function(2))
print(Multiplication_function(5))
print(Multiplication_function(7))




#-------------------------------------------------------------
# Quiz
def Multiply_with_pi(y):
    return 3.14159265359 * y
print(Multiply_with_pi(int(input("Enter a number to Multiply with pi "))))
print(Multiply_with_pi(int(input("Enter a number to Multiply with pi "))))
print(Multiply_with_pi(int(input("Enter a number to Multiply with pi "))))



#------------------------------------------------------------
# Another Quiz
number_of_multiply = 0
How_many_times_do_you_want_to_multiply  = int(input("How many times do you want to multiply with pi? "))
def Multiply_with_pi1(z):
    return 3.14159265359 * z

while(number_of_multiply < How_many_times_do_you_want_to_multiply):
    print(Multiply_with_pi1((int(input("Enter a number to Multiply with pi ")))))
    number_of_multiply = number_of_multiply + 1



#-------------------------------------------------------------
# empty function can raise an error without the pass statement
def sourav():
    pass
sourav()
