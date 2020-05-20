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
courses_invalid = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC200'],
                   'CSC100': []}


def ordering(courses, items=None):
    while courses:
        if not items:
            items = []
        dels = []
        for course, prereq in courses.items():
            if not prereq:
                items.append(course)
                dels.append(course)
            else:
                for c in prereq:
                    valid = True
                    if not c in items:
                        valid = False
                        break
                if valid:
                    items.append(course)
                    dels.append(course)
        if not dels:
            return None

        for d in dels:
            del courses[d]

    return items


if __name__ == '__main__':
    assert ordering(courses) == ['CSC100', 'CSC200', 'CSC300']
    assert ordering(courses_invalid) is None
