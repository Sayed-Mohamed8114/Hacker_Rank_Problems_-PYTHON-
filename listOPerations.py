#given len of the list and number of some operations then do it and then print the number of remining items in the set

n = int(input())  
my_set = set(map(int, input().split())) 

num_of_operations = int(input())  
for i in range(num_of_operations):
    line = input().split()  # Split the line by spaces
    
    if line[0].lower() == "remove":
        try:
            my_set.remove(int(line[1]))  # Try to remove the element
        except KeyError:
            pass  # If the element is not found, do nothing (or handle as desired)
    elif line[0].lower() == "pop":
        if my_set:  # Make sure the set is not empty before popping
            my_set.pop()
    elif line[0].lower() == "discard":
        my_set.discard(int(line[1]))  # Discard the element, no error if not found
        
#print the sum of remining items 
print(sum(my_set))