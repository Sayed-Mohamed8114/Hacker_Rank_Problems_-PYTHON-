
students_dic={}
n=int(input('enter the number of the students : ').strip())    
for i in range(n):
    std=input('enter student name : ').strip()
    grades = list(map(float, input("Enter the grades : ").strip().split()))
    students_dic[std]=grades

selcted_name=input('enter the name that you want : ').strip()    
if selcted_name in students_dic:
    average = sum(students_dic[selcted_name]) / len(students_dic[selcted_name])
    print(f"{average:.2f}")
else:
    print('not found ')    
