#name = input("Enter your name? ")
#print(name)
#print(type(name))

"""a = input("1 st no: ")
b = input("2 st no: ")
print(a + b)"""

"""
a = int(input("1 st no: "))
b = int(input("2 st no: "))
print(a + b)"""

"""
a = input("1 st no: ")
b = int(a)
c = input("2 st no: ")
d = int(c)
print(b + d)"""

"""a = input("1 st no: ")
b = input("2 st no: ")
c = int(a) + int(b)
print(c)"""

a = input("1 st no: ")
b = input("2 st no: ")
c = float(a) + float(b)
print(c)


"""
Python divides the operators in the following groups:
    1) Arithmetic operators
    2) Assignment operators
    3) Comparison operators
    4) Logical operators
    5) Identity operators
    6) Membership operators
    7) Bitwise operators"""


"""
# Python Arithmetic Operators
------------------------------------------------------------------------------------------------------------------------
              Operator              |                 Name                   |                  Example          
------------------------------------------------------------------------------------------------------------------------
                 +                  |              Addition                  |                   x + y
                 -                  |              Subtraction               |                   x - y
                 *                  |              Multiplication            |                   x * y
                 /                  |              Division                  |                   x / y
                 %                  |              Modulus                   |                   x % y
                 **                 |              Exponentiation            |                   x ** y
                 //                 |              Floor division            |                   x // y
------------------------------------------------------------------------------------------------------------------------


# Python Assignment Operators
------------------------------------------------------------------------------------------------------------------------
              Operator              |                 Example                   |                Same as    
------------------------------------------------------------------------------------------------------------------------
                =                   |                  x = 5                    |                x = 5
                +=                  |                  x += 5                   |                x = x + 5
                -=                  |                  x -= 5                   |                x = x - 5
                *=                  |                  x *= 5                   |                x = x * 5
                /=                  |                  x /= 5                   |                x = x / 5
                %=                  |                  x %= 5                   |                x = x % 5
                //=                 |                  x //= 5                  |                x = x // 5
                **=                 |                  x **= 5                  |                x = x ** 5
                &=                  |                  x &= 5                   |                x = x & 5
                |=                  |                  x |= 5                   |                x |= 5
                ^=                  |                  x ^= 5                   |                x ^= 5
                >>=                 |                  x >>= 5                  |                x = x >> 5
                <<=                 |                  x <<= 5                  |                x = x << 5
------------------------------------------------------------------------------------------------------------------------


# Python Comparison Operators
------------------------------------------------------------------------------------------------------------------------
              Operator              |                 Name                   |                  Example          
------------------------------------------------------------------------------------------------------------------------
                ==                  |          Equal                         |                  X == Y
                !=                  |          Not Equal                     |                  X != Y
                >                   |          Greater than                  |                  x > y
                <                   |          Less than                     |                  x < y
                >=                  |          Greater than or Equal to      |                  x >= y
                <=                  |          Less than or Equal to         |                  x <= y
------------------------------------------------------------------------------------------------------------------------


# Python Logical Operators
------------------------------------------------------------------------------------------------------------------------
         Operator          |               Description                               |             Example
------------------------------------------------------------------------------------------------------------------------
           and             | Returns True if both statements are true                |        x < 5 and  x < 10
           or              | Returns True if one of the statements is true           |        x < 5 or x < 4
           not             | Reverse the result, returns False if the result is true |        not(x < 5 and x < 10)  
------------------------------------------------------------------------------------------------------------------------


# Python Identity Operators
------------------------------------------------------------------------------------------------------------------------
         Operator        |                Description                                                       |  Example
------------------------------------------------------------------------------------------------------------------------
           in            | Returns True if a sequence with the specified value is present in the object     | x in y
         not in          | Returns True if a sequence with the specified value is not present in the object | x not in y
------------------------------------------------------------------------------------------------------------------------


# Python Bitwise Operators
------------------------------------------------------------------------------------------------------------------------
   Operator   |         Name             |                        Description
------------------------------------------------------------------------------------------------------------------------
       &      |         AND              |   Sets each bit to 1 if both bits are 1
       |      |          OR              |   Sets each bit to 1 if one of two bits is 1
       ^      |         XOR              |   Sets each bit to 1 if only one of two bits is 1
       ~      |         NOT              |   Inverts all the bits
      <<      |   Zero fill left shift   |   Shift left by pushing zeros in from the right and let the leftmost bits fall off
      >>      |   Signed right shift     |   Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
------------------------------------------------------------------------------------------------------------------------
"""
# Arithmetic Operators
print("Arithmetic Operators")

print("5 + 6 is", 5 + 6)
print("5 - 6 is", 5 - 6)
print("5 * 6 is", 5 * 6)
print("5 / 6 is", 5 / 6)
print("5 // 6 is", 5 // 6)
print("15 // 6 is", 15 // 6)
print("5 ** 3 is", 5 ** 3)
print("5 % 3 is", 5 % 3)
print("5 % 5 is", 5 % 5)



# Assignment Operators
# It is mainly used when we want to determine the value of a variable
print("Assignment Operators")

x = 5
print(x)

x += 7
print(x)

x -= 5
print(x)

x *= 7
print(x)

x /= 7
print(x) # here output is 7.0

x %= 5
print(x)



# Comparison Operators
print("Comparison Operators")

i = 8
print(i == 5)

print(i == 8)

print(i != 5)

print(i > 8)

print(i >= 8)

print(i <= 8)



# Logical Operators
print("Logical Operators")

a = True
b = False

print(a and a)

print(a and b)


print(a or b)




# Identity Operators
print("Identity Operators")

print(a is b)

print(a is not b)

print(5 is not 7)

print(5 is not 5)



# Membership Operators
print("Membership Operators")

list = [3, 3, 2, 3, 33, 35, 32]
print(32 in list)

print(324 in list)

print(324 not in list)



# Bitwise Operators
print("Bitwise Operators")
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 1)
print(0 | 1)