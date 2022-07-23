class Person:
    def __init__(kk,name,surname,age,yob):
        kk.name1 = name
        kk.surname1 = surname
        kk.age = age
        kk.yob=yob



#here we are creating just a generic function to calculat
#age
    def agecalc(kk):
        return 2022 - kk.yob

"""here if you see instead of self we wrote something
else and still acts as a pointer in OOPS concept
similary kk.name1 is a variable that take value from 
arguement name and that is passed in arguement list
 mentioned in by default(constructor) __init__
 """


anitaboni_data = Person("anita","kahar","aa@gmail.com",1993)
print(anitaboni_data.name1 +" "+anitaboni_data.surname1)
print(anitaboni_data.age)
print(type(anitaboni_data.yob))
print(type(anitaboni_data.name1))
print(type(anitaboni_data))
print(anitaboni_data.agecalc())

