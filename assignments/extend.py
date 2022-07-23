#extend function

def extend1(a):
    aa =[1,2,3,4]
    if type(a) == str:
        pass
    else:
        return ("enter string")
    for i in a :
        b = [i]
        aa = aa +b
    return aa

print(extend1("kaushik"))