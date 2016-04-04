# encryption

def printdescription():
	print '''
This program encrypts and decrypts messages, using multiple encryption methods.
Input files must be in the same directory as this program.
Output files will be created in this same directory.
'''

def start_menu():
	print '''
Do you want to encrypt or decrypt?
(e)ncrypt
(d)ecrypt
(q)uit
'''
	option = raw_input("choose: ")
	while option != 'e' and option != 'd' and option != 'q':
		option = raw_input("choose:")
		
	return option

def methodmenu():
	print '''
Which method do you want to use?
(c)aesarian fixed offset
(p)seudo-random offset
(s)ubstitution cipher
'''
	option = raw_input('choose: ')
	while option != 'c' and option != 'p' and option != 's':
		option = raw_input('choose: ')
		
	return option
	
	
def Caesarian(fin, fout, encrypt_or_decrypt_choice, alphabet):
    # Determine the offset by generating a random number in the correct range.
    # This will be the same random number, if the password sent to random.seed is the same.
    offset = random.randrange(1,len(alphabet))
    if encrypt_or_decrypt_choice=='d':
        offset = -offset
    print "Using the secret offset of", offset

    # Read every line of the input file.
    for line1 in fin:
        # Alter each character of the line1, putting the result into line2.
        line2 = ""
        for c in line1:
            if c in alphabet:
                pos1 = alphabet.find(c)
                pos2 = (pos1+offset)%len(alphabet)
                line2 += alphabet[pos2]
        # Write each resulting line2 to the output file.
        fout.write(line2)
	
	
def main():
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.?! \t\n\r"
	printdescription()
	
	while True:
		choice = start_menu()
		if choice == 'p':
			break
		method_choice = methodmenu()
		print 'Enter an input file name: '
		source_file = raw_input()
		print 'Enter an output file name: '
		destination_file = raw_input()
		print 'Enter your password: '
		password = raw_input()
		try:
			fin = open(source_file, "rb")
		except:
			print "That file doesn't exist"
			continue
		fout = open(destination_file, "wb")	
		
		random.seed(password)
		
		
	
main()