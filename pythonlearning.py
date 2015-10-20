#python learning exercises

#Functions
def echo(thing):
	return thing
	
def swap(x, y):
	return y, x
		
def main_function():
	print "test echo('marco'): ",echo('marco')
	print "test echo('shut up'): ",echo('no you shut up')
	print "test swap('Bob', 'Bill'): ",swap('Bob', 'Bill')
	
	
#Arithmetic Expressions
def reverse(x):
	return -x
	
def plus(x, y):     #adds two integers
	return x + y
	
def diff(x, y):     #subtracts two integers
	return x - y

def abs_diff(x, y):     #finds the difference between two integers
	return abs( x )- abs( y )
	
def divide(x, y):     #divides two integers
	return x / y
	
def remainder(x, y):     #finds the remainder of two integers
	retiurn
	
def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "test plus(6, 4): ", plus(6, 4)
	print "test diff(6, 4): ", diff(6,4)
	print "test abs_diff(6, 12): ", abs_diff(6, 12)
	print "test divide(16, 2): ", divide(16, 2)
	
def main():
	main_function()
	main_arithmetic()
	
main()

