# count how many egypt appear in the string
# will enter a long string and it will count how many "egypt" repeated in it 

string=input('enter a long string : ')
count=0
for i in range(len(string)):
    if string[i:i+5]=="egypt":
        count+=1
    
print(f'there are {count} egypt in your string..')       
