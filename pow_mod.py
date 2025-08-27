# take 3 numbers and return a**b then module them on c
arr=[]
for i in range(3):
    num=input()
    arr.append(int(num))

result=arr[0]**arr[1]
mod=result%arr[2]
print(result)
print(mod)