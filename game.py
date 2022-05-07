import random 
def gamewin(computer, you):
	if computer == you:
		return None
	elif computer == 'S' :
		if you == 'W':
			return False
		elif you == 'G':
			return True
	elif computer == 'W' :
		if you == 'G':
			return False
		elif you == 'S':
			return True
	elif computer == 'G' :
		if you == 'S':
			return False
		elif you == 'W':
			return True

print("Computer's Turn: Snake(S) Water(W) or Gun(G) ?")
randomno = random.randint(1,3)
if randomno == 1:
	computer = 'S'
elif randomno == 2:
	computer = 'W'
elif randomno == 3:
	computer = 'G'

you=(input("Your Turn: Snake(S) Water(W) or Gun(G) ?"))
a=gamewin(computer, you)
print(f"computer choose {computer}")
print(f"you choose {you}")

if a == None:
	print("The Game is a Tie!")
elif a:
	print("You Win!")
else:
	print("You Loose!")
 
 