#include <stdio.h>
#include <ctype.h> // for character classification and transformation

int main() {
    char cipher_text[100]; 
    int key;
    char plain_text[100];
    int i;

    printf("Enter cipher text: ");
    fgets(cipher_text, sizeof(cipher_text), stdin); // using fgets to read a full line

    printf("Enter key: ");
    scanf("%d", &key);

    // decrypting the cipher text
    for (i = 0; cipher_text[i] != '\0'; i++) {
        char char_current = cipher_text[i];

        // to add blank space
        if (char_current == ' ') {
            plain_text[i] = char_current;
            continue;
        }

        // for upper-case characters
        if (isupper(char_current)) {
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
    printf("Cipher Text:  %s", cipher_text);
    printf("Plain Text:   %s", plain_text);

    return 0;
}
