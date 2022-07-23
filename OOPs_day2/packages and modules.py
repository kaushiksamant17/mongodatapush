'''packages are the folder where pre-defined codes are written
and kept for reusability
modules are the files that are coded in the package folder'''
import test1
print(test1.__dict__)
obj33 = test1.Person("kaushik11","samant11","abc@gmail.com",2022)
print(obj33.name1)