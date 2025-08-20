# count the number of un repeated cities after remove the repeated 
n=int(input())
my_list=[]
for i in range(n):
    name=input()
    my_list.append(str(name))
myset=set(my_list)
print(len(myset))