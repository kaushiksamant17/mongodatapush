class Person77:
    def __init__(self,name,surname,email,yob):
        self.name1 = name
        self.surname = surname
        self.email = email
        self.yob = yob

""" this self word is not a reserved keyword, instead
in python inside class when you define a function 
the first variable acts as a pointer to the class
that would help to access the arguements.
Instead of self word, you can write any other word ,
program would function similarly
basically the init method acts a construction the moment
we create object of the class by default the init method
would be called . therefore the init method arguements
values have been mentioned as arguement while creating
the object of the class person"""

''''sachin_data = Person77("sachin","samant","scc@gmail",1993)
print(sachin_data.name1)
print(sachin_data.surname)
print(sachin_data.email)
print(sachin_data.yob)''''

"""Once we create a object this object acts a variable 
for the class . like if we declare a = 10 and write
type(a) it would be int , similarly if we type (sachin_data)
the anwer would be <class '__main__Person' it indicates
 the  variable sachin_data is of data type  class person
 the coorelation exists like this and technically we call
 this variable sachin_data as an object"""