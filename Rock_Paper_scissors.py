# Rock Paper Scissors game
import random
def game(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
         if you == 's':
             return False
         elif you == 'p':
             return True
    elif comp == 'p':
         if you == 'r':
             return False
         elif you == 's':
             return True
    elif comp == 's':
         if you == 'p':
             return False
         elif you == 'r':
             return True

print("Computer turn: Rock(r) Paper(p) or Scissors(s)?")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you =  input("Your turn: Rock(r) Paper(p) or Scissors(s)?")

a = game(comp , you)
if a == None:
    print("The game is a tie!")
elif a == True:
    print("You win!")
else:
    print("You lose!")