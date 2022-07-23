#MULTIPLE INHERITANCE

class bank:
    def transaction(self):
        print("total transcation value")

    def account_opening(self):
        print(" this wil show you account status")

    def deposit1(self):
        print("this will show the deposited amount")

    def test(self):
        print("this is the test method of the bank class")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show the transaction from HDFC to icici")

    def test(self):
        print("this is the test method of the hdfc class")


class ineuron_bank:
    def account_status_ineuron(self):
        print( " this is the account status of ineuron")


class icici(HDFC_bank,bank):
    pass

cc = icici()
cc.hdfc_to_icici()
cc.account_opening()
cc.deposit1()
cc.transaction()

'''If we see here there are two different class which are not connected 
to each other in any way , this separate class are HDFC_bank, bank . 
however, the class icici wants the features from both the class that are not
connected to each other  therefore both the class are called while declaring
the class icici. this is called multiple inheritance. Here if we see
that parents class are bank (parent 1) and hdfc_bank(parent 2) and child
class is icici(child class)'''

'''now let us see, that we are writing a  method with same name in both class
and input of the method are different and let us see which one get printed 
if we call using the object of child class icici
 
'''

cc.test()

'''so ideally it would call the method from the class that has been called
first in the child class . Therefore the method from HDFC bank would be called
first as we can see that the child class icici(HDFC bank, bank) so in this
case the first arguement is HDFC bank and therefore the method of HDFC bank
would be called in such case of conflict.
'''

'''we can also try to include more than 2 parent class in one child class
let see'''

class kotak(HDFC_bank,bank,ineuron_bank):
    def kotak_bal(self):
        print(" this is kotak balance")


ko1 = kotak()
#calling methof of own class
ko1.kotak_bal()

#calling method of class ineuron_bank
ko1.account_status_ineuron()

#calling method of HDFC_bank
ko1.hdfc_to_icici()

#calling method of bank class
ko1.transaction()

#this would called method from hdfc bank as in arguement of kotak class
#class HDFC_bank comes first
ko1.test()

''' we can see here that we inherit from multiple classess as shown above
'''