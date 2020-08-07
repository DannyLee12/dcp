"""
You are given a list of data entries that represent entries and exits of groups
of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people
in the building. Return it as a pair of (start, end) timestamps. You can assume
the building always starts off and ends up empty, i.e. with 0 people inside.
"""


def busiest_time(l: list, flag=None) -> tuple:
    """Return the busiest time given enters and exits"""
    current, max_val = 0, 0
    start, end = 0, 0
    for x in sorted(l, key=lambda x: x["timestamp"]):
        if x["type"] == "enter":
            current += x["count"]
        elif x["type"] == "exit":
            current -= x["count"]
        if current > max_val:
            flag = True  # Set flag to know when to close the interval
            max_val = current
            start = x["timestamp"]
        elif flag: # if the start has been set recently
            end = x["timestamp"]
            flag = False

    return start, end


if __name__ == '__main__':
    print(busiest_time([{"timestamp": 1, "count": 3, "type": "enter"},
                        {"timestamp": 2, "count": 3, "type": "exit"},
                        {"timestamp": 3, "count": 2, "type": "enter"},
                        {"timestamp": 4, "count": 2, "type": "exit"}]))
