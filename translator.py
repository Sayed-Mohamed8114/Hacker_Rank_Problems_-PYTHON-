# to take a word and any vowel <a-e-i-o-u> replace it with s
def translate(word):
    translation = ""  
    
    for letter in word:
        if letter.lower() in "aueio":  
            if letter.isupper():
                translation = translation + "S"  
            else:
                translation = translation + "s" 
        else:
            translation = translation + letter  
    
    return translation  

word = input("Enter the word to replace the vowels with (s): ")
print(translate(word))

        