import random
def guess():
    number = random.randint(1,100)
    attempts = 0
    while True :
      guess = int(input("Enter your guess(1-100)"))
      attempts += 1
      if guess < number :
        print("Too low")
      elif guess > number :
        print("Too high")
      else:
        print("Matched")
        print("You have guessed it in",attempts,"attempts")
        break

guess()