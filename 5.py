# String Slicing
Sourav = "You aree the presious gift of my life"
print(Sourav[2])
print(Sourav[4:7])

Sayani = "Sayani, Sourav"
print(Sayani[8:14])

print(len(Sourav))

gkciet = "Ghani Khan Choudhury Institute of Engineering & Technology (GKCIET),malda, A Centrally Funded Technical Institute(CFTI) under Ministry of Education,"
print(gkciet[0:])
print(gkciet[2:])
print(len(gkciet))
print(gkciet[::2])
print(gkciet[::])
print(gkciet.capitalize())
print(gkciet.lower())
print(gkciet.upper())
print(gkciet.lower())
print(gkciet)
print(gkciet.islower())
print(gkciet.isupper())

Love = "I LOVE YOU"
print(Love.isupper())
print(Love.isdigit())
print(Love.endswith("YOU"))


sourav=input("Enter your name ")
print(sourav.upper())
"""letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)"""


#------------------------------------------------------------------------------------------------------
"""statement = "This is a string with double  spaces"

doubleSpace = statement.find("  ")
print(doubleSpace)"""


#------------------------------------------------------------------------------------------------------
"""statement1 = "This is a string with double  spaces  ok"

statement1 = statement1.replace("  ", " ")
print(statement1)"""


#------------------------------------------------------------------------------------------------------
"""statement3 = input("Enter a statement \n")
statement3 = statement3.replace("  ", " ")
print(statement3)"""


#------------------------------------------------------------------------------------------------------
"""
# String Methods --> Method	Description

upper()	       - Converts a string into upper case
lower()	       - Converts a string into lower case
capitalize()   - Converts the first character to upper case
casefold()	   - Converts string into lower case
center()	   - Returns a centered string
count()	       - Returns the number of times a specified value occurs in a string
endswith()	   - Returns true if the string ends with the specified value
expandtabs()   - Sets the tab size of the string
find()	       - Searches the string for a specified value and returns the position of where it was found
format()	   - Formats specified values in a string
index()	       - Searches the string for a specified value and returns the position of where it was found
isalnum()	   - Returns True if all characters in the string are alphanumeric
isalpha()	   - Returns True if all characters in the string are in the alphabet
isdecimal()	   - Returns True if all characters in the string are decimals
isdigit()	   - Returns True if all characters in the string are digits
isidentifier() - Returns True if the string is an identifier
isnumeric()	   - Returns True if all characters in the string are numeric
islower()	   - Returns True if all characters in the string are lower case
isspace()	   - Returns True if all characters in the string are whitespaces
istitle()	   - Returns True if the string follows the rules of a title
join()	       - Joins the elements of an iterable to the end of the string
ljust()	       - Returns a left justified version of the string
isupper()	   - Returns True if all characters in the string are upper case
lstrip()	   - Returns a left trim version of the string
maketrans()    - Returns a translation table to be used in translations
partition()	   - Returns a tuple where the string is parted into three parts
replace()	   - Returns a string where a specified value is replaced with a specified value
rfind()	       - Searches the string for a specified value and returns the last position of where it was found
rindex()	   - Searches the string for a specified value and returns the last position of where it was found
rjust()	       - Returns a right justified version of the string
rpartition()   - Returns a tuple where the string is parted into three parts
rsplit()	   - Splits the string at the specified separator, and returns a list
rstrip()	   - Returns a right trim version of the string
split()	       - Splits the string at the specified separator, and returns a list
splitlines()   - Splits the string at line breaks and returns a list
startswith()   - Returns true if the string starts with the specified value
strip()	       - Returns a trimmed version of the string
swapcase()	   - Swaps cases, lower case becomes upper case and vice versa
title()	       - Converts the first character of each word to upper case
zfill()	       - Fills the string with a specified number of 0 values at the beginning"""


#--------------------------------------------------------------------------------------------------------------
# Example

# upper() - Converts a string into upper case
"""variable1 = "If I know what love is, it is because of you."
print(variable1.upper())"""


# lower() - Converts a string into lower case
"""variable2 = "It’s always better when we’re together."
print(variable2.lower())"""


# capitalize() - Converts the first character to upper case
"""variable3 = "i Have Found The One Whom My Soul Loves."
print(variable3.capitalize())"""


# casefold() - Converts string into lower case
"""variable4 = "In all the world, there is no heart for me like you. In all the world, there is no love for you like mine."
print(variable4.casefold())"""


