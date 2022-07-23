import test1

obb = test1.person("kaushik22","samant22",2022)
print(obb._name1)
print(obb._person__surname1)

'''if we see here we are directly importing the file frome
the same folder therefore we just import the module named
test1(test1.py) , however over here  we are importing the file
and accessing all the class and variable inside it be it 
private protected etc'''

'''now suppose if we want to access the files that are 
present in different folders then in that case there is also
a way to reach and access the module/file of different folder
for this we need to access the folder and then the tiles
and then it's classess'''

''' so over here if want to access the package/folder util
and modules/files containing in packages'''

import util.util1
obj11 = util.util1.util22("bulbasaur","squirtle",1999)
print(obj11._name1)

'''other way to do is below'''
from util.util1 import util22
obj2222 = util22("venosaur","warturtle",2002)
print(obj2222._util22__surname1)
print(obj2222.yob1)

'''packages and modules work like this and import function
works like this '''


