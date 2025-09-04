# the permutations --> is all the possible arrangements of a set of items where the order matters.
# apermutations(n,r) = ((n)!/ (n-r) !)
import itertools
# to make them all the input on one line
s,num=input().split()
num=int(num)
# we use the sorted to sort based on a alpha sort
result=itertools.permutations(sorted(s),num)
for item in result:
    print("".join(item))
    
#input ex --> abc 2