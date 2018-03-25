


#After CTs are finally over, Arnold is bored with life. He tasks you, the future Python master, to write him a number guessing game because that's all he likes.

#The program picks a random number from 1 to 100. The player keeps guessing as long as their guess is wrong **and** they have guessed less than 7 times. If their guess is higher than the number, print "Too high". If their guess is lower than the number, print "Too low". When they guess the correct number, the player wins. If they hit 7 guesses, the player loses.

import random
guess_number = random.randint(0,100)

print("I am thinking of a whole number between 1 and 100. You have 7 guesses.")

Guess_1 = int(input("Guess 1: Choose a number!"))

if Guess_1 < 0:
    print("That's not between 1 and 100! Guess again!")
elif Guess_1 > 100:
    print("That's not between 1 and 100! Guess again!")
else:
    if Guess_1 == guess_number:
        print("You guessed it! What are the odds??")
        exit()
    if Guess_1 > guess_number:
        print("Too high!")
    if Guess_1 < guess_number:
        print("Too low!")


Guess_2 = int(input("Guess 2: Choose a number!"))

if Guess_2 < 0:
    print("That's not between 1 and 100! Guess again!")
elif Guess_2 > 100:
    print("That's not between 1 and 100! Guess again!")
else:
    if Guess_2 == guess_number:
        print("You guessed it! What are the odds??")
        exit()
    if Guess_2 > guess_number:
        print("Too high!")
    if Guess_2 < guess_number:
        print("Too low!")


Guess_3 = int(input("Guess 3: Choose a number!"))

if Guess_3 < 0:
    print("That's not between 1 and 100! Guess again!")
elif Guess_3 > 100:
    print("That's not between 1 and 100! Guess again!")
else:
    if Guess_3 == guess_number:
        print("You guessed it! What are the odds??")
        exit()
    if Guess_3 > guess_number:
        print("Too high!")
    if Guess_3 < guess_number:
        print("Too low!")


Guess_4 = int(input("Guess 4: Choose a number!"))

if Guess_4 < 0:
    print("That's not between 1 and 100! Guess again!")
elif Guess_4 > 100:
    print("That's not between 1 and 100! Guess again!")
else:
    if Guess_4 == guess_number:
        print("You guessed it! What are the odds??")
        exit()
    if Guess_4 > guess_number:
        print("Too high!")
    if Guess_4 < guess_number:
        print("Too low!")


Guess_5 = int(input("Guess 5: Choose a number!"))

if Guess_5 < 0:
    print("That's not between 1 and 100! Guess again!")
elif Guess_5 > 100:
    print("That's not between 1 and 100! Guess again!")
else:
    if Guess_5 == guess_number:
        print("You guessed it! What are the odds??")
        exit()
    if Guess_5 > guess_number:
        print("Too high!")
    if Guess_5 < guess_number:
        print("Too low!")


Guess_6 = int(input("Guess 6: Choose a number!"))

if Guess_6 < 0:
    print("That's not between 1 and 100! Guess again!")
elif Guess_6 > 100:
    print("That's not between 1 and 100! Guess again!")
else:
    if Guess_6 == guess_number:
        print("You guessed it! What are the odds??")
        exit()
    if Guess_6 > guess_number:
        print("Too high!")
    if Guess_6 < guess_number:
        print("Too low!")


Guess_7 = int(input("Guess 7: Choose a number!"))

if Guess_7 < 0:
    print("That's not between 1 and 100! Guess again!")
elif Guess_7 > 100:
    print("That's not between 1 and 100! Guess again!")
else:
    if Guess_7 == guess_number:
        print("You guessed it! What are the odds??")
        exit()
    if Guess_7 > guess_number:
        print("Too high!")
    if Guess_7 < guess_number:
        print("Too low!")