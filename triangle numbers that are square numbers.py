import math
x = 1
i = 1
def isSquare(int):
	if(math.sqrt(int)%1==0):
		return True
	else:
		return False
while(1):
	if((isSquare(x))==True):
		print(x)
	else:
		x=x
	i = i + 1
	x = x + i