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


if __name__ == '__main__':
    assert reverse_words("hello world here") == "here world hello"
