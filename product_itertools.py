import itertools

list1=list(map(int,input().split()))
list2=list(map(int,input().split()))

product=itertools.product(list1,list2)
for item in product:
    print(f'({item[0]},{item[1]})',end=" ")
    
'''
1 2 3 4 
5 6 7 8
(1,5) (1,6) (1,7) (1,8) (2,5) (2,6) (2,7) (2,8) (3,5) (3,6) (3,7) (3,8) (4,5) (4,6) (4,7) (4,8) 
'''