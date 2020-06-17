"""
Implement the singleton pattern with a twist. First, instead of storing one
instance, store two instances. And in every even call of getInstance(), return
the first instance and in every odd call of getInstance(), return the second
instance.
"""


class DoubleTon:
    class SingleTon:
        def __init__(self, version):
            self.version = version

    s1 = SingleTon("first")
    s2 = SingleTon("second")
    call = 0

    def getInstance(self):
        self.call += 1
        if self.call % 2 == 0:
            return self.s1
        return self.s2


if __name__ == '__main__':
    d = DoubleTon()
    for i in range(10):
        print(d.getInstance().version)
