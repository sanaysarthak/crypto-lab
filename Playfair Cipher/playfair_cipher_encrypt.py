# Program in Python to implement encryption using the Playfair Cipher

# Take user input
plain_text = str(input("Enter plain-text: "))
keyword = str(input("Enter keyword: "))

# Convert the input text into upper-case and replace I with J 
plain_text = plain_text.upper()
keyword = keyword.upper()
plain_text = plain_text.replace('J', 'I')
plain_text = plain_text.replace(" ", "") # remove all blank-spaces

# Create the 5x5 matrix based on the keyword
matrix = [[], [], [], [], []] # empty list

# Note: we are omitting j completely for implementation purposes
used_char = []
alphabets = [] # ['A', 'B', 'C', ... , 'Z']
for i in range(65, 91):
	if (chr(i) == 'J'):
		continue
	else:
		alphabets.append(chr(i))

# Start filling in the data from the keyword into the matrix
i, j = 0, 0

for char in keyword:
	if (j == 5):
		j = 0
		i += 1
	
	if (char in used_char):
		continue

	if (char == 'J'):
		matrix[i].insert(j, char)
		used_char.append('I')
		j += 1

	else:
		matrix[i].insert(j, char)
		used_char.append(char)
		j += 1
	

for char in alphabets:
	if (j == 5):
		j = 0
		i += 1

	if (char in used_char):
		continue

	if (char == 'J'):
		matrix[i].insert(j, char)
		used_char.append('I')
		j += 1

	else:
		matrix[i].insert(j, char)
		used_char.append(char)
		j += 1

print(matrix)



# Encryption Process (Splitting -> Add Filler if needed -> Encrypt according to rules)

# Check if adding filler is needed or not
i = 0
# while i < len(plain_text):
	

# Split the plain-text in pairs and also implement both rules for filler word (repetition and singleton at end)
