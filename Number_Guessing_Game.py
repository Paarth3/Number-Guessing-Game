import random
randomNumber = random.randint(1,9)
chance = int(5)
gameValid = "true"

while chance>0:
    x=int(input("Enter your guess: "))
    if(x > randomNumber):
        chance = chance - 1
        print("Guess a Little lower than "+str(x))
        print("Chances Left "+str(chance))
    elif(x<randomNumber):
        chance = chance - 1
        print("Guess a Little higher than "+str(x))
        print("Chances Left"+str(chance))
    elif(chance == 0):
        print("You Lost")
    else:
        print("You Won")
        