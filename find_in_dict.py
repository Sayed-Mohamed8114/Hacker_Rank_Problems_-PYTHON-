num = int(input())   
my_dict = {}

for _ in range(num):
    line = input().split()
    key = line[0]
    value = line[1]
    my_dict[key] = value

try:
    while True:
        name = input("Enter name (or type exit): ")
        if name == "exit":
            break
        if name in my_dict:
            print(f'{name}={my_dict[name]}')
        else:
            print("Not found")
except EOFError:
    pass

'''
gave it the numbers of operations in the beganning then the name and for ex the passwords and then return gave him names to search or exit to go out
ex:
2
sayed 1234
mohamed 567 
sayed --> sayed = 1234
amr -> not found 
exit ..
'''