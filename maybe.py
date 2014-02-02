def foo(a):

    if a:
        b = 128 / a - 1 # lambda a: 128 / a - 1
    else:
        return a

    if b:
        c = bar(b)
    else:
        return b

    if c:
        return baz(c)
    else:
        return c


def bar(x):
    return x - 1


def baz(x):
    return 4 / x


class maybe:

    def __init__(self, value):
        self.value = value

    def bind(self, f):
        value = f(self.value) if self.value else self.value
        return maybe(value)


def maybe_foo(a):
    return maybe(a) \
            .bind(lambda x: 128 / x - 1) \
            .bind(bar) \
            .bind(baz) \











