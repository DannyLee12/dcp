"""
We're given a hashmap associating each courseId key with a list of courseIds
values, which represents that the prerequisites of courseId are courseIds.
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'],
          'CSC100': []}, should return ['CSC100', 'CSC200', 'CSC300'].
"""

courses = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'],
          'CSC100': []}


def ordering(courses, items=None):
    while courses:
        if not items:
            items = []
            for course, prereq in courses.items():
                # Append all courses without prerequisites
                if not prereq:
                    items.append(course)
            for c in items:
                del courses[c]

        else:
            for course, prereq in courses.items():
                for c in prereq:
                    valid = True
                    if not c in items:
                        valid = False
                        break
                if valid:
                    items.append(course)
            for c2 in items:
                try:
                    del courses[c2]
                except KeyError:
                    pass

    return items


if __name__ == '__main__':
    assert ordering(courses) == ['CSC100', 'CSC200', 'CSC300']
