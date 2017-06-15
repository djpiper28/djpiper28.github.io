def squareRoot(number):
	return sqrt(number)
def toThePowerOf(base, exponent):
	return base**exponent
def testIfSquare(number):
	if(squareRoot(number)%1==0):
		return True
	else:
		return False
def testIsPrime(number):
	if(number%2==0):
		return False
	else:
		i=0;
		while(i<=9999 and i<=number):
			if(number%i==0):
				return True
			else:
		return False
def isEven(number):
	if(number%2==0):
		return True
	else:
		return False
def isDivisibleByX(number, X):
	if(number%x==0):
		return True
	else:
		return False
def quadraticFormulaOne(a,b,c):
	quad = (-b + squareRoot((b**2 - 4*a*c)))/2a
	return quad
def quadraticFormulaTwo(a,b,c):
	quad = (-b - squareRoot((b**2 - 4*a*c)))/2a
	return quad
def pythagoras(a,b):
	return squareRoot(a**2 + b**2)
def Tau():
	return Math.pi*2