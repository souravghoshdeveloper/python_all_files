"""num1 = input("Enter Num 1 ")
num2 = input("Enter num 2 ")

try:
    print("The sum of these two numbers is", int(num1) + int(num2))
except Exception as e:
    print(e)"""


"""Sourav = "Sayani, you are a blessing to me"
try:
  print(Sourav)
except:
  print("An exception occurred")"""


"""x=6
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")"""


"""try:
  print("Hi, This is Sourav")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")"""



"""try:
  print(y)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")"""


"""try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")"""


"""x=6
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")"""



"""try:
  f = open("sourav.txt")
  try:
    f.write("Hi")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")"""


#--------------------------------------------------------------------------------------------------------------
"""x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")"""




"""age = int(input("Enter your age? "))
if age < 18:
    raise Exception("You are not 18 years old")"""



"""x = 8.2

if not type(x) is int:
  raise TypeError("Only integers are allowed")"""