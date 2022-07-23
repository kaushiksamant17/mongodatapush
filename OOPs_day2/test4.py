class testing:

    def __init__(self,name,surname):
        self._name1 = name
        self.__surname = surname

    def _nameadd(self,current):
        print(f"your name is {current}")

    def _name11(self):
        return self._name1

    def _surnamedd(self):
        print(f"your surname is {self.__surname}")


class test1(testing):

    def __init__(self,yob,surname):
        self.yob1 = yob
        self.__surname = surname



obb1 = testing("kkaushi","ssamant")
print(obb1._testing__surname)
obb1._nameadd("kesto")
#obb1._testing__surnamedd()

ob2 = test1(1989,"samant222")
print(ob2.yob1)
ob2._nameadd("kesto222")
