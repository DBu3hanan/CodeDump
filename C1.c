#include <stdio.h>
#include <string.h>
#include <ctype.h>

/*
 * This C program takes a sentence as input from the user and performs various analyses:
 * - Counts the number of words, letters, vowels, consonants, digits, and special characters.
 * - Determines the longest word in the sentence.
 * - Checks if the entire sentence is a palindrome (case-insensitive).
 */

int isVowel(char c) {
    c = tolower(c);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int isPalindrome(char word[]) {
    int length = strlen(word);
    for (int i = 0; i < length / 2; i++) {
        if (tolower(word[i]) != tolower(word[length - 1 - i])) {
            return 0;
        }
    }
    return 1;
}

int main() {
    char input[1000];
    int words = 0, letters = 0, vowels = 0, consonants = 0, digits = 0, specials = 0;

    printf("Enter a sentence: ");
    scanf(" %[^\n]", input);

    for (int i = 0; input[i] != '\0'; i++) {
        if (isalpha(input[i])) {
            letters++;
            if (isVowel(input[i])) {
                vowels++;
            } else {
                consonants++;
            }
        } else if (isdigit(input[i])) {
            digits++;
        } else if (!isspace(input[i])) {
            specials++;
        }

        if (isspace(input[i])) {
            words++;
        }
    }

    if (strlen(input) > 0) {
        words++;
    }

    printf("\nAnalysis:\n");
    printf("Number of words: %d\n", words);
    printf("Number of letters: %d\n", letters);
    printf("Number of vowels: %d\n", vowels);
    printf("Number of consonants: %d\n", consonants);
    printf("Number of digits: %d\n", digits);
    printf("Number of special characters: %d\n", specials);

    char longestWord[100] = "";
    char *token = strtok(input, " ");
    while (token != NULL) {
        if (strlen(token) > strlen(longestWord)) {
            strcpy(longestWord, token);
        }
        token = strtok(NULL, " ");
    }

    printf("\nLongest word: %s\n", longestWord);

    if (isPalindrome(input)) {
        printf("\nThe entire sentence is a palindrome.\n");
    } else {
        printf("\nThe entire sentence is not a palindrome.\n");
    }

    return 0;
}
