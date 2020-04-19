def reduce_expr(expr):
    for part in expr:
        part.reduce()
    


class Program:
    def __init__(self):
        self.expr = []

    def __repr__(self):
        return f"{', '.join(repr(x) for x in self.expr)}"

    def reduce(self):
        pass


class Height:
    def __repr__(self):
        return "Height"

    def reduce(self):
        pass


class Pop:
    def __repr__(self):
        return "Pop"

    def reduce(self):
        pass


class Toggle:
    def __repr__(self):
        return "Toggle"

    def reduce(self):
        pass


class Push:
    def __init__(self):
        self.expr = []

    def __repr__(self):
        return f"Push({', '.join(repr(x) for x in self.expr)})"

    def reduce(self):
        pass


class Negate:
    def __init__(self):
        self.expr = []

    def __repr__(self):
        return f"Negate({', '.join(repr(x) for x in self.expr)})"

    def reduce(self):
        pass


class Loop:
    def __init__(self):
        self.expr = []

    def __repr__(self):
        return f"Loop({', '.join(repr(x) for x in self.expr)})"

    def reduce(self):
        pass


class Suppress:
    def __init__(self):
        self.expr = []

    def __repr__(self):
        return f"Suppress({', '.join(repr(x) for x in self.expr)})"

    def reduce(self):
        pass
