# the len of items in set 1 and not in set 2 
# first insert len of set1 then the set , insert the len of set2 then the set 

n=int(input())
my_set1=set(map(int,input().split()))

n2=int(input())
my_set2=set(map(int,input().split()))

difference=my_set1 - my_set2

print(len(difference))

