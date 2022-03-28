Sourav_Sayani = 0
while(Sourav_Sayani<45):
    print(Sourav_Sayani)
    Sourav_Sayani = Sourav_Sayani + 1


Sourav_Sayani1 = 1
while Sourav_Sayani1 < 6:
  print(Sourav_Sayani1)
  if Sourav_Sayani1 == 3:
    break
  Sourav_Sayani1 += 1


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# With the else statement we can run a block of code once when the condition no longer is true
Sourav_Sayani2 = 1
while Sourav_Sayani2 < 6:
  print(Sourav_Sayani2)
  Sourav_Sayani2 += 1
else:
  print("i is no longer less than 6")




name = input("Enter Your name ")
age = int(input("enter Your age "))
score = 0
try1 = 0
while age >= 21:
    if try1< 1:
        print("You can perticipate in this exam")
        print("What is the full form of http? \n a) Hypertext Transfer Protocol b) Hypertext Transfer Protocol Secure")
        answer1 = input("Answer: ")
        if answer1 == "a" or answer1 == "A":
            print("Your answer 1 is Correct")
            score = score + 1
        else:
            print("You have enter a wrong answer")

        print("What is the full form of https? \n a) Hypertext Transfer Protocol b) Hypertext Transfer Protocol Secure")
        answer2 = input("Answer: ")
        if answer2 == "b" or answer2 == "B":
            print("Your answer 2 is Correct")
            score = score + 1
        else:
            print("You have enter a wrong answer")

        print("Your score is ", score)
        print("Name -", name, "Score:", score)
        try1 += 1
    else:
        break
else:
    print("You are not eligible for exam")