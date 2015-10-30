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
	
def  xsame(b, g):
	return b == g
	
def xor(b, g):
	return b != g
	
def main_boolean():
	print "test reverse(True): ", reverse(True)
	print "test reverse(False): ", reverse(False)
	print "test band(True, True): ", band(True, True)
	print "test band2(True, True): ", band2(True, True)
	print "test bor(True, False): ", bor(True, False)
	print "test bor(True, True): ", bor(True, True)
	print "test bor(False, False): ", bor(False, False)
	print "test xsame(False, False): ", xsame(False, False)
	print "test xsame(True, True): ", xsame(True, True)
	print "test xsame(True, False): ", xsame(True, False)
	
	

def positive(x):
	if x > 0:
		return True
	else:
		return False
		
def bigger(x, y):
	if x > y:
		return True
	else:
		return False
		
def no_diff(j, u):
	if j == u:
		return True 
	else:
		return False
		
def not_same(f, i):
	return not f == i
	
def less_than(r, p):
	return r < p
	
def at_least_13(x):
	return x >= 13
	
def at_most_13(x):
	return x <= 13		
		
		
def main_boolean_numbers():
	print 'testing positive(29): ', positive(29)
	print 'testing positive(-29): ', positive(-29)
	print 'testing bigger(3, 2): ', bigger(3, 2)
	print 'testing bigger(2, 3): ', bigger(2, 3)
	print 'testing no_diff(2, 2): ', no_diff(2, 2)
	print 'testing no_diff(2, 4): ', no_diff(2, 4)
	print 'testing not_same(2, 2): ', not_same(2, 2)
	print 'testing not_same(2, 4): ', not_same(2, 4)
	print 'testing less_than(2, 8): ', less_than(2, 8)
	print 'testing less_than(8, 2): ', less_than(8, 2)
	print 'testing at_least_13(40): ', at_least_13(40)
	print 'testing at_least_13(13): ', at_least_13(13)
	print 'testing at_least_13(3): ', at_least_13(3)
	print 'testing at_most_13(40): ', at_most_13(40)
	print 'testing at_most_13(13): ', at_most_13(13)
	print 'testing at_most_13(3): ', at_most_13(3)
			
			
def biggest(ab, yb):
	if ab > yb:
		return ab
	else:
		return yb
		
def smallest(ab, yb):
	if ab < yb:
		return ab
	else:
		return yb
		
def letter_grade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"
		
def food_tax(sub, gro):
	if gro:
		return sub * .03
	else:
		return sub * .0725
		
def same(a, b, c):
	return a == b == c
	
def big3(get_right, allu, jw):
	if get_right >= allu and get_right >= jw:
		return get_right
	elif allu >= get_right and allu >= jw:
		return allu
	elif jw >= get_right and jw >= allu:
		return jw
	else:
		return 
		
def small_sum(a, b, c):
	if a < b and b < c:
		return a + b
	elif b < a and c < a:
		return b + c
	else:
		return a + c
		
def meat_loaf(onions, ketchup, garlic):
	if onions and garlic and not ketchup:
		return True
	elif onions and ketchup and not garlic:
		return True
	elif garlic and ketchup and not onions:
		return True
	else:
		return False
		
'''def big3reorder(a, b, c):
	big = big3(a, b, c)
	if a == big:
		small = smallest(b, c)
		if b == small:
			middle = c
		else:
			middle = b
	elif b == big:
		small = smallest(a, c)
		if a == small:
			middle = c
		else:
			middle = a
	elif c == big:
		small = smallest(a, b)
		if a == small:
			middle = b
		else:
			middle = a
	return big, middle, small
	
	
def big3reorder(a, b, c):
	x = [a, b, c]
	x.sort()
	x.reverse()
	return x[0], [], []'''
	
def big3reorder(a, b, c):
	if a == big3(a, b, c):
		return a, biggest(b, c), smallest(b, c)
	elif b == big3(a, b, c):
		return b, biggest(a, c), smallest(a, c)
	else:
		return c, biggest(a, b), smallest(a, b)
		
