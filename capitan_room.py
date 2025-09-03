num=int(input())
num = int(input())  
room_numbers = list(map(int, input().split()))  

# Convert the list to a set to get unique room numbers (remove duplicates)
unique_rooms = set(room_numbers)  

# Sum of all room numbers (with duplicates included)
sum_of_room_numbers = sum(room_numbers)  

# Sum of unique room numbers (without duplicates)
sum_of_unique_rooms = sum(unique_rooms)  

# Formula explanation:
# (num * sum_of_unique_rooms) gives the total sum if every room appeared 'num' times
# Subtracting the actual sum leaves (num-1) * captain_room
# Divide by (num-1) to get the captain's room number
captain_room = (num * sum_of_unique_rooms - sum_of_room_numbers) // (num - 1)  

# Print the captain's room number
print(captain_room)


'''
example of the input 
num = 3
room_numbers = [1, 2, 3, 6, 2, 3, 1, 1, 2, 3]
the output will be f

'''