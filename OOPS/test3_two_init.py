class Person:
    def __init__(self,name,surname,age,yob):
        self.name1 = name
        self.surname1 = surname
        self.age = age
        self.yob = yob

    def __init__(self,name,surname,age):
        self.name1 = name
        self.surname1 = surname
#here if you see i am not using the age value as a
#reference but still would need to add the value
# as it is mentioned in arguement list



"""Here if you see that we have declared two same
init method but first have 5 arguements and second has 
4 arguements including self . But when we created
object and passed 4 arguements equal to first init 
it throws an error because the second init method
overrides the first init method and as per the latest
init method only three arguements are needed
so ideally in this case the second init method 
would take 3 argeuement and print the firt two value
name and surname,because here the third arguement age
is not referenced."""

durga = Person("momita","karan",29)
print(durga.name1)
print(durga.surname1)

kesto = Person("sunny","karan",20,2005)
print(kesto.name1)
print(kesto.surname1)