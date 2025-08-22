#get the first letter of each word in a string and make it upper case

def solve(s):
    result=''
    
    for i in range(len(s)):
        if i==0 or (s[i-1]==' '):
            result+=s[i].upper()
        else:
            result+=s[i]
    return result

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)