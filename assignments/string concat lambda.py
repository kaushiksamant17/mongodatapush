#Try to write a lambda function which can return a concatination of all the string that we will pass
a =[]
aa = lambda *args : " ".join([i for i in args])


print(aa("kesto","dd","ooo"))