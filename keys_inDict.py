# make from the letters of the string keys to dictionary 
string=input().strip()
len1=len(string)
my_list=[]
for i in range(len1-1):
    if string[i]!=string[i+1]:
        my_list.append(string[i])
        
if string[-1] != string[-2]:
    my_list.append(string[-1])
    
my_dict = {key: None for key in my_list}