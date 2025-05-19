# Program in python to implement Rail-Fence Decryption Algorithm with variable depth (given by user)
# Note: The program expects the cipher_text to have a whitespace after each rail
# Note: The program will return plain_text without spaces as per encryption algorithm

cipher_text = str(input("Enter Cipher-Text: "))
depth = int(input("Enter depth: "))

# Splitting the cipher_text based on spaces to get the rails
rail_strings = cipher_text.split()

# Calculate the length of the original plain text
plain_text_length = sum(len(rail) for rail in rail_strings)

# Create the rail matrix structure
rail_matrix = [[''] * plain_text_length for _ in range(depth)]

# Fill in the marker for valid positions in the matrix
index = 0
direction = 1  # 1 for down, -1 for up
row = 0

for col in range(plain_text_length):
    rail_matrix[row][col] = '*'  # Mark positions where characters should be
    
    if row == 0:
        direction = 1  # Going down
    elif row == depth - 1:
        direction = -1  # Going up
        
    row += direction

# Fill in the rail matrix with the characters from the cipher text
index = 0
for i in range(depth):
    rail_chars = rail_strings[i]
    for col in range(plain_text_length):
        if rail_matrix[i][col] == '*' and index < len(rail_chars):
            rail_matrix[i][col] = rail_chars[index]
            index += 1
    index = 0  # Reset index for next rail

# Read the original message from the rail matrix
plain_text = ""
row = 0
direction = 1

for col in range(plain_text_length):
    plain_text += rail_matrix[row][col]
    
    if row == 0:
        direction = 1
    elif row == depth - 1:
        direction = -1
        
    row += direction

print("Plain-Text:", plain_text)