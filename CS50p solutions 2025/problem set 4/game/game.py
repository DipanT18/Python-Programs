import random

level = 0
while True:
    try:
        level=int(input("Level: ").strip())
        if(level<0):
            raise ValueError
        break
    except ValueError:
        pass
guessingNumber=random.randint(0,level)

while True:
    try:
        guessedNumber=int(input("Guess: ").strip())
        if(guessedNumber==guessingNumber):
            print("Just right!")
            break
        if(guessedNumber>guessingNumber):
            print("Too large!")
        if(guessedNumber<guessingNumber):
            print("Too small!")
    except ValueError:
        pass

