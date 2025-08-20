# if it a subset of the big one or not 

num_of_element=int(input())
my_list=list(map(int,input().split()))  
num_of_element2=int(input())
what_will_be_checked=list(map(int,input().split()))
checker=0

for i in what_will_be_checked:
    if i in my_list:
        checker+=1

if checker==num_of_element2:
    print('true')
else:
    print('false')