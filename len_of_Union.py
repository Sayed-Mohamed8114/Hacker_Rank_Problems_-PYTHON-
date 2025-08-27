n=int(input())
my_set1=set(map(int,input().split()))

n2=int(input())
my_set2=set(map(int,input().split()))

union= my_set1.union(my_set2)

print(len(union))

# will remove the dublicate 