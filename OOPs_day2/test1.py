class person:
    def __init__(self,name,surname,yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

'''normally the self.name1 , self.surname1 acts as 
class variable and class attributes. These variables
are by default public . Therefore , wherever we create
object of this class we can use those. However, let's'
say that we want some of the variable to be restricted
in terms of usage.
then in that case we underscore sign befor the variabl
name like self._name1 instead of self.name, the underscore
sign indicates it is in protected mode now
there is no keyword called as public protected ,private
ideally if there is no underscore at the begining then
it is protected 
and if it's not there then that is public
so if it is double underscore(__) then it's private
if it is single underscore(_) it is protected
if there is no underscore then it is public
'''

kk = person("kaushik","samant",1989)
print(kk._name1)
'''normally if it is protected we would be able to call
it but in case if we have private and we call them
 then in that case it would throw error'''
try:
    print(kk.__surname1)
except Exception as e:
    print(e)
finally:
    print(kk._person__surname1)

'''if you see here ideally we normally try to call
private variable of any class using normal syntax as 
it is shown in try block then in that case it would 
throw an error but if in case the finally block code 
we try it would execute as it shows a different way 
to access the private variable using class and 
underscore'''