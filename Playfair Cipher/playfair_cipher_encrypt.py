# Program in Python to implement encryption using the Playfair Cipher

# Taking user input
plain_text = str(input("\nEnter plain-text: "))
keyword = str(input("Enter keyword: "))

# Converting the input text into upper-case and replace I with J 
plain_text = plain_text.upper()
keyword = keyword.upper()
plain_text = plain_text.replace('J', 'I')
plain_text = plain_text.replace(" ", "") # to remove all blank-spaces

# Creating the 5x5 matrix based on the keyword
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

# print("\n", plain_text)
	


# Encryption process:-
# Split the plain-text in pairs and check which rule to apply and encrypt accordingly
# Rules are: (same column, same row, different row & column -> rectangular replacement rule)


# Encryption process:-

i = 0
cipher_text = ""

while i < len(plain_text):
	# getting pair of characters on each iteration
    char1 = plain_text[i]
    char2 = plain_text[i+1]
    
    row1, col1, row2, col2 = -1, -1, -1, -1 # intializing positions in the matrix

    # loop to find position of the characters
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char1:
                row1, col1 = r, c
            if matrix[r][c] == char2:
                row2, col2 = r, c

    # Applying different rules
    
    # Same row rule            
    if row1 == row2:
        cipher_text += matrix[row1][(col1 + 1) % 5]
        cipher_text += matrix[row2][(col2 + 1) % 5]

    # Same column rule    
    elif col1 == col2:
        cipher_text += matrix[(row1 + 1) % 5][col1]
        cipher_text += matrix[(row2 + 1) % 5][col2]
    
    # Different row and column rule
    else:
        cipher_text += matrix[row1][col2]
        cipher_text += matrix[row2][col1]
    
    i += 2

print("\nPlain Text:\t", plain_text)
print("Cipher Text:\t", cipher_text, "\n")
