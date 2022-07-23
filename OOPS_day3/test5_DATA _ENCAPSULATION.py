#DATA ENCAPSULATION
class ineuron:
    def __init__(self):
        self.students1 = "data science"

    def students(self):
        print(self.students1)


i = ineuron()
i.students()
i.students1 = "maths"
i.students()




class ineuron1:
    def __init__(self):
        self.__students1 = "data science11"

    def students1(self):
        print(self.__students1)

    def student_change(self):
        self.__students1 = "CHANGED DATA VALUE USING METHOD"


i1 = ineuron1()
i1.students1()

#trying to change the value of private variable using object
i1.__students1 =" BIG DATA 1111"
i1.students1()

# we can see the value of private variable didn't change
'''if i have a private variable declared we can't change the value of the 
private variable just by using the object and assigning a new value . but 
for changing the value of a private variable we have to change it inside a 
class using a different method as shown above using student_change method
 so that the value of private variable can 
be oveririden . This is called Data Encapsulation'''

i1.student_change()
i1.students1()

'''that you are not suppose to allow the user to change the value of a 
private variable directly  like user can do it for a normal variable mentioned
above .The user should be able to change the private variable value 
stored in  a class and user wants to modify the private variable value
they should change it using only a method name as shown above '''