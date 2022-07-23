# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    for i in range(10):
        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    first()

def first():
    a=1
    b=1
    print(a)
    print(b)
    for i in range(5):
       # print(f"this is the value of i : {i}")
        print("printing fibonacci")
        a,b = b,b+a
        print(b)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
