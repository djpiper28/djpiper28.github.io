def textToCharacters(character, text):
	character = len(text)*'character'
	return character
def length(text):
	return len(text)
def isNotNull(text):
	if(text!=None):
		return True
	else:
		return False
def hashText(text):
	return hash(text),len(text)
def toLowerCase(text):
	return text.lower()
def toUpperCase(text):
	return text.upper()
def toString(text):
	return str(text)
def encodeText(text):
	return text.encode()
def decodeText(text):
	return text.decode()
def onlyHasLetters(text):
	return text.isAlpha()