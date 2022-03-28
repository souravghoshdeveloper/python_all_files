#in a single program we can't use if or else in twice
# we can use "if" in an individual program bt we can't use "else" individually
#we can use "elif"  multiple time in a program

"""
var1 = int(input("Enter a number "))
var2 = int(input("Enter 2 nd number "))

if var2 > var1:
    print("Var2 is greter")
else:
    print("Var1 is greter")

"""

"""
var3 = int(input("Enter a number "))
var4 = int(input("Enter 2 nd number "))

if var4 > var3:
    print("Var4 is greter")
elif var4 == var3:
    print("Var3 = Var4")
else:
    print("Var3 is greter")
"""

"""age = int(input("Enter age "))
if age < 18:
    print("Your age is between 0 - 18")
elif age == 18:
    print("Your age is 18")
else:
    print("your age is not between 0 - 18")"""


"""
age1 = int(input("Enter your age "))
if age1 == 21:
    print("Ja icha")
else:
    print("You are not allowed")"""


"""
age2=int(input("enter your age"))
if age2 < 18:
    print("you are not elligible for vote")
elif age2==18:
    print("waiting for voter card")
else:
    print("elligible for vote")"""



"""
print("Enter your age")
age10 = int(input())

if age10 > 18:
    print("You can drive")
elif age10== 18:
    print("We will think about you")
else:
    print("You can't drive")"""




"""
digit1=int(input("enter 1 st number "))
digit2=int(input("enter 2 nd number "))
symbol1 = input("Plese enter '+', '-', '*', '/' ")
if symbol1 == "+" or symbol1 == "-" or symbol1 == "*" or symbol1 == "/":
    if symbol1 == "+":
        print(digit1 + digit2)
    elif symbol1 == "-":
        if digit1<digit2:
            print("your output will be negative", digit1 - digit2)
        else:
            print(digit1 - digit2)
    elif symbol1 == "*":
        print(digit1 * digit2)
    else:
        print(digit1 / digit2)
else:
    print("You have enter an invalid input")"""



"""
list1 = [1, 2, 3]
print(2 in list1)



list2 =[5,6,7]
list3 =int(input("enter a number"))
if list3 in list2:
    print("true")
else:
    print("is no exist")"""


"""list4 =[5,6,7]
list5 =int(input("enter a number"))
if list5 not in list4:
    print("is not exist")
else:
    print("is exist")"""


enter_age = int(input("Enter your age "))
if enter_age > 7 and enter_age < 100:
    if enter_age > 18:
        print("You can drive")
    elif enter_age == 18:
        print("We will think about you")
    else:
        print("You can't drive")
else:
    print("Please enter a valid age")





# Faulty Calculator
# 45 *  3 = 555, 56+9 = 77, 56/6 = 4
# Design a  calculator which wll correctly solve all the problems except the following ones: 45 *3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator and the two numbers as as input from the user and then retur the result

first_number = int(input("Enter first number "))
enter_operator = input("Enter operator? ")
second_number = int(input("Enter second number "))


if first_number == 45 and enter_operator == "*"  and second_number == 3:
    print("555")
elif first_number == 56 and enter_operator == "+" and second_number == 9:
    print("77")
elif first_number == 56 and enter_operator == "/" and second_number == 6:
    print("4")
else:
    if enter_operator == "+":
        print("Sum of this two number is ",first_number + second_number)
    elif enter_operator == "-":
        print("Subtraction of this two number is ",first_number - second_number)
    elif enter_operator == "*":
        print("Multiplication of this two number is ",first_number * second_number)
    elif enter_operator == "/":
        print("Division of this two number is ",first_number / second_number)
    else:
        print("Please enter +, -, * or /")




# Short hand if else Notation
a = int(input("enter a\n"))
b = int(input("enter b\n"))

print("B A ar thaka boro") if a < b else print("A B ar thaka boro")





#--------------------------------------------------------------------------------------------------------
# Both are same
"""
# Short hand if else Notation
a = int(input("enter a\n"))
b = int(input("enter b\n"))

print("B A ar thaka boro") if a < b else print("A B ar thaka boro")


#------------------------------
a = int(input("enter a\n"))
b = int(input("enter b\n"))
if a > b:
    print("A B ar thaka boro")
else:
    print("B A ar thaka boro")"""