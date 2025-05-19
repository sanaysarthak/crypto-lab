print("\nRail Fence Cipher Encryption & Decryption Tool:-") 
ch = 1 

while ch != 0: 
    ch = int(input( 
        "\nEnter 1 to Encrypt. \n" 
        "Enter 2 to Decrypt. \n" 
        "Enter 0 to Exit. \n" 
        "Enter choice: " 
    )) 

    match ch: 
        case 1: 
            print("\nEncrypting Rail Fence Cipher!\n") 
            plain_text = input("Enter plain text: ") 
            depth = int(input("Enter depth: ")) 

            # remove all spaces 
            text = plain_text.replace(" ", "") 
            rails = [[] for _ in range(depth)] 
            row, direction = 0, 1 

            for char in text: 
                rails[row].append(char) 
                if row == 0: 
                    direction = 1 
                elif row == depth - 1: 
                    direction = -1 
                row += direction 

            cipher_text = "" 
            for rail in rails: 
                for char in rail: 
                    cipher_text += char 
                cipher_text += " " 

            print("Plain Text:  ", plain_text) 
            print("Cipher Text: ", cipher_text, "\n") 

        case 2: 
            print("\nDecrypting Rail Fence Cipher!\n") 
            cipher_text = input("Enter cipher text: ") 
            depth = int(input("Enter depth: ")) 

            rails_str = cipher_text.split() 
            length = sum(len(r) for r in rails_str) 

            # build rail matrix  
            matrix = [[''] * length for _ in range(depth)] 
            row, direction = 0, 1 
            for col in range(length): 
                matrix[row][col] = '*' 
                if row == 0: 
                    direction = 1 
                elif row == depth - 1: 
                    direction = -1 
                row += direction 

            # fill characters 
            index = 0 
            for i in range(depth): 
                for col in range(length): 
                    if matrix[i][col] == '*' and index < len(rails_str[i]): 
                        matrix[i][col] = rails_str[i][index] 
                        index += 1 
                index = 0 

            plain_text = "" 
            row, direction = 0, 1 
            for col in range(length): 
                plain_text += matrix[row][col] 
                if row == 0: 
                    direction = 1 
                elif row == depth - 1: 
                    direction = -1 
                row += direction 

            print("Cipher Text: ", cipher_text) 
            print("Plain Text:  ", plain_text, "\n") 

        case 0: 
            print("\nProgram exited successfully!") 

        case _: 
            print("\nEnter correct choice!\n")
