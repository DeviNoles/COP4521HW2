import math
class Student:
    firstName=""
    lastName=""
    gender=""
    level=""
    gpa=""
    def __init__(self, firstName="", lastName="", gender="",level="",gpa=""):
        if(gender.lower() != "m" and gender.lower() != "f" and gender.lower() != "male" and gender.lower() != "female"):
            print("Gender Error")
        elif(level.lower() != "freshman" and level.lower() != "sophomore" and level.lower() != "junior" and level.lower() != "senior"):
            print("Class Error")
        else:
            self.firstName = firstName
            self.lastName = lastName
            self.gender = gender
            self.level = level
            self.gpa = gpa
            
        if(float(self.gpa)>4):
           # print("DA GP IS ", self.gpa)
            self.gpa=4

        
    def show_myself(self):
        print("First Name: "+self.firstName)
        print("Last Name: "+self.lastName)
        print("Gender: "+self.gender)
        print("Class Level: "+self.level)
        print("GPA: "+str(self.gpa))

        
    def study_time(self,st):
        gp = float(self.gpa) + math.log10(st)
       # print(math.log10(st))
        self.gpa = gp
       # print(self.gpa)
        if(float(self.gpa)>4):
            self.gpa=4
s1 = Student("Mike", "Barnes", "Male", "Freshman", 4)
s2 = Student("Jim", "Nickerson", "Male", "Sophomore", 3)
s3 = Student("Jack", "Indabox", "Male", "Junior", 2.5)
s4 = Student("Jane", "Miller", "Female", "Senior", 3.6)
s5 = Student("Mary", "Scott", "Female", "Senior", 2.7)

student_list = [s1,s2,s3,s4,s5]

for i in student_list:
    i.show_myself()
    i.study_time(5)
    i.show_myself()