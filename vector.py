type Vector = Vector
class Vector:
    def __init__(self, x: int | float, y: int | float, z: int | float):
        types = [float, int]
        assert type(x) in types and type(y) in types and type(z) in types
        assert isinstance(x, (int, float))

        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y}, {self.z})'

    def scalar(self, v: Vector) -> int | float:
        return self.x * v.x + self.y * v.y + self.z * v.z


