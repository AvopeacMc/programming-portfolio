# Band Name Generator
import random


titles = ['gigantic', 'sour', 'steamy', 'gross', 'stupid',
          'ironic', 'greasy', 'tangy', 'smelly', 'small',
          'inventive', 'spherical', 'spiritual', 'green',
          'blue', 'pot bellied', 'pickled', 'prickly']
          
adjs = ['tiny', 'fat', 'shiny', 'electric', 'fluffy', 'bright',
        'corrupt', 'agressive', 'alarming', 'amazing', 'magical',
        'courageous', 'fierce', 'colorless', 'red', 'thoughtless',
        'smart', 'delerious', 'fabulous', 'fergaliscius', 'dangerous']
        
plural_nouns = ['apples', 'oranges', 'kiwis', 'clementines',
                'wildabeasts', 'mamoths', 'rabbits', 'sloths',
                'spices', 'eggs', 'herbs', 'pony tails', 'bears',
                'unicorns', 'kermits', 'signs', 'indians', 'cowboys']
                
def title():
	''' This function chooses a random title for the name '''
	return random.choice(titles)
	
def adj():
	''' This function chooses a random adj for the band '''
	return random.choice(adjs)
	
def plural_noun():
	return random.choise(plural_nouns)
	
def main():
	while True:
		name = raw_input("Enter your name: ")
		if name == "q":
			break
		random.seed(name)
		print title(), name, "and the", adj(), plural_noun()
		
main()