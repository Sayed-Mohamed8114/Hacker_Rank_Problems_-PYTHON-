#make an application to calculate how many one in the binary of number it must be following each other 
# and convert the number to binary 

#examole : 125 -> 1111101 so the output will be 5

def to_binary(user_input):
    reminder=""
    while user_input>0:
        reminder =str(user_input%2) + reminder 
        user_input=user_input//2
    return reminder if reminder else "0"

def count_the_ones(n):
    binary=to_binary(n)
    max_count = current_count = 0
    for digit in binary:
        if digit == '1':
          current_count += 1
          max_count = max(max_count, current_count)
        else:
           current_count = 0
    return max_count

if __name__=='__main__':
    n=int(input('enter the number : '))
    print(to_binary(n))
    print(count_the_ones(n))