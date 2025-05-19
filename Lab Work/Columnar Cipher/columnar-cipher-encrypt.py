# Program in Python to implement encryption using the Columnar Transposition Cipher
# Implemented the algorithm without removing the whitespaces.

# Taking user input
plain_text = str(input("\nEnter plain-text: "))
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

# Calculate number of rows needed
num_rows = (len(plain_text) // len(keyword)) + (1 if len(plain_text) % len(keyword) != 0 else 0)

# Create the matrix for columnar transposition
matrix = [['' for _ in range(len(keyword))] for _ in range(num_rows)]

# Fill the matrix with the plain text
index = 0
for i in range(num_rows):
    for j in range(len(keyword)):
        if index < len(plain_text):
            matrix[i][j] = plain_text[index]
            index += 1
        else:
            # Fill empty spaces with underscore
            matrix[i][j] = '_'

# Display the matrix
print("\n+---" + "---+---" * (len(keyword) - 1) + "---+")
# Print the keyword row
keyword_row = "|"
for char in keyword:
    keyword_row += f" {char} " + "|"
print(keyword_row)
print("+---" + "---+---" * (len(keyword) - 1) + "---+")

# Print the key order row
order_row = "|"
for order in key_order:
    order_row += f" {order} " + "|"
print(order_row)
print("+---" + "---+---" * (len(keyword) - 1) + "---+")

# Print the matrix with the plaintext
for row in matrix:
    row_string = "|"
    for char in row:
        row_string += f" {char} " + "|"
    print(row_string)
    print("+---" + "---+---" * (len(keyword) - 1) + "---+")

# Generate the cipher text by reading the columns in key order
cipher_text = ""
for col_num in range(1, len(keyword) + 1):  # From 1 to len(keyword)
    col_index = key_order.index(col_num)
    
    for row in matrix:
        cipher_text += row[col_index]

print("\nPrint Characters of column 1,2,3,...")
print("Encrypted Text:", cipher_text)