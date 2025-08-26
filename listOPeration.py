number = int(input("enter the number of the operations : "))
my_list = []
for i in range(number):
    line = input().split()
    operation = line[0].lower()  # convert to lowercase once
    
    if operation == "insert": # gave the index and the value we want to insert 
        my_list.insert(int(line[1]), int(line[2]))  # convert both index and value to int
    elif operation == "print":
        print(my_list)
    elif operation == "remove":
        value = int(line[1]) if line[1].isdigit() else line[1]  # handle both string and int
        my_list.remove(value)
    elif operation == "append":
        value = int(line[1]) if line[1].isdigit() else line[1]  # handle both string and int
        my_list.append(value)
    elif operation == "sort":
        my_list.sort()
    elif operation == "pop":
        if my_list:
            my_list.pop()
    elif operation == "reverse":
        my_list.reverse()