#pig latin translator
while
	word = raw_input("Enter Word to be Translated: "

	vowels = 'aeiouyAEIOUY'

	vpos = 0

	for i in range(len(word)):
		if word[i] in vowels:
			vpos = i
			break
	
	print word[vpos:] + word[:vpos] + "ay"