import random
number = random.randint(1,9)
chanceCount = 0
while (chanceCount < 5):
      intoString = int (input("enter the number between 1-9: "))
      if (intoString > number):
            print("Your guess is too large")
      elif (intoString == number):
            print("Congratulation you have guess it correct")
      else:
            print("Your number guess is to less")
      chanceCount = chanceCount + 1
if (chanceCount > 5):
      print("You are out of chances")