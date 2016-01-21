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
	high = 1000
	low = 1
	guess = (low + high) / 2
	print 'my guess is ' + str(guess) + '.'
	guessnum = raw_input ('Please enter -1, 0, or 1: ')
	if guessnum == '-1':
		print 'my guess is ' + str(guess / 2) + '.'
		high = str(guess / 2)
	elif guessnum == '0':
		print 'I got it right!'
	elif guessnum == '1':
		print 'my guess is ' +str(guess + (guess / 2)) + '.'
		
		
def main():
	show_instructions()
	time.sleep(2)
	take_guess