numbers = list(map(int, input("Enter numbers separated by spaces: ").strip().split()))

unique_numbers= sorted(set(numbers), reverse=True)

if len(unique_numbers )>1:
    print(f'second element is {unique_numbers[1]}')
else:
    print('no second largest number ') 
    
#the second way very important*******
'''
n=int(input('enter the len of the list: ').strip())

while True:
     numbers = list(map(int, input("Enter numbers separated by spaces: ").strip().split()))
     if len(numbers)==n:
         break
     else:
         continue

unique_numbers= sorted(set(numbers), reverse=True)

if len(unique_numbers )>1:
    print(f'second element is {unique_numbers[1]}')
else:
    print('no second largest number ') 
'''