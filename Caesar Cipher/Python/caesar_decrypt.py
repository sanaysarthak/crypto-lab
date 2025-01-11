# Code in Python to implement just the decryption part of Caesar Cipher algorithm

cipher_text = str(input("Enter cipher text: "))
key = int(input("Enter key: "))
plain_text = ""

for i in range(0, len(cipher_text)):
    char = cipher_text[i]

    # to add blank space
    if char == chr(32):
        plain_text += char
        continue

    # for upper-case characters
    elif (char.isupper()):
        plain_text += chr((ord(char) - key-65) % 26 + 65)

    # for lower-case characters
    elif (char.islower()):
        plain_text += chr((ord(char) - key-97) % 26 + 97)

    # special characters remains unchanged
    else:
        plain_text += char

print("Cipher Text:	", cipher_text)
print("Plain Text:	", plain_text)
