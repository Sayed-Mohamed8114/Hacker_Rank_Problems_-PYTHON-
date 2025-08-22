# the usage of any and all functions to check if all >0 and any of them is palindorme 


def  search_for_palindorme(i):
    i_str=str(i)
    return i_str==i_str[::-1]
        
num=int(input())
my_list=list(map(int,input().split()))

# Step 1: Check if all numbers are positive
if all(i > 0 for i in my_list):
    # Step 2: Check if any number is palindromic
    if any(search_for_palindorme(i) for i in my_list):
        print(True)
    else:
        print(False)
else:
    print(False)
