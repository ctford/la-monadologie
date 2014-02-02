def foo(a):

    log = []

    b = abs(a)
    log.append("Ensure input is not negative.")

    c = percent(b, 20)
    log.append("Take 20 percent.")

    d = c + 5
    log.append("Add tax.")

    return (d, log)


def percent(x, p):
    return x / p * 100


class writer:

    def __init__(self, value, output=[]):
        self.value = value
        self.output = output

    def bind(self, f):
        (value, log) = f(self.value)
        output = list(self.output)
        output.append(log)
        return writer(value, output=output)


def writer_foo(a):
    return writer(a) \
            .bind(lambda x: (abs(x), "Ensure input is not negative.")) \
            .bind(lambda x: (percent(x, 20), "Take 20 percent.")) \
            .bind(lambda x: (x + 5, "Add tax."))















