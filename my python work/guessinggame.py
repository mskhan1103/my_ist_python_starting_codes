#Guessing game.
guess=int(input("Guess any  no .............."))
import random
randomno=random.randint(1,50)
counter=1
while  randomno!=guess:
 if randomno>guess:
  print("Guess higher ...........")

 else:
  print("guess lower ...........")

 guess=int(input("guess again ......"))
 counter +=1
else :
  print(f"You have guess the right no .....in {counter}")
 
