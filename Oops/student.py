class student:

    name:str

    id:str

    gender:str

    age:int

    course:str

    contact:str

    address:str

    def set_student(self,name,id,gender,age,course,contact,address):

        self.id=id

        self.name=name

        self.id=id

        self.gender=gender

        self.age=age

        self.course=course

        self.contact=contact

        self.address=address

    def display_student(self):

        print(self.id,self.name)

# creating objects

student_instance=student()

student_instance.set_student(100,"amal","male",24,"django",22334455,"address line 1")

student_instance.display_student()



        
