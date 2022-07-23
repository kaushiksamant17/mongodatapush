class person:

    def age(self,crnt_yr,yob ):
        return crnt_yr - yob

    def  email_in(self,email):
        print("your email id is ",email)

    def ask_name(self):
        name = input("enter your name")
        return name

    def ask_dob(self):
        dob = input("enter you birth")
        return dob


mandya = person()
muchhi = person()
kaalia = person()
pachaas = person()

print(mandya.ask_name())
print(mandya.ask_dob())
mandya.email_in("mandy@gmail.com")

kaalia.ask_dob()
print("your age kaalia is ",kaalia.age(2022,1992))

print(pachaas.ask_name())

print(muchhi.ask_name())