import random


def gameWin(comp, you):
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


print("Computer has chosen now you choose")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
you = input("Your turn : SNAKE (s),WATER (w) or GUN (g)?  ")
a = gameWin(comp, you)

print(f"COMPUTER chose {comp}")
print(f"YOU chose {you}")

if a == None:
    print("MATCH TIE !!")
elif a:
    print("YOU WIN !!!!!!!!!!!!!!!!!")
else:
    print("You LOSE")
