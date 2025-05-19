# Program in Python to implement decryption using the Playfair Cipher

# Taking user input
cipher_text = str(input("\nEnter cipher-text: "))
keyword = str(input("Enter keyword: "))

# Converting the input text into upper-case
cipher_text = cipher_text.upper()
keyword = keyword.upper()
cipher_text = cipher_text.replace(" ", "") # to remove all blank-spaces

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

# Displaying the 5*5 matrix
print("\n+---+---+---+---+---+")
for row in matrix:
    row_string = "|"
    for num in row:
        row_string += f" {num} " + "|"
    print(row_string)
    print("+---+---+---+---+---+")

# Decryption process:
# Split the cipher-text in pairs and check which rule to apply and decrypt accordingly
# Rules are: (same column, same row, different row & column -> rectangular replacement rule)

i = 0
plain_text = ""

while i < len(cipher_text):
    # getting pair of characters on each iteration
    char1 = cipher_text[i]
    char2 = cipher_text[i+1]
    
    row1, col1, row2, col2 = -1, -1, -1, -1 # initializing positions in the matrix

    # loop to find position of the characters
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char1:
                row1, col1 = r, c
            if matrix[r][c] == char2:
                row2, col2 = r, c

    # Applying different rules - reverse of encryption
    
    # Same row rule - shift left instead of right           
    if row1 == row2:
        plain_text += matrix[row1][(col1 - 1) % 5]
        plain_text += matrix[row2][(col2 - 1) % 5]

    # Same column rule - shift up instead of down   
    elif col1 == col2:
        plain_text += matrix[(row1 - 1) % 5][col1]
        plain_text += matrix[(row2 - 1) % 5][col2]
    
    # Different row and column rule - same as encryption but reversed positions
    else:
        plain_text += matrix[row1][col2]
        plain_text += matrix[row2][col1]
    
    i += 2

# Note: The decryption won't remove 'X' fillers added during encryption

print("\nCipher Text:\t", cipher_text)
print("Plain Text:\t", plain_text, "\n")