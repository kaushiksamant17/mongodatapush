class kesto:

    _name = "kk"
    __surname = "samant"
    yob = 1989


class employee(kesto):

    empid = "24214"
try:
    kest = kesto()
    ks = employee()
    print(ks.empid)
    print(ks.yob)
    print(ks._name)
    print(ks._employee__surname)
    print(kest._kesto__surname)
except Exception as e:
    print(e)
finally:
    print(kest._kesto__surname)

'''over here if you see the private variable is not accessible
in child class employee as the variable is private in
parent class Kesto'''

'''Now if we try the same thing in functions then in that
case you have like private function and protected function'''

class func:

    _name=  "kaushik"
    __surname = "samant"
    yob = 1989

    def _age(self,current):
        return current - self.yob

    def __age(self,current):
        return current - self.yob

'''over here we are accessing the variable yob using self
otherwise we wont be able to access.'''
try:
    obj = func()
    print(obj._age(2022))
    print(obj.__age(2022))
except Exception as e:
    print(e)
finally:
    print(obj._func__age(2022))

'''so here as well it works in similar way the private
functions does not gets executed outside of the class'''

'''for that we have access those private function in a 
similar way as we access the private variable , the same
has been mentioned in finally block'''

'''now let us see whether in inheritance how the private ,
protected variable and funcation works'''

class func1(func):
    yob = 2020
    __surname1 = "samant1"
try:
    obj1 = func1()
    print(obj1._age(2024))
    print(obj1._name)
    print(obj1._func1__age(2025))
except Exception as e:
    print(e)
finally:
    print(obj1._func__age(2030))
    print(obj1._func__surname)
    print(obj1._func1__surname1)

'''as we can see the parent class private function is 
accessible using the object of child class and remaining
syntax remains same for accessing the private function '''
