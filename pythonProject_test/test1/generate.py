def key1(n):
    for i in range(n):
        if i%2 == 0:
            yield i

for i in range(20):
    b = key1(i)
    print(f"{i}th iteration output {list(b)}")



