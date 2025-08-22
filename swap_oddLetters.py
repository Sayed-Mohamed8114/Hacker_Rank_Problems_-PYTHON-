#a code to do this to a word ex : input= hacker , output = hce akr 

def strings(string):
    s1=''
    s2=''
    for i in range(len(string)):
        if i %2 ==0:
            s1+=string[i]
        elif i%2 !=0:
            s2+=string[i]
    return s1+ " " + s2

n=int(input())
for i in range(n):
    string=input()   
    print(strings(string))
