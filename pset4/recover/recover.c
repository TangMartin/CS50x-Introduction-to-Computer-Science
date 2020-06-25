#include <cs50.h>       
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 512
//1. Open Memory Card
    //FILE *f = fopen(filename, "r")
//2. Look for JPEG
    //Every JPEG begins with a header (0xff, 0xd8, oxff, or 0xe0/1/2/3/4/5.../f)
    //JPEG are stored back-to-back
    //Each block is 512 Bytes
//3. Open a new JPEG File
//4. Write 512 Bytes tunil a new JPEG is found
//5. Stop at the end of the file

//Read the memory card using fread(data, size, number, inptr)
//Use buffer[0] == 0xff

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("Only Two Command-Line Arguemnt");
        return 1;
    }
    
    char* file = argv[1];
    
    FILE* input = fopen(file, "r");
    
    if(input == NULL)
    {
        printf("Invalid File:%s\n", argv[1]);
        return 1;
    }
    // create buffer
    unsigned char buffer[BUFFER_SIZE];

    // filename counter
    int filecount = 0;
    
    FILE* picture = NULL; 
    
    // check if we've found a jpeg yet or not
    int jpg_found = 0; //false
    
    // go through cardfile until there aren't any blocks left
    while (fread(buffer, BUFFER_SIZE, 1, input) == 1)
    {
        // read first 4 bytes of buffer and see if jpg signature using bitwise on last byte
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xe0) == 0xe0)
        {
            if (jpg_found == 1)
            {
                // We found the start of a new pic so close out current picture
                fclose(picture);
            }
            else
            {
                // jpg discovered and now we have the green light to write
                jpg_found = 1;
            }
            
            char filename[8];
            sprintf(filename, "%03d.jpg", filecount);
            picture = fopen(filename, "a");
            filecount++;
        }
        
        if (jpg_found == 1)
        {
            // write 512 bytes to file once we start finding jpgs
            fwrite(&buffer, BUFFER_SIZE, 1, picture);
        }
        
    }

    // close files
    fclose(input);
    fclose(picture);

    return 0;

}
