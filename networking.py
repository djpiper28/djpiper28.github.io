import socket
import time
import _thread
import subprocess
s = socket.socket()  
def encodeTheText(text):
	return text.encode()
def decodeTheText(text):
	return text.decode()
def bindToHost(host, port):
	s.bind((host, port))
def getHostName():
	return socket.gethostname()
def listen():
	s.listen(5)
def acceptConnection():
	c, addr = s.accept()
	#Probably best to run this in your python script enless this code is in the same script
def sendText(text):
	c.send(text)
	#text must be encoded before sending
def recieve():
	return c.recv(1024).decode()
def clear():
    subprocess.call('cls', shell=True)
def null():
	return None
def connect(host, port):
	s.connect((host,port));