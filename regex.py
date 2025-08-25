# check if have regex

num=int(input())
regex='+*?'
for x in range(num):
    string=input()
    has_regex=False
    for i in range(len(string)-1):
        if string[i] in regex and string[i+1] in regex:
            has_regex=True
            break
    print(False if has_regex else True)

# check if the string have a regex in it or not 

'''
import re

for x in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)'''  