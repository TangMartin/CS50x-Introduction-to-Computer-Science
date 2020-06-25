// Implements a dictionary's functionality
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

//wordcount
int(wordcount) = 0;


// Returns true if word is in dictionary else false
bool check(const char *word)
{
    node *cursor = table[hash(word)];
    
    if (strcasecmp(cursor->word, word) == 0)
    {
        return true;
    }
    
    while(cursor->next != NULL)
    {
        cursor = cursor->next;
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int hash = (int) tolower(word[0]) - 97;
    return hash;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    char *buffer = malloc(LENGTH);
    
    if(buffer == NULL)
    {
        return false;
    }
    if(!file)
    {
        return false;
    }
    
    while (fscanf(file, "%s", buffer) != EOF)
    {
        node *n = malloc(sizeof(node));
        
        if(n == NULL)
        {
            return false;
        }
        
        strcpy(n->word, buffer);
        wordcount += 1;
        
        n->next=table[hash(buffer)];
        
        table[hash(buffer)] = n;
    }
    
    fclose(file);
    free(buffer);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return wordcount;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int n = 0; n < N ; n++)
    {
        node *cursor = table[n];
        
        while(cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);=
        }
        
        free(cursor);
    }
    return true;
}
