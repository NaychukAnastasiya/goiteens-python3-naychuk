import random

print("Введіть число від 1 до 10") 
inputed_val = int(input())
number = random.randrange(0,11)
if inputed_val==number:
    print("You win!")
else:
     print("You lose, the right number is: ",number )