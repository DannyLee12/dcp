"""
Given a string of words delimited by spaces, reverse the words in string. For
example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this
operation in-place?

"""


def reverse_words(s: str) -> str:
    """Reverse words in a string"""
    # Split on the space, reverse and join on a space
    return " ".join(reversed(s.split(" ")))


def reverse_in_place(s: str) -> str:
    """Reverse the string in place"""
    # Reverse the entire string
    a = [c for c in s]

    def reverse_(a, start, end):
        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1
        return a

    a = reverse_(a, 0, len(a) - 1)

    start_of_word = 0
    for i, x in enumerate(a):
        if x == " ":
            reverse_(a, start_of_word, i - 1)
            start_of_word = i + 1

    reverse_(a, start_of_word, len(a) - 1)

    return "".join(a)


if __name__ == '__main__':
    assert reverse_words("hello world here") == "here world hello"
    print(reverse_in_place("hello world here"))
    assert reverse_in_place("hello world here") == "here world hello"
    assert reverse_in_place("hello a world b here") == "here b world a hello"
