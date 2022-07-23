FUNCTION POLYMORPHISM

#here i am declaring a function which performs addition
def test(a,b):
    return a+b

print(test(4,5))
print(test("kaushik ","samant"))

''' if we see the function test is performing addition as well as concatentation
based on the different data type it recieves. like a boy can be kid for a family
friend for  other friend, grandson for grandfather. The person same and based on
different situtation it's role change like the upper fucntion test 
This is called polymorphism one function or method taking multiple forms
based on data type '''

class ineuron:
    def students(self):
        print("print student details")


class class_type:
    def students(self):
        print("print the class type of students of class type")

'''over here we are declaring a fucnation that would transform it's behaviour
as per the input it recieve . IDeally this function is function polymorphism
 where it is taking the object of different class and per the object mentioned
 it would execute the function accordingly , one time it is executing 
 one time ineuron class and one time class_type class'''
def ineuron_external(a):
    a.students()

i = ineuron()

j = class_type()

ineuron_external(i)

ineuron_external(j)


'''class
object
constructor
inheritance
private
public
protected
abstraction
encaptulations
polymorpsim
package
modules
method overrridding

For all the concepts that we have discussed in our class point by point you have to write
atleast 10 examples

you have to make sure that use ineuron studnets , class , class type , number of courses
, affiliates , blog, internship , jobs as a reference example


sql workbench link windows - https://dev.mysql.com/downloads/windows/installer/8.0.html
different system - https://dev.mysql.com/downloads/workbench/'''