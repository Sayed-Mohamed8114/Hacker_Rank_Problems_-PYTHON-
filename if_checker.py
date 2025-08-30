#if checker
#even  and odd numbers 

number=int(input()) #to take an number

if number%2==0 and number>20:
    print('Not Weird')
elif number%2==1:
    print('Wierd')
elif number%2==0 and number in range(2,5):
    print('Not Weird')
elif number%2==0 and number in range(6,20):
    print('Wierd')

