"""
What does the below code snippet print out? How can we fix the anonymous
functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())

"""

global n
n = 0


def fn():
    global n
    n += 1
    return n - 1


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
    # 1. - Using another function with a global variable
    functions = []
    for i in range(10):
        functions.append(fn)

    for _, f in enumerate(functions):
        print(f())

    # 2. Passing in a variable
    functions = []
    for i in range(10):
        functions.append(lambda i: i)

    for i, f in enumerate(functions):
        print(f(i))
