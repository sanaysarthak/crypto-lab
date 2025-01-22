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

# print(matrix)

# Displaying the 5*5 matrix
print("\n+---+---+---+---+---+")
for row in matrix:
	row_string = "|"
	for num in row:
		row_string += f" {num} " + "|"
	print(row_string)
	print("+---+---+---+---+---+")

# Checking and appending the filler word ('X') as per need in between and at the end of plain_text
i = 0
while i < len(plain_text):
	substring = plain_text[i:i+2]
	if (substring[0] == substring[1]):
		first_half = plain_text[:i+1]
		first_half += "X"
		second_half = plain_text[i+1:]
		plain_text = first_half + second_half
	i += 2

	if (i+2 == len(plain_text)):
		continue

	if (i+1 == len(plain_text)):
		plain_text += "X"
		break

print("\n", plain_text)
	

# Encryption process:-
# Split the plain-text in pairs and check which rule to apply and encrypt accordingly
# Rules are: (same column, same row, different row & column -> rectangular rule)