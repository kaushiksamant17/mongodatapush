#Try to print a prime number in between 1 to 1000

count = 0
for i in range(1,100):
    if i ==1:
        print(i)
    for j in range(1,i):
        if i%j == 0:
            count +=1
        else:
            pass
    if count == 1:
        print(i)
    count = 0