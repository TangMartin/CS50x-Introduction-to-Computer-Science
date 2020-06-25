#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int countletters();

int main(void)
{
    int words = 1;
    int sentences = 0;
    int letters = 0;

    string text = get_string("Text: ");

    for(int i = 0; i < strlen(text); i++)
    {
        if((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            letters = letters + 1;
        }
        else if(text[i] == ' ')
        {
            words = words + 1;
        }
        else if(text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences = sentences + 1;
        }
    }

    //printf("letters: %i; words: %i; sentences: %i\n", letters, words, sentences);

    float index = (0.0588 * (float) letters * (100 / (float) words)) - (0.296 * (float) sentences * (100 / (float) words)) - 15.8;


    if(index > 1 && index < 16)
    {
        printf("Grade %i\n", (int) round(index));
    }
    else if(index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Before Grade 1\n") ;
    }


}



