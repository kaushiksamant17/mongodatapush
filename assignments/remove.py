# remove function

def remove1(a):
    aa = [1, 2, 3, 4]
    for i in aa:
        if i == a:
            aa.remove(i)
    return aa


print(remove1(2))