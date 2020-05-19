"""
What does the below code snippet print out? How can we fix the anonymous
functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())

"""

if __name__ == '__main__':
    functions = []
    for i in range(10):
        functions.append(lambda: i)

    for f in functions:
        print(f())

    #  In the original instance, there is no value passed to the function
    #  and so it is called with CURRENT value of i. That is set to 9 therefore
    #  the loop will print '9' ten times

    # Expected Behavior:

    functions = []
    for i in range(10):
        functions.append(lambda i=i: i)

    for f in functions:
        print(f())
