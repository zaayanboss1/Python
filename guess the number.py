import random
playing=True
number=str(random.randint(1,20))
print("i generated a number between 1 to 20 and you have to guess it")
print("the game ends when you get it correct")
while playing:
    guess=input("give me your best guess")
    if number==guess:
        print("you win the game")
        print("the number was",number)
        break
    else:
        print("your guess isn't quite right")