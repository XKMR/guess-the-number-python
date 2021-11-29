import random
import os

x = 0
os.system('clear')
num = random.randint(0,100)
print ("GUESS THE NUMBER GAME!")
print ("I will choose a Number and you should guess it!")
input('Press Enter To Start!')
os.system("clear")
n = int(input('guess: '))
os.system("clear")

while n != num:
	if n < num:        
	 x=x+1
	 print (n,' ==> guess a bigger number  -    ',x,'  Guesse(s)')
	 n = int(input('guess: '))
	 os.system("clear")
	if n > num:      
	 x=x+1  
	 print (n,' ==> guess a smaller number  -    ',x,'  Guesse(s)')
	 n = int(input('guess: '))
	 os.system("clear")
os.system("clear")
x=x+1
print (n,' ==> NICE!    number was: ',num,'   -    with ',x,' guesse(s)')