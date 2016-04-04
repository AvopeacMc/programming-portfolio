#number guesser
import time			
			
def show_instructions():
	print 'Pick a number between 1 and 1000 and I will try to guess it.'
	print 'I can do this in no more than 10 guesses.'
	print ' '
	print 'After each guess, enter: '
	print '-1 - if I guessed too high'
	print '0  - if I got it right'
	print '1  - if I guessed too low'
	
def take_guess():
	print ' '
	time.sleep(3)
	tries = 0
	min = 1
	max = 1000
	guess = (min + max) / 2
	print 'my guess is ' + str(guess) + '.'
	guess1 = raw_input ('Please enter -1, 0, or 1: ')
	if guess1 == '0':
		print 'I got it right'
	elif guess1 == '-1':
		print 'my guess is ' + str(guess / 2) + '.'
		max = guess
		guess2 = raw_input ('Please enter -1, 0, or 1: ')
		if guess2 == '0':
			print 'I got it right'
		elif guess2 == '-1':
			print 'my guess is ' + str(guess / 2) + '.'
			guess3 = raw_input ('Please enter -1, 0, or 1: ')
		elif guess2 == '1':
			print 'my guess is ' +str(guess + (guess / 2))
			guess3 = raw_input ('Please enter -1, 0, or 1: ')
	elif guess1 == '1':
		print 'my guess is ' +str(guess + (guess / 2))
		guess2 = raw_input ('Please enter -1, 0, or 1: ')
		if guess2 == '0':
			print 'I got it right'
		elif guess2 == '-1':
			print 'my guess is ' + str(guess + guess + guess / 2) + '.'
			guess3 = raw_input ('Please enter -1, 0, or 1: ')
		elif guess2 == '1':
			print 'my guess is ' +str(1000)
			guess3 = raw_input ('Please enter -1, 0, or 1: ')
	
	
				
	
def main():
	show_instructions()
	take_guess()
	
	
main()