# Code in Python to implement just the encryption part of Caesar Cipher algorithm

plain_text = str(input("Enter plain text: "))
key = int(input("Enter key: "))
cipher_text = ""

for i in range(0, len(plain_text)):
    char = plain_text[i]

    # to add blank space
    if char == chr(32):
        cipher_text += char
        continue

    # for upper-case characters
    if (char.isupper()):
        cipher_text += chr((ord(char) + key-65) % 26 + 65)

    # for lower-case characters
    if (char.islower()):
        cipher_text += chr((ord(char) + key-97) % 26 + 97)

print("Plain Text:  ", plain_text)
print("Cipher Text: ", cipher_text)
