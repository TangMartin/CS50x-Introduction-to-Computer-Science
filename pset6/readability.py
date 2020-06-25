from cs50 import get_string

def main():
    words = 1
    letters = 0
    sentences = 0
    
    text = get_string("Text: ")
    
    for i in range(len(text)):
        if text[i].isspace() == True:
            words += 1
        elif (text[i].isalpha()) == True:
            letters += 1
        elif text[i] == "!" or text[i] == "." or text[i] == "?":
            sentences += 1
            
    l = (letters / words) * 100
    s = (sentences / words) * 100
    
    index = 0.0588 * l - 0.296 * s - 15.8
    
    if index > 16:
        print("Grade 16+")
    if index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade:{round(index)}")
    
main()

