# snake gun water game
import random
def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
         if you == 'w':
             return False
         elif you == 'g':
             return True
    elif comp == 'w':
         if you == 'g':
             return False
         elif you == 's':
             return True
    elif comp == 'g':
         if you == 's':
             return False
         elif you == 'w':
             return True

print("Computer turn: Snake(s) Water(w) or Gung(G)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you =  input("Your turn: Snake(s) Water(w) or Gung(G)?")

a = game(comp , you)
if a == None:
    print("The game is a tie!")
elif a == True:
    print("You win!")
else:
    print("You lose!")