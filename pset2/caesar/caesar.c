#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

string ciphertext ();

int main(int argc, string argv[])
{
    
    if(argc != 2)
    {
        printf("Fail");
        return 1;
    }
    
    for(int i = 0; i < strlen(argv[1]); i++)
    {
        if (isdigit(argv[1][i]))
        {
            continue;
        }
        else
        {
            printf("Fail");
            return 1;
        }
    }
    
    int key = atoi(argv[1]);
    string plaintext = get_string("Plain Text:");
    
    printf("ciphertext:");
    for(int j = 0; j < strlen(plaintext); j++)
    {
        if(islower(plaintext[j]))
        {
            printf("%c", (((plaintext[j] + key) - 97) % 26) + 97);
        }
        else if(isupper(plaintext[j]))
        {
            printf("%c", (((plaintext[j] + key) - 65) % 26) + 65);
            
        }
        else 
        {
            printf("%c", plaintext[j]);
        }
    }
    printf("\n");
}
