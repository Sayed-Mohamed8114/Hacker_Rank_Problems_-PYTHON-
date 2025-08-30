class Person:
    def __init__(self,initialAge):
        # we can't add self.age instead of initialAge because it will be undefined we need to use it first 
        #then assign it to self.age
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
            self.age=0
        else:
            self.age=initialAge
            
    def amIOld(self):
        if self.age <13:
            print("You are young.")
        elif 13<=self.age<18:
            print("You are a teenager.")
        else:
            print("You are old..")
            
    def yearPasses(self):
        # Increment the age of the person in here
        self.age+=1
        
        
#for the number of test cases 
t = int(input()) # expeected input 4 


# calculate the age now and after 3 years 
for i in range(0, t):      # make the loop for the number of the cases 
    age = int(input())     #take the age of the person      
    p = Person(age)        #assign the age to the class person 
    p.amIOld()             # check the age 
    for j in range(0, 3):  # increment the age 3 times 
        p.yearPasses()       
    p.amIOld()
    print("")