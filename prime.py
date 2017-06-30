x = 2
while(1):
	i = x - 1
	isNotPrime = 0
	while(i>1):
		if(x%i==0):
			isNotPrime = 1
			break
		i = i - 1
	if(isNotPrime==0):
		print(x," is prime")
	x = x + 1