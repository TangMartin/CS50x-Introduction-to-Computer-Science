#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int height = -1;
    while(height > 8 || height < 1)
    {
        height = get_int("Height: ");
    }
    
    int space = height - 1;
    
    for(int x = 0; x < height; x++)
    {
                
        for(int y = space; 0 < y; y--)
        {
            printf(" ");
        }
        space -= 1;
    
        for(int y = x; y >= 0; y--)
        {
            printf("#");
        }
        printf("\n");
    }

}