# center() - Returns a centered string
"""variable5 = "I need you like a heart needs a beat."
print(variable5.center(100))"""


# count() - Returns the number of times a specified value occurs in a string
"""variable6 = "To me, you are perfect."
print(variable6.count("you"))"""


# endswith() - Returns true if the string ends with the specified value
"""variable7 = "“I promise to love you forever, every single day of forever."
print(variable7.endswith("forever"))"""


# expandtabs() - Sets the tab size of the string
"""variable8 = "T\th\ti\ts"
print(variable8.expandtabs(1))"""



# find() - Searches the string for a specified value and returns the position of where it was found
# ***Note: The find() method returns -1 if the value is not found.
"""variable9 = "Every time I see you, I fall in love all over again"
print(variable9.find("time"))"""


# format() - Formats specified values in a string
"""variable10 = "cost of biryani is {price:.3f} rupee"
print(variable10.format(price = 80)) # Output - 80.000"""
"""
another example
variable10 = "cost of biryani is {price:.2f} rupee"
print(variable10.format(price = 80)) # output - 80.0

** Note: Here .1f is Format specifier
"""


# index() - Searches the string for a specified value and returns the position of where it was found
"""variable11 = "Sayani, I love You"
print(variable11.index("I"))"""


# isalnum()	- Returns True if all characters in the string are alphanumeric
"""variable12 = "#"
print(variable12.isalnum()) # Output - False (Because a Special character cannot be alphanumeric."""


# isalpha()	   - Returns True if all characters in the string are in the alphabet
"""variable13 = "I"
print(variable13.isalpha())"""



# isdecimal() - Returns True if all characters in the string are decimals
# Not important
"""variable14 = "I2021"
print(variable14.isdecimal())"""



# isdigit() - Returns True if all characters in the string are digits
"""variable15 = "2021"
print(variable15.isdigit())""" # Output - true



# isidentifier() - Returns True if the string is an identifier
"""
***Note:
The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
A valid identifier cannot start with a number, or contain any spaces."""

"""variable16 = "1Hi"
print(variable16.isidentifier()) # Output - False"""


# isnumeric() - Returns True if all characters in the string are numeric
"""variable17 = "2021"
print(variable17.isnumeric())"""



# islower()	   - Returns True if all characters in the string are lower case
"""variable18 ="sayani, i love you"
print(variable18.islower())"""


# isspace() - Returns True if all characters in the string are whitespaces
"""variable19 = " "
print(variable19.isspace())"""


# istitle()	- Returns True if the string follows the rules of a title
"""
***Note:
The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
Symbols and numbers are ignored.
"""
"""variable19 = "I Love You"
print(variable19.istitle())"""



# join() - Joins the elements of an iterable to the end of the string
"""love = ("Sourav", "Sayani")
print(" + ".join(love))"""


# ljust() - Returns a left justified version of the string
# Not important
"""variable20 = "Biriyani"
print(variable20.ljust(10), "is my favorite food")"""



# isupper()	   - Returns True if all characters in the string are upper case
"""variable21 = "I LOVE YOU"
print(variable21.isupper())"""



# lstrip() - Returns a left trim version of the string
# **Note: The lstrip() method removes any leading characters (space is the default leading character to remove)
"""variable22 = "          Biriyani          "
print(variable22.lstrip(), "is my favorite food")""" # output - Biriyani           is my favorite food



# maketrans()    - Returns a translation table to be used in translations
"""variable23 = "Hello Arijit"
print(variable23.translate(variable23.maketrans("A", "S")))"""  # output - Hello Srijit



# partition() - Returns a tuple where the string is parted into three parts
"""variable24 = "I could eat biriyani all day"
print(variable24.partition("biriyani"))"""  # Output - ('I could eat ', 'biriyani', ' all day')



# replace()	- Returns a string where a specified value is replaced with a specified value
"""variable25 = "My favorite food is Pizza"
print(variable25.replace("Pizza", "Biriyani"))""" # My favorite food is Biriyani


# rfind() - Searches the string for a specified value and returns the last position of where it was found
"""
*** Note:
1) The rfind() method finds the last occurrence of the specified value.
2) The rfind() method returns -1 if the value is not found.
3) The rindex() method is almost the same as the rfind() method. See example below.
"""
"""variable26 = "I love you Sayani. Sayani, you are the precious gift of my life"
print(variable26.rfind("Sayani"))""" # Output -> 19 (Because The rfind() method finds the last occurrence of the specified value.)


