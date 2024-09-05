# course_name="python django"

# print(type(course_name))

# expenses=[10000,12000,13000,14000]

# print(type(expenses))

class Employee:

    id:int

    name:str

    age:int

    gender:str

    department:str

# initializing instance variables=>constructor
# constructor unique name
# java=>classname()
# javascript=>costructor()
# python=>__init__()
# 

    def __init__(self,id,name,age,gender,dept):
        
        self.id=id

        self.name=name

        self.age=age

        self.gender=gender

        self.department=dept

    def display_employee(self):

            print(self.name,self.id,self.department)