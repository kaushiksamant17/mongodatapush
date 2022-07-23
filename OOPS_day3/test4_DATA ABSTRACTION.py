#DATA ABSTRACTION
class ineuron:
    __students = "data science"
    fees = 35000

    def students11(self):
        print(" this is the class of ",ineuron.__students)


ii = ineuron()
ii.students11()
print(ii.fees)

print(ii._ineuron__students)

'''over here ,the private variable __students is a private and we can't
reach to a variable directly to the variable just with object .
Over here we have call the class(_ineuron) which store the variable student and it's
associated value and then only we aould be able to access the value of the 
 hidden variable/private variable . 
 SO we can say that the value of variable( --students) was hidden by declaring
 it privately and storing it in a class . Therefore this kind of hiding of 
  data of  variable in a class and directly not giving it a access is called
  a DATA ABSTRACTION'''

