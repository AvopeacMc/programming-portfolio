 # Decoder

def main():
	file_name = raw_input("Enter your file name: ")
	old_message = open(file_name)
	print 'Your old message said: '
	print old_message.read()
	
	message = raw_input("Enter your message: ")
	plain_message = open(file_name, 'w')
 	plain_message.write(message)
 	plain_message.close()
 	
 	
 	
 	 
main()