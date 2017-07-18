from decimal import *
getcontext().prec = 1000000
x = 1
while(1):
	x = ((Decimal(x)/Decimal(2))+(Decimal(2)/(Decimal(2)*Decimal(x))))
	print(x)