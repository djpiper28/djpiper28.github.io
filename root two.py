from decimal import *
getcontext().prec = 1000000
x = 1
file  = open("C:\\Users\\dp\\Desktop\\djpiper28.github.io\\djpiper28.github.io\\roottwo.txt", "r+")
x = float(file.read())
while(1):
	x = ((Decimal(x)/Decimal(2))+(Decimal(2)/(Decimal(2)*Decimal(x))))
	print(x)
	file.write(str(x)) 
file.close() 
