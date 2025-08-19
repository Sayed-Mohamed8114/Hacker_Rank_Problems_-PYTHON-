def checker(s):
    if any (s.isalnum() for s in s):
        print('True')
    else:
        print('False')
    
    if any (s.isalpha() for s in s):
        print('True')
    else:
        print('False')
    
    if any (s.isdigit() for s in s ):
        print('True')   
    else :
        print('False')
        
    if any (c.islower() for c in s):
        print('True')
    else:
        print('False')
    
    if any (c.isupper() for c in s ):
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    s = input()
    checker(s)