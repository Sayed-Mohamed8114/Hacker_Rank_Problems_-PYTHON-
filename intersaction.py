n1=int(input())
mylist=[]
line1=input().split()
for i in range(n1):
    mylist.append(int(line1[i]))
    
n2=int(input())
mylist2=[]
line2=input().split()
for i in range(n2):
    mylist2.append(int(line2[i]))
    # you can do this in one line my_set=set(map(int,input().split())) will work faster and better 

#remove dublicates
myset1=set(mylist)
myset2=set(mylist2)

common=myset1&myset2 # will print the intersaction between them (elements in both sets)
result=myset1 ^ myset2  # symmetric difference → elements in one set but not both 

for item in sorted(common):
   print(item)

print(len(common))

# taking to elements and print the len of the common var --> the numbers that appear in both sets  
