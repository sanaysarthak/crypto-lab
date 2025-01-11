# Program in Python to implement Caesar Cipher cryptography (both encryption and decryption)

def encrypt(plain_text, key):
    cipher_text = ""

    for char in plain_text:

        # to add blank space
        if char == ' ':
            cipher_text += char
            continue

        # for upper-case characters
        elif char.isupper():
            cipher_text += chr((ord(char) + key - 65) % 26 + 65)

        # for lower-case characters
        elif char.islower():
            cipher_text += chr((ord(char) + key - 97) % 26 + 97)

        # special characters remains unchanged
        else:
            cipher_text += char

    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""

    for char in cipher_text:
        # to add blank space
        if char == ' ':
            plain_text += char
            continue

        # for upper-case characters
        elif char.isupper():
            plain_text += chr((ord(char) - key - 65) % 26 + 65)

        # for lower-case characters
        elif char.islower():
            plain_text += chr((ord(char) - key - 97) % 26 + 97)

        # special characters remains unchanged
        else:
            plain_text += char

    return plain_text


def main():
    print("\nCaesar Cipher Encryption & Decryption Tool:-")
    while True:
        ch = int(input("\nEnter 1 to Encrypt. \nEnter 2 to Decrypt. \nEnter 0 to Exit. \nEnter choice: "))
        
        if ch == 1:
            print("\nEncrypting Caesar Cipher!\n")
            plain_text = input("Enter plain text: ")
            key = int(input("Enter key: "))
            cipher_text = encrypt(plain_text, key)
            print("Plain Text:  ", plain_text)
            print("Cipher Text: ", cipher_text, "\n")

        elif ch == 2:
            print("\nDecrypting Caesar Cipher!\n")
            cipher_text = input("Enter cipher text: ")
            key = int(input("Enter key: "))
            plain_text = decrypt(cipher_text, key)
            print("Cipher Text: ", cipher_text)
            print("Plain Text:  ", plain_text)

        elif ch == 0:
            print("\nProgram exited successfully!")
            break

        else:
            print("\nEnter correct choice!\n")


if __name__ == "__main__":
    main()
