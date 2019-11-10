from random import randint

sn = randint(1,250)
print(sn)
tries = 0
GuessNum = int(input("Please choose a number between 1 and 250: "))
print(type(GuessNum))

if GuessNum < sn:
	print ("too small")
if GuessNum > sn:
	print ("too big")
if GuessNum == sn:
	print ("BINGO")
