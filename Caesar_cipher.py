caesar_var, phrase = input("a shift number for the Caesar cipher, followed by '/' and then your phrase").split('/')
def caesar(phrase):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
	print ('\n')
	phrase = phrase.lower()
	break_at_space = phrase.split(" ")
	new_phrase = ' '
	for word in break_at_space:
		new_word = [ ]
		for letter in word:
			if letter in alphabet:
				spot = alphabet.index(letter)
				new_spot = spot + int(caesar_var)
				new_letter = alphabet[new_spot]
				new_word += new_letter
		FINAL = str.join('', (new_word))
		new_phrase += (" " + FINAL)
	new_phrase = str.join('', (new_phrase))
	return (new_phrase)
	
print ("Your new phrase is:" + caesar(phrase))
