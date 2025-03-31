# Program in Python to implement decryption using the Columnar Transposition Cipher

# Taking user input
cipher_text = str(input("\nEnter cipher-text: "))
keyword = str(input("Enter keyword: "))

# Converting the keyword to uppercase for consistency
keyword = keyword.upper()

# Create the key order based on alphabetical positions in the keyword
# For example, if keyword is "HACK", the order would be "3 1 2 4"
key_order = []
for i in range(len(keyword)):
    position = 1
    for j in range(len(keyword)):
        if keyword[j] < keyword[i] or (keyword[j] == keyword[i] and j < i):
            position += 1
    key_order.append(position)

print("\nOrder of Alphabets in", keyword, "=", "".join(map(str, key_order)))

# Calculate number of rows and columns
num_columns = len(keyword)
num_rows = (len(cipher_text) + num_columns - 1) // num_columns

# Calculate the number of characters in each column
col_lengths = [num_rows for _ in range(num_columns)]

# Adjust for columns that are shorter (if text length not divisible by key length)
remaining_chars = len(cipher_text) % num_columns
if remaining_chars > 0:
    # The first columns (by key order) get extra characters
    for i in range(1, num_columns + 1):
        col = key_order.index(i)
        if i > remaining_chars:
            col_lengths[col] = num_rows - 1

# Create the matrix for columnar transposition
matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]

# Fill the matrix column by column according to the key order
index = 0
for i in range(1, num_columns + 1):  # For each position in key order
    col = key_order.index(i)  # Get the column index
    
    for row in range(col_lengths[col]):
        if index < len(cipher_text):
            matrix[row][col] = cipher_text[index]
            index += 1

# Display the decryption matrix
print("\n+---" + "---+---" * (num_columns - 1) + "---+")
# Print the keyword row
keyword_row = "|"
for char in keyword:
    keyword_row += f" {char} " + "|"
print(keyword_row)
print("+---" + "---+---" * (num_columns - 1) + "---+")

# Print the key order row
order_row = "|"
for order in key_order:
    order_row += f" {order} " + "|"
print(order_row)
print("+---" + "---+---" * (num_columns - 1) + "---+")

# Print the matrix with the filled ciphertext
for row in matrix:
    row_string = "|"
    for char in row:
        row_string += f" {char} " + "|"
    print(row_string)
    print("+---" + "---+---" * (num_columns - 1) + "---+")

# Read the plain text row by row
plain_text = ""
for row in matrix:
    for char in row:
        plain_text += char

# Remove trailing underscores that might have been added during encryption
plain_text = plain_text.rstrip('_')

print("\nDecrypted Text:", plain_text)