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
	
	
#Arithmetic Functions
def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	diff = d - b
	if diff < 0:
		diff *= -1
	return diff
	
def divide(w, p):
	return w / float(p)
	
def remainder(w, p):
	return w % p

def power(x, e):
	answer = 1
	for i in range(e):
		answer *= x
	return answer

def power2(x, e):
	return x ** e
	
def calculate(a, b, c, d, e):
	return (a + b / d - e) * c
	
def ratio(al, fred):
	if al > fred:
		return al / fred
	else:
		return fred / al
		
def pythagoras(a, b):
	return(a**2 + b**2)**(.5)

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "test abs_diff(10, 5): ", abs_diff(10, 5)
	print "test abs_diff(5, 10): ", abs_diff(5, 10)
	print "test divide(10, 2): ", divide(10, 2)
	print "test divide(2, 10): ", divide(2, 10)
	print "test remainder(40, 19): ", remainder(40, 19)
	print "test remainder(126, 19): ", remainder(126, 19)
	print "test remainder(133, 19): ", remainder(133, 19)
	print "test power(2, 3): ", power(2, 3)
	print "test calculate(1, 2, 3, 4, 5): ", calculate(1, 2, 3, 4, 5)
	print "test ratio(3.2, 7.8): ", ratio(3.2, 7.8)
	print "test pythagoras(3, 4): ", pythagoras(3, 4)
	print "test pythagoras 2(35, 67): ", pythagoras(35, 67)
	
	
def reverse(zack):
	return not zack
	
def band(a, b):
	if a==True and b==True: 
		return True
	else:
		return False
		
def band2(a, b):
	return a and b
	
def bor(a, b):
	if a==True or b==True:
		return True
	else:
	return False	
	
"""def bor(a, b):
	return a or b"""
	
def main_boolean():
	print "test reverse(True): ", reverse(True)
	print "test reverse(False): ", reverse(False)
	print "test band(True, True): ", band(True, True)
	print "test band2(True, True): ", band2(True, True)
	print "test bor(True, False): ", bor(True, False)
	print "test bor(True, True): ", bor(True, True)
	print "test bor(False, False): ", bor(False, False)
	
def main():
	main_function()
	main_arithmetic()
	main_boolean()
	
main()

