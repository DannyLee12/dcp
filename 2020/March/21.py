"""
Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


def find_rooms(l: list) -> int:
    """Determine the number of rooms required"""
    # Probably makes sense to sort the times by start time
    starts = sorted(start for start, end in l)
    ends = sorted(end for start, end in l)

    # Looking for max number of overlapping starts and ends
    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    n = len(l)
    while i < n and j < n:
        if starts[i] < ends[j]:
            # if the endtime is after the startime of the next meeting
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1

    return current_max


if __name__ == '__main__':
    print(find_rooms([(30, 75), (0, 50), (60, 150)]))
