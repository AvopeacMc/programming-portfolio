#pig latin translator

def pigify(word):
	vowels = 'aeiouyAEIOUY'
	vpos = 0
	for i in range(len(word)):
		if word[i] in vowels:
			vpos = i
			break
			
	return word[vpos:] + word[:vpos] + "ay"
	
	
def main():
	while True:
		word = raw_input("Enter a word to be translated: ")
		print pigify(word)