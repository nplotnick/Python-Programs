#Program to demonstrate the IF statement in Python
#N. Plotnick 1/20/16
#While loop allows user to keep guessing until they are correct.
print "This program will demonstrate how to use an IF statement in Python."
print "Please pick a number from 1-20"
#initialize the variables
guess=100
i=10
while guess != i:
	guess = input ("Enter a number from 1-20   ")
	if guess==i:
		print "You got it right!"
	elif guess > i:
		print "Your guess is too high, try again!"
	elif guess < i:
		print "Your guess is too low, try again!"
