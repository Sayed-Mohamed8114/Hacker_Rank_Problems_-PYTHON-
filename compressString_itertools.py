import itertools
# take an number from the user as an whole sequence of numbers '1222311'
# then the outbut will be (1, 1) (3, 2) (1, 3) (2, 1) the first number in the pracket is the numbers of howmany the seq repeated
num=input()
for n1,group in itertools.groupby(num):
    group_list=list(group)
    print(f'({len(group_list)}, {n1})',end=" ")
