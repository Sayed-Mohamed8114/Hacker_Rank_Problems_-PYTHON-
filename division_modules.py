# calculate the division and the modules fot the arr
''''''
arr=[]
for i in range(2):
       num=input()
       arr.append(int(num))
# a//b
division=arr[0]//arr[1]
#a%b
mod=arr[0]%arr[1]
print(division)
print(mod)
my_Set=(division,mod)
print(my_Set)