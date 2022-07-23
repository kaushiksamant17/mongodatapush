#METHOD OVERRIDING

class ineuron:
    def student(self):
        print("print the details of all the students")
    def achiever(self):
        print(" this is list acheivers")
    def hall_fame(self):
        print(" this is the list of hall of fame")


class ineuron_vision(ineuron):

    def student(self):
        print(" these are the filtered student for vision")

iv = ineuron_vision()
iv.student()

'''if we see here, we inherited the class ineuron in ineuron_vision
so all methods are inherited but we want to redefine or overide some 
method of of parent class ineruon therefore what we do we overide the 
student method of parent class ineuron by redefining  the same method 
again in ineuron_vision. now when we call the child class using the object
  and call the redfined method and you would see that the latest methode
  would get executed FROM THE CHILD CLASS  . This is called METHOD OVERRIDING '''