"""
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two
middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
print out:

2
1.5
2
3.5
2
2
2

"""

from statistics import median


def current_median(l: list):
    """Brute Force"""
    new_list = []
    for i, x in enumerate(l):
        if not new_list:
            new_list.append(x)
        else:
            flag = False
            for j, item in enumerate(new_list):
                if x <= item:
                    new_list.insert(j, x)
                    flag = True
                    break
            if not flag:
                new_list.append(x)
        # i is the length of the new_list
        if i == 0:
            print(new_list[0])
        elif i % 2 != 0:
            print((new_list[i//2] + new_list[i//2 + 1])/2)
        else:
            print(new_list[i//2])


if __name__ == '__main__':
    current_median([2, 1, 5, 7, 2, 0, 5])
