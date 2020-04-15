"""
Given a string s and an integer k, break up the string into multiple lines such
that each line has a length of k or less. You must break it up so that words
don't break across lines. Each line has to have the maximum possible amount of
words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that
there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and
k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy",
"dog"]. No string in the list has a length of more than 10.
"""


def list_to_len(s: str, k: int) -> list:
    """Return a list of words less than k chars per line"""
    words = s.split()
    len_words = 0
    word_list = []
    word_snipppet = ""
    for word in words:
        if len(word) > k:
            return None
        if len_words + 1 + len(word) <= k:
            if not word_snipppet:
                word_snipppet += word
                len_words += len(word)
            else:
                word_snipppet += " " + word
                len_words += len(word) + 1
        else:
            word_list.append(word_snipppet)
            word_snipppet = word
            len_words = len(word)

    word_list.append(word_snipppet)

    return word_list


if __name__ == '__main__':
    print(list_to_len("the quick brown fox jumps over the lazy dog", 10))
    print(list_to_len("the 1234567890 brown fox jumps over the lazy dog", 10))