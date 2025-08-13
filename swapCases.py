def swap_cases(store):
    new_str=""
    for char in store:
        if char.isupper():
           new_str+=char.lower()
        elif char.islower():
           new_str+=char.upper()
        else:
            new_str+=char
            
    return new_str        
        
str1=input('enter the string: ')  
result=swap_cases(str1)        
print(result) 