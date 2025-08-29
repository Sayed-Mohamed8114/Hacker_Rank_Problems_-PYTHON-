# print form 1 to the number the user will input in the hexa , binary , octal and decimal shapes 


def to_binary(n):
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result if result else "0"

def to_octal(n):
    result = ""
    while n > 0:
        result = str(n % 8) + result
        n = n // 8
    return result if result else "0"

def to_hexa(n):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while n > 0:
        result = hex_digits[n % 16] + result
        n = n // 16
    return result if result else "0"

def print_formatted(n):
    for i in range(1, n + 1):
        width=len(to_binary(n)) # here to calculate the len of the binary because it is the largest one
        dec = str(i)
        octal = to_octal(i)
        hexa = to_hexa(i)
        binary = to_binary(i)
        #this is good formatted but we need to make it all go with the binary because it is the largest between them
        #print("{:>5} {:>5} {:>5} {:>5}".format(dec, octal, hexa, binary))
        # now to print it correctly
        print(dec.rjust(width),octal.rjust(width),hexa.rjust(width),binary.rjust(width))
        #now with thos line it will formatted the width with the value of the binary we need 

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_formatted(n)