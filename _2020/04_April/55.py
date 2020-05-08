"""
Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric
    string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url.
    If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
"""

import string
import random


class URL:
    urls = {}

    def shorten(self, url):
        if url in self.urls.values():
            shorter_url = next(k for k, v in self.urls.items() if v == url)
        else:
            shorter_url = "".join(random.choice(string.ascii_letters + string.
                                            digits) for _ in range(6))
            self.urls[shorter_url] = url
        return shorter_url

    def restore(self, short_url):
        if short_url in self.urls:
            return self.urls[short_url]
        return None


def shorten(url):
    global u
    return u.shorten(url)


def restore(short_url):
    global u
    return u.restore(short_url)


if __name__ == '__main__':
    global u
    u = URL()
    v = shorten("https://apple.com")
    print(restore(v))
    assert restore(shorten("http://reddit.com")) == "http://reddit.com"
