"""
Find an efficient algorithm to find the smallest distance (measured in number
of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat
hello cat dog dog hello cat world", return 1 because there's only one word
"cat" in between the two words.
"""


def smallest_distance(s: str, word1: str, word2: str) -> int:
    """Return the smallest distance between two words in a string of words"""
    words = s.split(" ")
    n = len(words)

    def create_wordlist(words, word):
        wordlist = [words.index(word)]
        pos = wordlist[-1]
        while pos < n:
            try:
                wordlist.append(words.index(word, pos + 1))
            except ValueError:
                break
            pos = wordlist[-1]
        return wordlist

    wordlist_1 = create_wordlist(words, word1)
    wordlist_2 = create_wordlist(words, word2)

    min_distance = float("inf")
    for x in wordlist_1:
        for y in wordlist_2:
            min_distance = min(min_distance, abs(y - x))

    return min_distance - 1


if __name__ == '__main__':
    assert smallest_distance("dog cat hello cat dog dog hello cat world",
                             "hello", "world") == 1
    assert smallest_distance("dog cat hello cat dog dog hello cat world",
                             "dog", "cat") == 0
