
import itertools

s,num=input().split()
num=int(num)
s_sorted=sorted(s)
combine=itertools.combinations_with_replacement(s_sorted,num)
for item in combine:
    print("".join(item))
    
# test case  ABC 2 ----> without repeatation ex ab == ba 

#result:
'''
        AA
        AB
        AC
        BB
        BC
        CC
'''