def positive_multiple(w, h):
	product = w * h
	if not positive(product):
		return product * -1
	else:
		return product
	
	
					
def main_conditionals():
	print 'testing biggest(500, 10): ', biggest(500, 10)
	print 'testing biggest(500, 1000): ', biggest(500, 1000)
	print 'testing smallest(500, 10): ', smallest(500, 10)
	print 'testing smallest(500, 1000): ', smallest(500, 1000)
	print 'testing letter_grade(90): ', letter_grade(90)
	print 'testing letter_grade(80): ', letter_grade(80)
	print 'testing letter_grade(70): ', letter_grade(70)
	print 'testing letter_grade(60): ', letter_grade(60)
	print 'testing letter_grade(55): ', letter_grade(55)
	print 'testing food_tax(12.45, True): ', food_tax(12.45, True)
	print 'testing food_tax(12.45, False): ', food_tax(12.45, False)
	print 'testing same(7, 7, 7): ', same(7, 7, 7)
	print 'testing same(7, 4, 5): ', same(7, 4, 5)
	print 'testing big3(3, 2, 1): ', big3(3, 2, 1)
	print 'testing big3(2, 3, 1): ', big3(2, 3, 1)
	print 'testing big3(1, 2, 3): ', big3(1, 2, 3)	
	print 'testing big3(3, 3, 1): ', big3(3, 3, 1)
	print 'testing big3(1, 3, 3): ', big3(1, 3, 3)
	print 'testing big3(3, 1, 3): ', big3(3, 1, 3)
	print 'testing small_sum(1, 2, 3): ', small_sum(1, 2, 3)
	print 'testing small_sum(3, 2, 1): ', small_sum(3, 2, 1)
	print 'testing meat_loaf(True, True, False): ', meat_loaf(True, True, False)
	print 'testign meat_loaf(true, False, False); ', meat_loaf(True, False, False)
	print 'testing meat_loaf(True, True, True): ', meat_loaf(True, True, True)
	print "test big3reorder(5, 8, 2): ", big3reorder(5, 8, 2)
	print 'testing positive_multiple(5, 7): ', positive_multiple(5, 7)
	print 'testing positive_multiple(-5, -7): ', positive_multiple(-5, -7)
	print 'testing positive_multiple(-5, 7): ', positive_multiple(-5, 7)
	
	
def total(x):
	t = 0
	for num in range(x):
		t += num
	return t
	
def total_slice(a, b):
	t = 0
	for num in range(a, b):
		t += num
	return t
	
def total_slice2(a, b):
	t = 0
	for num in range(smallest(a, b), biggest(a, b)):
		t += num
	return t
	
def total_odds(a, b):
	t = 0
	for num in range(a, b):
		if num % 2 == 1:
			t += num
	return t
	
def total_evens(a, b):
	t = 0
	for num in range(a, b):
		if num % 2 == 0:
			t += num
	return t
	
def total_7s(a, b):
	t = 0
	for num in range(a, b):
		if num % 7 == 0:
			t += num
	return t
	
def total_non7s(a, b):
	t = 0
	for num in range(a, b):
		if num % 7 != 0:
			t += num
	return t
	
def squares(x):
	ts = 0
	for num in range(x):
		ts += num**2
	return ts

	
	
def main_counted_loops():
	print 'testing total(5): ', total(5)
	print 'testing total(63): ', total(63)
	print 'testing total_slice(3, 8): ', total_slice(3, 8)
	print 'testing total_slice2(8, 3): ', total_slice2(8, 2)
	print 'testing total_odds(2, 10): ', total_odds(2, 10)
	print 'testing total_evens(2, 10): ', total_evens(2,10)
	print 'testing total_7s(2, 30): ', total_7s(2, 30)
	print 'testing total_non7s(2, 10): ', total_non7s(2, 10)
	print 'testing squares(5): ', squares(5)
	
	
def hello()
	return hello
	
	
def main_strings():

			
def main():
	main_function()
	main_arithmetic()
	main_boolean()
	main_boolean_numbers()
	main_conditionals()
	main_counted_loops()
	main_strings()
	
main()

