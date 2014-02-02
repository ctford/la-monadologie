class identity:
    def __init__(self, value):
        self.value = value

    def bind(self, f):
        value = f(self.value)
        return identity(value)
