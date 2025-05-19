#include <stdio.h>
#include <ctype.h> // for character classification and transformation (example: tolower() )

int main() {
    char plain_text[100]; 
    int key;
    char cipher_text[100];
    int i;

    printf("Enter plain text: ");
    scanf("%s", plain_text);

    printf("Enter key: ");
    scanf("%d", &key);

    // encrypting the plain text
    for (i = 0; plain_text[i] != '\0'; i++) {
        char char_current = plain_text[i];

        // to add blank space
        if (char_current == ' ') {
            cipher_text[i] = char_current;
            continue;
        }

        // for upper-case characters
        if (isupper(char_current)) {
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

    return 0;
}
