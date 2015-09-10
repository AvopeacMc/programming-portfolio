# learning python intrest calculator

amount = float(raw_input("Enter amount: "))
inrate = float(raw_input("Enter Intrest rate: "))
period = int(raw_input("Enter Period: "))
value = 0
year = 1
while year <= period:
	value = amount + (inrate * amount)
	print "year %d Rs. %.3f" % (year, value)
	amount = value
	year = year +1