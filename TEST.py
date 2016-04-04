#TEST
import random
import time


def rand():
	r = random.randrange(1, 999)
	print r
		
def main():
	p = 0
	while p == 0:
		time.sleep(.3)
		rand()
	
	
main()

