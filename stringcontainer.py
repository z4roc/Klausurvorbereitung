type StringContainer = StringContainer
class StringContainer():
    def __init__(self, s: str):
        assert isinstance(s, str)
        self.s = s

    def __str__(self):
        return self.s

    def __repr__(self):
        return f"StringContainer({self.s})"

    def __lt__(self, other: StringContainer):
        return len(self.s) < len(other.s)

    def __eq__(self, other: StringContainer):
        return len(self.s) == len(other.s)

    def __add__(self, other: StringContainer):
        return StringContainer(self.s + other.s)

    def __sizeof__(self):
        return len(self.s)
