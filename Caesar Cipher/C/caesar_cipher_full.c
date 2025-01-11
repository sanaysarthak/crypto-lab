// Program in C to implement Caesar Cipher cryptography (both encryption and decryption)

#include <stdio.h>
#include <ctype.h>
#include <string.h> // include string.h for strlen

int main() {
    char plain_text[100]; 
    char cipher_text[100];
    int key, i, ch;

    printf("\nCaesar Cipher Encryption & Decryption Tool:\n");

    while (ch != 0) {
        printf("\nEnter 1 to Encrypt. \nEnter 2 to Decrypt. \nEnter 0 to Exit. \nEnter choice: ");
        scanf("%d", &ch);
        getchar(); // clear the newline character from the input buffer

        switch(ch) {

            // Encryption Case
            case 1:
                printf("\nEncrypting Caesar Cipher!\n");
                
                printf("\nEnter plain text: ");
                fgets(plain_text, sizeof(plain_text), stdin); // using fgets to read a full line

                // remove newline character if present
                size_t len = strlen(plain_text);
                if (len > 0 && plain_text[len - 1] == '\n') {
                    plain_text[len - 1] = '\0';
                }

                printf("Enter key: ");
                scanf("%d", &key);
                getchar(); // clear the newline character from the input buffer

                // encrypting the plain text into cipher text
                for (i = 0; plain_text[i] != '\0'; i++) {
                    char char_current = plain_text[i];

                    // to add blank space
                    if (char_current == ' ') {
                        cipher_text[i] = char_current;
                        continue;
                    }
                    // for upper-case characters
                    else if (isupper(char_current)) {
                        cipher_text[i] = (char)((((char_current - 'A') + key) % 26) + 'A');
                    }
                    // for lower-case characters
                    else if (islower(char_current)) {
                        cipher_text[i] = (char)((((char_current - 'a') + key) % 26) + 'a');
                    } 
                    // special characters remain unchanged
                    else {
                        cipher_text[i] = char_current; 
                    }
                }
                cipher_text[i] = '\0'; // adding null-termination at the end of cipher_text string

                // displaying the output
                printf("Plain Text:  %s\n", plain_text);
                printf("Cipher Text: %s\n", cipher_text);
                break;

            // Decryption Case
            case 2:
                printf("\nDecrypting Caesar Cipher!\n");

                printf("\nEnter cipher text: ");
                fgets(cipher_text, sizeof(cipher_text), stdin); // using fgets to read a full line

                // remove newline character if present
                len = strlen(cipher_text);
                if (len > 0 && cipher_text[len - 1] == '\n') {
                    cipher_text[len - 1] = '\0';
                }

                printf("Enter key: ");
                scanf("%d", &key);
                getchar(); // clear the newline character from the input buffer

                 // decrypting the cipher text into plain text
                for (i = 0; cipher_text[i] != '\0'; i++) {
                    char char_current = cipher_text[i];

                    // to add blank space
                    if (char_current == ' ') {
                        plain_text[i] = char_current;
                        continue;
                    }
                    // for upper-case characters
                    else if (isupper(char_current)) {
                        plain_text[i] = (char)((((char_current - 'A') - key + 26) % 26) + 'A'); 
                    }
                    // for lower-case characters
                    else if (islower(char_current)) {
                        plain_text[i] = (char)((((char_current - 'a') - key + 26) % 26) + 'a'); 
                    } 
                    // special characters remain unchanged
                    else {
                        plain_text[i] = char_current; 
                    }
                }
                plain_text[i] = '\0'; // adding null-termination at the end of plain_text string

                // displaying the output
                printf("Cipher Text:  %s\n", cipher_text);
                printf("Plain Text:   %s\n", plain_text);
                break;

            case 0:
                printf("\nProgram exited successfully!\n");
                break;

            default:
                printf("\nEnter correct choice!\n");
                break;
        } 
    }

    return 0;
}
