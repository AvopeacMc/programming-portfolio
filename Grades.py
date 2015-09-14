#grades

var = 1
while var == 1 :

	score = int(raw_input('Enter your score: '))
	if score > 100:
		print 'HOW DID YOU DO THAT'
	elif score >= 92:
		print 'A'
	elif score >= 89:
		print 'A-'
	elif score >= 87:
		print 'B+'
	elif score >= 83:
		print 'B'
	elif score >= 80:
		print'B-'
	else:
		print 'You Have Failed'