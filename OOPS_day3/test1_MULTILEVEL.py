#MULTILEVEL INHERITANCE
class bank:
    def transaction(self):
        print("total transcation value")

    def account_opening(self):
        print(" this wil show you account status")

    def deposit1(self):
        print("this will show the deposited amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show the transaction from HDFC to icici")


class ICICI(HDFC_bank):
    pass

aa = ICICI()
aa.hdfc_to_icici()
aa.deposit1()
aa.transaction()
aa.account_opening()

'''If we see here the parent class bank feature is inherited by HDFC_bank
and now the HDFC_bank has features inherited from parent class
Now ICICI class inherits the features from class HDFC _bank which in 
turn inherits the grand parents class Bank features. 
This is called MULTILEVEL INHERITANCE, SO HERE THE BANK CLASS ACTS AS A 
PARENT CLASS AND IT'S FEATURE ARE INHERITED BY CHILD CLASS HDFC_bank CLASS\
AND NEXT IS THE GRAND CHILD ICICI WHICH INHERTED FEATURES OF HDFC BANK \
AND ALSO BANK CLASS THROUGH CLASS HDFC _BANK CLASS'''