class car:
    def __init__(self,body,engine,tyre):
        self.body1 = body
        self.engine1 = engine
        self.tyre1  = tyre

    def mileage(self):
        print("mileage of this car",self.tyre1)

c= car("solid","v6","radial")
print(c)

class tata(car):
    pass

t = tata("solid","v8","radial22")
print(t)
t.mileage()