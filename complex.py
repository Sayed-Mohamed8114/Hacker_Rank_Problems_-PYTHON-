# to convert from the complex number to the regular one
# enter the complex number like this : 3+4j

import cmath

def complex_to_regular(complex_num):
    
    # Calculating modulus (magnitude)
    modulus = abs(complex_num)
    # Calculating argument (angle)
    argument = cmath.phase(complex_num)
    
    return modulus, argument
# Example usage
# :
complex_input = complex(input("Enter a complex number: "))  # e.g., 1+2j
modulus, argument = complex_to_regular(complex_input)

print(f"Modulus (magnitude): {modulus}")
print(f"Argument (angle in radians): {argument}")
