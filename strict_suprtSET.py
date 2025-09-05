#the strict super set : a set have all elements from another set and more element 

super_set=set(map(int,input().split()))
num_of_sets=int(input())
is_in=True
while num_of_sets>0:
    set1=set(map(int,input().split()))
    for i in set1:
        if i not in super_set:
            is_in=False
            break
        
    if not  is_in: # to reset the is_in to the next set 
        break
    
    num_of_sets-=1
print(is_in)

#input ex 
#1 2 3 4 5 6 
# 2
# 1 2 3 
# 4 5 6
# will return true 