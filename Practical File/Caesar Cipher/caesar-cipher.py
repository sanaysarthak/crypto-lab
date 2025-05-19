print("\nCaesar Cipher Encryption & Decryption Tool:-") 
ch = 1

while (ch != 0): 
    ch = int(input("\nEnter 1 to Encrypt. \nEnter 2 to Decrypt. \nEnter 0 to Exit. \nEnter choice: ")) 
    
    match ch: 
        case 1: 
            print("\nEncrypting Caesar Cipher!\n") 
            plain_text = str(input("Enter plain text: ")) 
            key = int(input("Enter key: ")) 
            cipher_text = "" 

            for i in range(0, len(plain_text)): 
                char = plain_text[i] 

                if char == chr(32): 
                    cipher_text += char 
                    continue 

                elif (char.isupper()): 
                    cipher_text += chr((ord(char) + key - 65) % 26 + 65) 

                elif (char.islower()): 
                    cipher_text += chr((ord(char) + key - 97) % 26 + 97) 

                else: 
                    cipher_text += char 

            print("Plain Text:  ", plain_text) 
            print("Cipher Text: ", cipher_text, "\n") 

        case 2: 
            print("\nDecrypting Caesar Cipher!\n") 
            cipher_text = str(input("Enter cipher text: ")) 
            key = int(input("Enter key: ")) 
            plain_text = "" 

            for i in range(0, len(cipher_text)): 
                char = cipher_text[i] 

                if char == chr(32): 
                    plain_text += char 
                    continue 

                elif (char.isupper()): 
                    plain_text += chr((ord(char) - key - 65) % 26 + 65) 

                elif (char.islower()): 
                    plain_text += chr((ord(char) - key - 97) % 26 + 97) 

                else: 
                    plain_text += char 

            print("Cipher Text: ", cipher_text) 
            print("Plain Text:  ", plain_text, "\n") 

        case 0: 
            print("\nProgram exited successfully!") 

        case _: 
            print("\nEnter correct choice!\n")
