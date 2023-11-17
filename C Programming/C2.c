#include <stdio.h>
#include <string.h>

/*
 * This C program takes a sentence as input from the user
 * and prints the sentence in reverse order.
 */

int main() {
    char sentence[1000];

    // Input from the user
    printf("Enter a sentence: ");
    fgets(sentence, sizeof(sentence), stdin);

    // Remove the newline character from the end of the input
    sentence[strcspn(sentence, "\n")] = '\0';

    // Print the sentence in reverse order
    printf("\nReversed Sentence: ");
    for (int i = strlen(sentence) - 1; i >= 0; i--) {
        printf("%c", sentence[i]);
    }

    printf("\n");

    return 0;
}
