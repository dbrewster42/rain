import random
def randInt(min = 0, max = 100):
	if min > max:
		print("You failed math class. Try again")
	else:
		if max < 0:	
			print("This function doesn't like your negativity. Come back when you are feeling more positive")
		else:
			num = random.random() * max 
			rand = round(num)
			while rand < min:
				rand += round(min/5)
			while rand > max:
				rand -= round(min/10)
				
			return rand

print(randInt())