# rindex() - Searches the string for a specified value and returns the last position of where it was found
"""
*** Note:
1) The rindex() method finds the last occurrence of the specified value.
2) The rindex() method raises an exception if the value is not found.
3) The rindex() method is almost the same as the rfind() method. See example below.
"""

"""variable27 = "Sayani I love you. Sayani, you are the precious gift of my life"
print(variable27.rindex("Sayani"))"""  # Output -> 19



#------------------------------------------------------------------------------------------------------|
"""                                                                                                    |
*** difference between rfind() and rindex()                                                            |
----------------------------------------------------------------------------------------------------   |
|                   rfind()                         |                    rindex()                  |   |
|---------------------------------------------------|----------------------------------------------|   |
|    1) The rfind() method returns -1 if the value  |   1) The rindex() method raises an exception |   |
|       is not found.                               |      if the value is not found.              |   |
|---------------------------------------------------------------------------------------------------   |
"""
#------------------------------------------------------------------------------------------------------|




# rjust() - Returns a right justified version of the string
# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
# Not important
"""variable28 = "I like Fuchka"
print(variable28.rjust(15))"""





# rpartition() - Returns a tuple where the string is parted into three parts
# *** Note: The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
"""variable29 = "I could eat biyiyani all day, biriyani are my favorite food"
print(variable29.rpartition("biriyani")) # Output - ('I could eat biyiyani all day, ', 'biriyani', ' are my favorite food')"""





# rsplit() - Splits the string at the specified separator, and returns a list
"""variable30 = "Biriyani,Fuchka, Pizza"
print(variable30.rsplit(",")) # Output -> ['Biriyani', 'Fuchka', ' Pizza']"""

# Another Example
"""variable31 = "Arijit & Chitrajyoti"
print(variable31.rsplit("&"))""" # Output -> ['Arijit ', ' Chitrajyoti']





# rstrip() - Returns a right trim version of the string
# *** Note: The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
"""variable31 = "      Biriyani    "
print(variable31.rstrip(), "is my favorite food")"""  # Output ->       Biriyani is my favorite food **[Returns a right trim version of the string]

# Another example
"""variable32 = "Fuchka\",@*#$%"
print(variable32.rstrip("~`@#$%^&*()_+-=/\'\"<>?,{}[]|"))"""    # Output - Fuchka




# split() - Splits the string at the specified separator, and returns a list
"""
***Note: 
1) The split() method splits a string into a list.
2) You can specify the separator, default separator is any whitespace.
"""
"""variable33 = "Welcome to the computer world."
print(variable33.split())""" # Output -> ['Welcome', 'to', 'the', 'computer', 'world.']    ** Because default separator is any whitespace.

#Another Example
"""variable34 = "Sayani, Sourav & Arijit, Nokia"
print(variable34.split("&"))"""  # Output -> ['Sayani, Sourav ', ' Arijit, Nokia']     ** Because we have already specified the separator here




# splitlines() - Splits the string at line breaks and returns a list
# *** Note: The splitlines() method splits a string into a list. The splitting is done at line breaks.
"""variable35 = "Sayani I love you.\n You are the precious gift of my life"
print(variable35.splitlines())"""     # Output -> ['Sayani I love you.', ' You are the precious gift of my life']



# startswith()   - Returns true if the string starts with the specified value
"""variable36 = "Sayani, I love you"
print(variable36.startswith("Sayani"))"""



# strip() - Returns a trimmed version of the string
""" **** Note: The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) 
characters (space is the default leading character to remove)"""
"""variable37 = "       Computer     "
print("Welcome to the world of",variable37.strip())"""    # Output -> Welcome to the world of Computer



# swapcase() - Swaps cases, lower case becomes upper case and vice versa
"""
The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
If the word contains a number or a symbol, the first letter after that will be converted to upper case."""

"""variable38 = "Sayani, welcome to my world"
print(variable38.title())  # Output -> Sayani, Welcome To My World"""


# zfill() - Fills the string with a specified number of 0 values at the beginning"""
"""
Note: The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

If the value of the len parameter is less than the length of the string, no filling is done."""

variable39 = "54"
print(variable39.zfill(3)) # Output -> 054




