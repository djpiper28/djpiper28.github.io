def inchToCM(inches):
	return inches/2.541
def CMToInch(CMs):
	return CMs*2.451
def CMToMetric(metricUnit, CMs):
	CMs = CMs.lower()
	if(metricUnit=='m'):
		return CMs/100
	if(metricUnit=='km'):
		return CMs/100000
	if(metricUnit=='mm'):
		return CMs*10
def bitsToX(x,bits):
	x = x.lower
	bitByteConstant = 8
	if(x=='bytes'||x=='b'):
		return bits*8
	if(x=='kb'||x=='kilo bytes'):
		return bits*bitByteConstant*1000
	if(x=='mb'||x=='mega bytes'):
		return bits*bitByteConstant*1000000
	if(x=='gb'||x=='giga bytes'):
		return bits*bitByteConstant*1000000000
	if(x=='tb'||x=='terra bytes'||x=='tera bytes'):
		return bits*bitByteConstant*1000000000000
def celciusToKelvin(C):
	return c-273.15
#To save time in python scripts by converting units quicker