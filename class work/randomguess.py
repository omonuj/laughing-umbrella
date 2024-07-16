import random

number = random.randint(1, 1000)

counter = 0

guess = 0

while guess != number: 
	guess = int(input("Guess a random number: "))
	if guess == number:
		print("congratulations, you got it")
	elif guess > number:
		print("Your guess is too high")
	elif guess < number:
		print("Your guess is too low")
	
	counter = counter + 1
