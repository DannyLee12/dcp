"""
Create a basic sentence checker that takes in a stream of characters and
determines whether they form valid sentences. If a sentence is valid, the
program should print it out.

We can consider a sentence valid if it conforms to the following rules:

    The sentence must start with a capital letter, followed by a lowercase
    letter or a space.
    All other characters must be lowercase letters, separators (,,;,:) or
    terminal marks (.,?,!,‽).
    There must be a single space between each word.
    The sentence must end with a terminal mark immediately following a word.
"""

from string import ascii_lowercase


def is_sentence(s: str) -> None:
    """Print the string if it's a valid sentence"""
    # Start with a capital
    if s[0].islower():
        return

    # end with a terminal mark
    terminals = {".", "?", "!"}
    if s[-1] not in terminals:
        return

    valid_chars = {",", ";", ":", " "}
    [valid_chars.add(x) for x in ascii_lowercase]

    for i, c in enumerate(s[1:-1]):
        # is_valid
        if c not in valid_chars:
            return
        # Double space
        if c == " ":
            if s[i + 2] == " ":
                return

    print(s)


if __name__ == '__main__':
    is_sentence("This is a valid sentence.")
    is_sentence("This is not a  valid sentence.")