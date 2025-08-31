# Get names of students with the second-lowest score and sort alphabetically
#nested list

n=int(input('enter your limit of the students :').strip())
student=[]
for i in range(n):
    name=input().strip()
    grade=float(input().strip())
    student.append([name,grade])
    
unique_scores = sorted(set(grades for name, grades in student))

if len(unique_scores) > 1:
    second_lowest_score = unique_scores[1]
else:
    print("Not enough unique scores to determine the second-lowest.")
    exit()

# Get names of students with the second-lowest score and sort alphabetically
second_lowest_students = sorted([name for name, score in student if score == second_lowest_score])

# Print each name on a new line
for student in second_lowest_students:
    print(student)


