def create_matrix(keyword):
    keyword = keyword.upper()
    keyword = keyword.replace('J', 'I')

    matrix = [[], [], [], [], []]
    used_char = []
    alphabets = []  # ['A', 'B', 'C', ... , 'Z']
    for i in range(65, 91):
        if chr(i) == 'J':
            continue
        alphabets.append(chr(i))

    i, j = 0, 0
    for char in keyword:
        if j == 5:
            j = 0
            i += 1
        if char in used_char:
            continue
        if char == 'J':
            matrix[i].insert(j, char)
            used_char.append('I')
            j += 1
        else:
            matrix[i].insert(j, char)
            used_char.append(char)
            j += 1

    for char in alphabets:
        if j == 5:
            j = 0
            i += 1
        if char in used_char:
            continue
        if char == 'J':
            matrix[i].insert(j, char)
            used_char.append('I')
            j += 1
        else:
            matrix[i].insert(j, char)
            used_char.append(char)
            j += 1

    return matrix


def display_matrix(matrix):
    print("\n+---+---+---+---+---+")
    for row in matrix:
        row_string = "|"
        for num in row:
            row_string += f" {num} " + "|"
        print(row_string)
        print("+---+---+---+---+---+")


def prepare_text_encrypt(plain_text):
    plain_text = plain_text.upper().replace('J', 'I').replace(" ", "")

    i = 0
    while i < len(plain_text):
        substring = plain_text[i:i+2]
        if len(substring) == 2 and substring[0] == substring[1]:
            plain_text = plain_text[:i+1] + "X" + plain_text[i+1:]
        i += 2
        if i+1 == len(plain_text):
            plain_text += "X"
            break
    return plain_text


def encrypt_playfair(plain_text, keyword):
    matrix = create_matrix(keyword)
    display_matrix(matrix)

    plain_text = prepare_text_encrypt(plain_text)

    i = 0
    cipher_text = ""

    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = plain_text[i+1]

        row1 = col1 = row2 = col2 = -1
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == char1:
                    row1, col1 = r, c
                if matrix[r][c] == char2:
                    row2, col2 = r, c

        if row1 == row2:
            cipher_text += matrix[row1][(col1 + 1) % 5]
            cipher_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + 1) % 5][col1]
            cipher_text += matrix[(row2 + 1) % 5][col2]

        else:
            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]

        i += 2

    return plain_text, cipher_text


def decrypt_playfair(cipher_text, keyword):
    matrix = create_matrix(keyword)
    display_matrix(matrix)

    cipher_text = cipher_text.upper().replace(" ", "")

    i = 0
    plain_text = ""

    while i < len(cipher_text):
        char1 = cipher_text[i]
        char2 = cipher_text[i+1]

        row1 = col1 = row2 = col2 = -1
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == char1:
                    row1, col1 = r, c
                if matrix[r][c] == char2:
                    row2, col2 = r, c

        if row1 == row2:
            plain_text += matrix[row1][(col1 - 1) % 5]
            plain_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += matrix[(row1 - 1) % 5][col1]
            plain_text += matrix[(row2 - 1) % 5][col2]
        else:
            plain_text += matrix[row1][col2]
            plain_text += matrix[row2][col1]

        i += 2

    return plain_text


choice = None
while choice != 0:
    print("\nPlayfair Cipher Encryption & Decryption Tool:")
    print("Enter 1 to Encrypt.")
    print("Enter 2 to Decrypt.")
    print("Enter 0 to Exit.")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 0.")
        continue

    if choice == 1:
        print("\nEncrypting Playfair Cipher!")
        pt = input("Enter plain-text: ")
        key = input("Enter keyword: ")
        prepared, ct = encrypt_playfair(pt, key)
        print("\nPlain Text: \t", prepared)
        print("Cipher Text:\t", ct)
    elif choice == 2:
        print("\nDecrypting Playfair Cipher!")
        ct_input = input("Enter cipher-text: ")
        key = input("Enter keyword: ")
        pt_out = decrypt_playfair(ct_input, key)
        print("\nCipher Text:\t", ct_input.replace(' ', '').upper())
        print("Plain Text: \t", pt_out)
    elif choice == 0:
        print("\nProgram exited successfully!")
    else:
        print("\nEnter correct choice!")
